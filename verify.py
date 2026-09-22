#!/usr/bin/env python3
"""Verify FILL from outside: every fixing, every revealed hour, one key.

    pip install cryptography
    python3 verify.py              # everything in pulse/
    python3 verify.py 2026-09-21   # one day

A fixing verifies when pulse/marks/<day>.json hashes (sha256) to the
`marks_sha256` in pulse/fixings/<day>.json and the ed25519 signature over that
hex digest checks against the published key. An hour verifies when the bytes
at the path named in pulse/commitments/<day>.json hash to the committed sha256
and the signature over it checks. Hours committed to but not yet revealed are
listed with the time they are due (as_of + delay_hours). Exit 1 on any failure.
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
except ImportError:  # pragma: no cover
    sys.exit("pip install cryptography")

ROOT = Path(__file__).resolve().parent
PULSE = ROOT / "pulse"


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def signature_checks(public_key_hex: str, digest_hex: str, signature_hex: str) -> bool:
    try:
        Ed25519PublicKey.from_public_bytes(bytes.fromhex(public_key_hex)).verify(
            bytes.fromhex(signature_hex), digest_hex.encode()
        )
        return True
    except Exception:  # noqa: BLE001 — InvalidSignature and malformed input alike
        return False


def main(argv: list[str]) -> int:
    only = argv[1] if len(argv) > 1 else None
    failures: list[str] = []
    keys: set[str] = set()
    now = datetime.now(timezone.utc)

    fixings = sorted((PULSE / "fixings").glob("*.json"))
    if only:
        fixings = [f for f in fixings if f.stem == only]
    for f in fixings:
        fx = json.loads(f.read_text())
        marks = PULSE / "marks" / f"{f.stem}.json"
        keys.add(fx["public_key"])
        if not marks.exists():
            failures.append(f"{f.stem}: fixing without a marks file")
            continue
        digest = sha256_hex(marks.read_bytes())
        ok_hash = digest == fx["marks_sha256"]
        ok_sig = signature_checks(fx["public_key"], fx["marks_sha256"], fx["signature"])
        doc = json.loads(marks.read_bytes())
        head = (doc.get("fill") or {}).get("fill")
        status = "ok" if ok_hash and ok_sig else "FAIL"
        print(
            f"fixing {f.stem}: {status}  hash {'matches' if ok_hash else 'MISMATCH'}, "
            f"signature {'checks' if ok_sig else 'FAILS'}, FILL {head}, "
            f"methodology {fx['methodology_version']}, struck {fx['struck_at']}"
        )
        if not (ok_hash and ok_sig):
            failures.append(f"fixing {f.stem}")

    commitments = sorted((PULSE / "commitments").glob("*.json"))
    if only:
        commitments = [c for c in commitments if c.stem == only]
    for c in commitments:
        day = json.loads(c.read_text())
        delay = timedelta(hours=int(day.get("delay_hours", 24)))
        for h in day["hours"]:
            keys.add(h["public_key"])
            path = ROOT / h["path"]
            ok_sig = signature_checks(h["public_key"], h["sha256"], h["signature"])
            if not path.exists():
                due = datetime.fromisoformat(h["as_of"]) + delay
                late = "" if due > now else f" — OVERDUE by {now - due}"
                print(
                    f"hour {h['as_of']}: committed, not yet revealed (due {due.isoformat(timespec='minutes')}){late}; "
                    f"signature {'checks' if ok_sig else 'FAILS'}"
                )
                if not ok_sig:
                    failures.append(f"hour {h['as_of']} (signature)")
                continue
            digest = sha256_hex(path.read_bytes())
            ok_hash = digest == h["sha256"]
            board = json.loads(path.read_bytes())
            lanes = '"lane_id"' in path.read_text()
            print(
                f"hour {h['as_of']}: {'ok' if ok_hash and ok_sig and not lanes else 'FAIL'}  "
                f"{h['path']} hash {'matches' if ok_hash else 'MISMATCH'}, signature "
                f"{'checks' if ok_sig else 'FAILS'}, FILL {(board.get('index') or {}).get('fill')}"
                + (", LANE ROWS PRESENT" if lanes else "")
            )
            if not (ok_hash and ok_sig) or lanes:
                failures.append(f"hour {h['as_of']}")

    if len(keys) > 1:
        failures.append(f"more than one signing key: {sorted(keys)}")
    print(f"\nkey{'s' if len(keys) != 1 else ''}: {', '.join(sorted(keys)) or 'none'}")
    if failures:
        print(f"FAILED: {len(failures)} — " + "; ".join(failures))
        return 1
    print("verified: every fixing and every revealed hour checks against the one key")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
