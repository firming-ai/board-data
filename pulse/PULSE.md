# FILL — the inference availability index

*As of 2026-11-10T12:05:12+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-11T12:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-10/12.json`; their sha256 `06d32fef7ae7…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 92.9** · FILL·FLEX 88.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=274) | 100.0% (n=30) |
| GEM·FILL | 82.8% | 66.7% (n=18) | 99.0% (n=96) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 95.8% | 100.0% (n=32) | 87.5% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1187 ms |
| bedrock | 100.0% | — | 0.0% | 612 ms |
| deepseek | 100.0% | — | 0.0% | 1335 ms |
| gemini | 99.4% | 59.7% | 14.4% | 1322 ms |
| mistral | 100.0% | — | 0.0% | 917 ms |
| openai | 99.8% | 94.5% | 0.0% | 1075 ms |
| openrouter | 100.0% | — | 0.0% | 1464 ms |
| xai | 100.0% | — | 0.0% | 805 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 276 | 276 | 0 | 0 | 98.6% | 99.6% | 100.0% | 100.0% | 100.0% | 96 s | 3 min |
| gemini | 96 | 96 | 0 | 0 | 88.5% | 91.7% | 99.0% | 100.0% | 100.0% | 2 min | 14 min |
| mistral | 48 | 48 | 0 | 0 | 87.5% | 89.6% | 100.0% | 100.0% | 100.0% | 51 s | 19 min |
| openai | 312 | 312 | 0 | 0 | 79.8% | 83.0% | 88.1% | 90.7% | 100.0% | 66 s | 428 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
