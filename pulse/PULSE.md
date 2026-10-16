# FILL — the inference availability index

*As of 2026-10-15T14:05:12+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-16T14:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-15/14.json`; their sha256 `72f127ba2aac…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 64.3** · FILL·FLEX 54.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 0.5% | 0.0% (n=18) | 1.0% (n=96) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 92.4% | 84.4% (n=32) | 92.8% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1091 ms |
| bedrock | 100.0% | — | 0.0% | 681 ms |
| deepseek | 100.0% | — | 0.0% | 1161 ms |
| gemini | 0.0% | 0.5% | 0.0% | — ms |
| mistral | 100.0% | — | 0.0% | 760 ms |
| openai | 100.0% | 81.0% | 0.0% | 1008 ms |
| openrouter | 100.0% | — | 0.0% | 1485 ms |
| xai | 100.0% | — | 0.0% | 758 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 97.0% | 98.5% | 100.0% | 100.0% | 100.0% | 116 s | 4 min |
| gemini | 96 | 1 | 0 | 95 | 0.0% | 0.0% | 1.0% | 0.0% | 56.3% | 35 min | 35 min |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 97.9% | 100.0% | 100.0% | 100.0% | 22 s | 105 s |
| openai | 264 | 261 | 3 | 0 | 86.2% | 88.9% | 94.3% | 99.2% | 100.0% | 68 s | 69 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
