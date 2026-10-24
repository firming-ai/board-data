# FILL — the inference availability index

*As of 2026-10-23T13:05:12+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-10-24T13:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-23/13.json`; their sha256 `28caf003f0cf…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 88.8** · FILL·FLEX 76.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 80.6% | 61.1% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 89.6% | — | 89.6% (n=48) | — |
| OAI·FILL | 85.7% | 84.4% (n=32) | 72.7% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1048 ms |
| bedrock | 100.0% | — | 0.0% | 696 ms |
| deepseek | 100.0% | — | 0.0% | 1216 ms |
| gemini | 100.0% | 64.1% | 7.1% | 1147 ms |
| mistral | 100.0% | — | 0.0% | 954 ms |
| openai | 100.0% | 83.1% | 0.0% | 1058 ms |
| openrouter | 100.0% | — | 0.0% | 1309 ms |
| xai | 100.0% | — | 0.0% | 736 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 96.6% | 99.2% | 100.0% | 100.0% | 100.0% | 108 s | 3 min |
| gemini | 96 | 96 | 0 | 0 | 92.7% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 6 min |
| mistral | 48 | 45 | 3 | 0 | 73.3% | 80.0% | 91.1% | 100.0% | 100.0% | 29 s | 73 min |
| openai | 264 | 236 | 28 | 0 | 71.6% | 74.6% | 81.8% | 83.7% | 99.6% | 67 s | 279 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
