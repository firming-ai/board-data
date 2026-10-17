# FILL — the inference availability index

*As of 2026-10-16T15:05:03+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-17T15:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-16/15.json`; their sha256 `9584a2bc225d…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 85.4** · FILL·FLEX 82.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.6% | — | 99.2% (n=264) | 100.0% (n=30) |
| GEM·FILL | 58.3% | 50.0% (n=18) | 66.7% (n=96) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 98.4% | 100.0% (n=32) | 95.1% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1213 ms |
| bedrock | 100.0% | — | 0.0% | 726 ms |
| deepseek | 100.0% | — | 0.0% | 1280 ms |
| gemini | 100.0% | 50.0% | 27.7% | 1286 ms |
| mistral | 100.0% | — | 0.0% | 999 ms |
| openai | 99.7% | 98.2% | 0.0% | 1025 ms |
| openrouter | 100.0% | — | 0.0% | 1533 ms |
| xai | 98.7% | — | 0.0% | 855 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 93.2% | 95.8% | 99.2% | 100.0% | 100.0% | 112 s | 8 min |
| gemini | 96 | 68 | 0 | 28 | 70.8% | 70.8% | 70.8% | 54.2% | 1.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 97.9% | 100.0% | 100.0% | 100.0% | 21 s | 46 s |
| openai | 264 | 261 | 3 | 0 | 83.5% | 88.9% | 95.8% | 98.9% | 100.0% | 67 s | 44 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
