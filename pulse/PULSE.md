# FILL — the inference availability index

*As of 2026-11-04T20:05:03+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-05T20:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-04/20.json`; their sha256 `0b874128097e…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.8** · FILL·FLEX 86.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 80.6% | 61.1% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 94.8% | 100.0% (n=32) | 84.3% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1338 ms |
| bedrock | 100.0% | — | 0.0% | 710 ms |
| deepseek | 100.0% | — | 0.0% | 1346 ms |
| gemini | 100.0% | 62.1% | 17.7% | 1312 ms |
| mistral | 100.0% | — | 0.0% | 947 ms |
| openai | 99.5% | 88.0% | 0.0% | 1212 ms |
| openrouter | 100.0% | — | 0.0% | 1432 ms |
| xai | 100.0% | — | 0.0% | 852 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 97.0% | 99.2% | 100.0% | 100.0% | 100.0% | 107 s | 3 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 85.4% | 97.9% | 100.0% | 100.0% | 100.0% | 58 s | 9 min |
| openai | 312 | 297 | 15 | 0 | 79.8% | 81.1% | 88.6% | 93.9% | 100.0% | 66 s | 179 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
