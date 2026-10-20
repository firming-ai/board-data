# FILL — the inference availability index

*As of 2026-10-19T13:05:03+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-20T13:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-19/13.json`; their sha256 `5d149a1415a7…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 98.7** · FILL·FLEX 98.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.8% | — | 99.6% (n=264) | 100.0% (n=30) |
| GEM·FILL | 97.2% | 94.4% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 72.9% | — | 72.9% (n=48) | — |
| OAI·FILL | 99.0% | 100.0% (n=32) | 97.0% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1206 ms |
| bedrock | 93.8% | — | 6.2% | 789 ms |
| deepseek | 100.0% | — | 0.0% | 1333 ms |
| gemini | 99.4% | 97.6% | 1.1% | 1223 ms |
| mistral | 100.0% | — | 0.0% | 930 ms |
| openai | 100.0% | 97.7% | 0.0% | 1101 ms |
| openrouter | 100.0% | — | 0.0% | 1536 ms |
| xai | 100.0% | — | 0.0% | 922 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 261 | 3 | 0 | 92.3% | 98.1% | 100.0% | 100.0% | 100.0% | 2 min | 8 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 27.1% | 37.5% | 75.0% | 100.0% | 100.0% | 24 min | 135 min |
| openai | 264 | 264 | 0 | 0 | 87.1% | 90.2% | 97.7% | 99.6% | 100.0% | 50 s | 35 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
