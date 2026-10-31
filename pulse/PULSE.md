# FILL — the inference availability index

*As of 2026-10-30T20:05:13+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-10-31T20:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-30/20.json`; their sha256 `5df176bcd6f2…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 92.5** · FILL·FLEX 84.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 86.1% | 72.2% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 91.3% | 90.6% (n=32) | 83.3% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1268 ms |
| bedrock | 93.8% | — | 6.2% | 679 ms |
| deepseek | 100.0% | — | 0.0% | 1382 ms |
| gemini | 100.0% | 68.0% | 6.2% | 1204 ms |
| mistral | 100.0% | — | 0.0% | 888 ms |
| openai | 99.5% | 94.0% | 0.0% | 1155 ms |
| openrouter | 100.0% | — | 0.0% | 1362 ms |
| xai | 100.0% | — | 0.0% | 853 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 98 s | 2 min |
| gemini | 96 | 96 | 0 | 0 | 99.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 47 | 1 | 0 | 91.5% | 93.6% | 97.9% | 100.0% | 100.0% | 27 s | 12 min |
| openai | 312 | 298 | 14 | 0 | 77.9% | 82.6% | 86.9% | 94.6% | 100.0% | 67 s | 181 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
