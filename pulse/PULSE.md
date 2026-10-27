# FILL — the inference availability index

*As of 2026-10-26T14:05:13+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-10-27T14:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-26/14.json`; their sha256 `b3ea784eb1e6…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 86.2** · FILL·FLEX 72.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 75.0% | 50.0% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 83.7% | 84.4% (n=32) | 66.7% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1115 ms |
| bedrock | 95.3% | — | 4.7% | 720 ms |
| deepseek | 100.0% | — | 0.0% | 1291 ms |
| gemini | 100.0% | 53.4% | 17.1% | 1273 ms |
| mistral | 100.0% | — | 0.0% | 893 ms |
| openai | 99.7% | 84.4% | 0.0% | 1261 ms |
| openrouter | 100.0% | — | 0.0% | 1503 ms |
| xai | 100.0% | — | 0.0% | 797 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 263 | 1 | 0 | 97.7% | 98.9% | 100.0% | 100.0% | 100.0% | 102 s | 3 min |
| gemini | 96 | 95 | 1 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 118 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 21 s | 27 s |
| openai | 264 | 185 | 30 | 49 | 65.4% | 67.9% | 75.6% | 70.8% | 76.5% | 68 s | 42 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
