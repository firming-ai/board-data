# FILL — the inference availability index

*As of 2026-10-01T15:05:13+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-02T15:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-01/15.json`; their sha256 `bd7c5a188203…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 87.6** · FILL·FLEX 87.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 88.5% | — | 77.1% (n=192) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 91.9% | 100.0% (n=32) | 75.8% (n=240) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1817 ms |
| bedrock | 100.0% | — | 0.0% | 692 ms |
| deepseek | 100.0% | — | 0.0% | 1278 ms |
| gemini | 100.0% | 75.3% | 13.7% | 1040 ms |
| mistral | 100.0% | — | 0.0% | 788 ms |
| openai | 99.0% | 98.4% | 0.0% | 1241 ms |
| openrouter | 100.0% | — | 0.0% | 1681 ms |
| xai | 98.7% | — | 0.0% | 943 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 184 | 8 | 0 | — | — | 80.4% | 8 min | 73 min |
| gemini | 48 | 48 | 0 | 0 | — | — | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | — | — | 100.0% | 22 s | 12 min |
| openai | 240 | 193 | 1 | 46 | — | — | 77.0% | 70 s | 38 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
