# FILL — the inference availability index

*As of 2026-10-13T16:05:02+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-14T16:05:11+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-13/16.json`; their sha256 `8388a19a7e9b…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 85.1** · FILL·FLEX 59.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 70.6% | 41.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 93.8% | — | 93.8% (n=48) | — |
| OAI·FILL | 84.7% | 68.8% (n=32) | 85.2% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1393 ms |
| bedrock | 100.0% | — | 0.0% | 729 ms |
| deepseek | 100.0% | — | 0.0% | 1299 ms |
| gemini | 100.0% | 32.5% | 30.2% | 1376 ms |
| mistral | 100.0% | — | 0.0% | 862 ms |
| openai | 99.5% | 83.1% | 0.0% | 1155 ms |
| openrouter | 100.0% | — | 0.0% | 1539 ms |
| xai | 100.0% | — | 0.0% | 812 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 263 | 1 | 0 | 98.5% | 99.6% | 100.0% | 100.0% | 100.0% | 102 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 118 s | 3 min |
| mistral | 48 | 44 | 4 | 0 | 54.5% | 88.6% | 97.7% | 100.0% | 100.0% | 4 min | 18 min |
| openai | 264 | 252 | 12 | 0 | 77.0% | 80.2% | 88.5% | 95.8% | 100.0% | 68 s | 158 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
