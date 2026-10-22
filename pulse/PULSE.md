# FILL — the inference availability index

*As of 2026-10-21T02:05:02+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-22T02:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-21/02.json`; their sha256 `91de76606ca8…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 93.9** · FILL·FLEX 90.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.4% | — | 98.9% (n=264) | 100.0% (n=30) |
| GEM·FILL | 88.9% | 77.8% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 77.1% | — | 77.1% (n=48) | — |
| OAI·FILL | 93.4% | 96.9% (n=32) | 83.3% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1133 ms |
| bedrock | 100.0% | — | 0.0% | 754 ms |
| deepseek | 100.0% | — | 0.0% | 1288 ms |
| gemini | 100.0% | 84.0% | 6.8% | 1175 ms |
| mistral | 100.0% | — | 0.0% | 825 ms |
| openai | 100.0% | 97.7% | 0.0% | 1075 ms |
| openrouter | 100.0% | — | 0.0% | 1371 ms |
| xai | 100.0% | — | 0.0% | 840 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 92.0% | 97.0% | 98.9% | 100.0% | 100.0% | 114 s | 7 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 118 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 47.9% | 56.3% | 77.1% | 100.0% | 100.0% | 7 min | 144 min |
| openai | 264 | 260 | 4 | 0 | 72.3% | 75.4% | 83.5% | 95.1% | 100.0% | 68 s | 232 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
