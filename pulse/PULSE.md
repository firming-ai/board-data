# FILL — the inference availability index

*As of 2026-11-05T22:05:03+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-06T22:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-05/22.json`; their sha256 `3ea52a4d96f9…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 92.0** · FILL·FLEX 82.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 83.3% | 66.7% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 92.7% | 90.6% (n=32) | 87.5% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1577 ms |
| bedrock | 100.0% | — | 0.0% | 713 ms |
| deepseek | 100.0% | — | 0.0% | 1418 ms |
| gemini | 100.0% | 65.0% | 13.9% | 1258 ms |
| mistral | 100.0% | — | 0.0% | 890 ms |
| openai | 99.5% | 97.4% | 0.0% | 1126 ms |
| openrouter | 100.0% | — | 0.0% | 1509 ms |
| xai | 100.0% | — | 0.0% | 904 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 98.1% | 99.6% | 100.0% | 100.0% | 100.0% | 100 s | 3 min |
| gemini | 96 | 96 | 0 | 0 | 99.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 87.5% | 89.6% | 100.0% | 100.0% | 100.0% | 52 s | 22 min |
| openai | 312 | 300 | 12 | 0 | 80.7% | 84.3% | 91.3% | 90.1% | 100.0% | 66 s | 273 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
