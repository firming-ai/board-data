# FILL — the inference availability index

*As of 2026-11-06T15:05:03+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-07T15:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-06/15.json`; their sha256 `6b2bf7a435c5…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.4** · FILL·FLEX 84.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 77.8% | 55.6% (n=18) | 100.0% (n=94) | — |
| MIS·FILL | 77.1% | — | 77.1% (n=48) | — |
| OAI·FILL | 96.4% | 100.0% (n=32) | 89.1% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1473 ms |
| bedrock | 100.0% | — | 0.0% | 685 ms |
| deepseek | 100.0% | — | 0.0% | 1418 ms |
| gemini | 98.2% | 58.2% | 14.9% | 1393 ms |
| mistral | 100.0% | — | 0.0% | 1048 ms |
| openai | 100.0% | 96.6% | 0.0% | 1128 ms |
| openrouter | 100.0% | — | 0.0% | 1470 ms |
| xai | 100.0% | — | 0.0% | 913 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 96.2% | 100.0% | 100.0% | 100.0% | 100.0% | 100 s | 3 min |
| gemini | 96 | 94 | 0 | 2 | 100.0% | 100.0% | 97.9% | 97.9% | 100.0% | 2 min | 3 min |
| mistral | 48 | 37 | 11 | 0 | 94.6% | 94.6% | 94.6% | 89.6% | 100.0% | 50 s | 50 min |
| openai | 312 | 304 | 8 | 0 | 83.2% | 86.2% | 91.1% | 92.0% | 100.0% | 66 s | 256 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
