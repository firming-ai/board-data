# board-data

The published half of **FILL**, the inference availability index — the share of
frontier discount-lane work that gets its discount inside the budget, struck by
[Firming](https://firming.ai) from a minute-resolution probe series on two
vantages. Machine-written: every commit here is the tape's own publisher or a
workflow, under the org identity. Methodology: `METHODOLOGY.md` in the tape,
version-pinned and hashed into every published number.

## The rule (methodology 1.2.1 §7, since 2026-09-22)

- **The daily fixing is public at strike.** Struck once at 00:10Z over the
  previous UTC day, final on publication, never restated.
- **The hourly board is public 24 hours after it is struck**, market-wide and
  per venue — the headline, FILL·FLEX, the venue children, the legs, every
  venue's last hour, the venues' 24-hour series and the batch queue per venue.
  No lane rows.
- **Everything live, and every per-lane series, is on the keyed feed.** A live
  per-lane fill is a routing signal; the signal is what the key buys. The
  index — the daily print, its marks, the history — is what stays open.
- **Each hour is committed to at the hour.** The public board for an hour is
  serialized as canonical JSON (sorted keys, no whitespace) the moment it is
  struck; the sha256 of those exact bytes is signed with the fixing's ed25519
  key and published at once; the bytes follow a day later at the path the
  commitment names. A board that does not hash to its commitment was rewritten.
  The delay hides nothing that could be restated.

The "24 h" is to the hourly timer's grain: the board struck at :05 yesterday is
published by the :05 run today. The first board under the rule, struck the hour
the rule took effect, was published at once so this repository carried the rule
from the start; it is committed to like every other hour.

## Layout

| path | what | when |
| :-- | :-- | :-- |
| `pulse/fixings/<day>.json` | the day's fixing: `marks_sha256`, ed25519 `signature`, `public_key`, methodology version, `struck_at` | at strike, 00:10Z |
| `pulse/marks/<day>.json` | the marks document the fixing signs — every lane's daily mark, the batch marks, the children, the headline; canonical JSON | at strike |
| `pulse/commitments/<day>.json` | one entry per hour: `as_of`, the `path` the bytes will appear at, their `sha256`, the `signature` over it, `public_key` | at the hour, rewritten as hours are struck |
| `pulse/hourly/<day>/<HH>.json` | the hour's public board, exact bytes — hash it | 24 h after `as_of` |
| `pulse/latest.json` | the newest revealed board, plus `published_at`, `delay_hours` and its commitment under `revealed` — a convenience copy; the hashed artifact is the hourly file | hourly |
| `pulse/PULSE.md` | the same board, rendered | hourly |
| `nightly/FLEX.md`, `nightly/flex-summary.json` | the hourly flex "shape" probe, summarized per lane over days (counts and percentiles) | twice daily |
| `sheet/` | the SDK's price sheet | on change |
| `watch/` | the daily tariff watch — venue list prices against the roster | daily |
| `nightly/<date>-*.json`, `receipts/` | the Offpeak-era night board and batch receipts, kept as records | frozen |

The read API at `https://fill.firming.ai/tape/<view>` serves the same split:
`marks`, `fixing`, `board_public`, `board_commitment`, `fill_1h_public`,
`venue_1h_public`, `roster_public`, `roster_event`, `tariff_latest`,
`batch_sized_public` and `tape_health` (what the tape is doing, never what it is
reading) without a key; the live views with one.

## Verify it

```
pip install cryptography
python3 verify.py            # every fixing, every revealed hour
python3 verify.py 2026-09-21 # one day
```

`verify.py` checks that each `pulse/marks/<day>.json` hashes to its fixing and
that the signature checks against the published key; that each revealed hour's
bytes hash to the sha256 in that day's commitments and that the signature
checks; and that one key signed all of it. Hours committed to but not yet
revealed are listed, with the time they are due. Anything else is a failure and
the exit code says so.

The key: `2758b1acf4a4c695abbc0a1edd91742cc42ecd6db8a552daf08a23d99b22fad2`
(ed25519, hex; printed in every fixing and every commitment). A rotated key
would be announced here, and the old one would keep verifying the days it
signed.

## Before 2026-09-22

Until 2026-09-22 02:05Z this data lived on the `board-data` branch of
`firming-ai/firming` and the hourly board was published live, lane rows
included; that history came across whole (379 commits) and is not rewritten —
the five days of lane-hour data it holds are already public and stay so. The
delay and the coarsening apply from the evening of 2026-09-22.
