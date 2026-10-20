# FILL — the inference availability index

*As of 2026-10-19T19:05:03+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-20T19:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-19/19.json`; their sha256 `5dcaa885b168…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 92.5** · FILL·FLEX 80.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.6% | — | 99.2% (n=264) | 100.0% (n=30) |
| GEM·FILL | 83.3% | 66.7% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 77.1% | — | 77.1% (n=48) | — |
| OAI·FILL | 94.6% | 87.5% (n=32) | 96.2% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1299 ms |
| bedrock | 98.4% | — | 1.6% | 784 ms |
| deepseek | 100.0% | — | 0.0% | 1304 ms |
| gemini | 99.4% | 63.1% | 14.4% | 1341 ms |
| mistral | 100.0% | — | 0.0% | 921 ms |
| openai | 100.0% | 88.8% | 0.0% | 1232 ms |
| openrouter | 100.0% | — | 0.0% | 1602 ms |
| xai | 100.0% | — | 0.0% | 943 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 263 | 1 | 0 | 91.6% | 97.0% | 99.2% | 100.0% | 100.0% | 2 min | 9 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 27.1% | 37.5% | 77.1% | 100.0% | 100.0% | 30 min | 126 min |
| openai | 264 | 260 | 4 | 0 | 88.5% | 91.2% | 97.3% | 98.9% | 100.0% | 40 s | 35 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
