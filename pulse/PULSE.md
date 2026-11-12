# FILL — the inference availability index

*As of 2026-11-11T20:05:13+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-12T20:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-11/20.json`; their sha256 `3159883cbf31…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 90.9** · FILL·FLEX 80.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 51.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=312) | 100.0% (n=30) |
| GEM·FILL | 81.6% | 63.2% (n=19) | 100.0% (n=122) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 91.2% | 90.6% (n=32) | 83.0% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1048 ms |
| bedrock | 100.0% | — | 0.0% | 632 ms |
| deepseek | 100.0% | — | 0.0% | 1268 ms |
| gemini | 100.0% | 66.5% | 9.4% | 1220 ms |
| mistral | 100.0% | — | 0.0% | 808 ms |
| openai | 99.8% | 95.3% | 0.0% | 1058 ms |
| openrouter | 100.0% | — | 0.0% | 1415 ms |
| xai | 100.0% | — | 0.0% | 764 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 312 | 312 | 0 | 0 | 99.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100 s | 3 min |
| gemini | 124 | 124 | 0 | 0 | 99.2% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 97.9% | 100.0% | 100.0% | 100.0% | 50 s | 3 min |
| openai | 312 | 289 | 23 | 0 | 81.3% | 84.1% | 89.3% | 91.0% | 100.0% | 67 s | 213 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
