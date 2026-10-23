# FILL — the inference availability index

*As of 2026-10-22T12:05:02+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-23T12:05:11+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-22/12.json`; their sha256 `5c0ebc3fabb2…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 89.0** · FILL·FLEX 72.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 77.8% | 55.6% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 89.1% | 81.2% (n=32) | 86.0% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1040 ms |
| bedrock | 100.0% | — | 0.0% | 726 ms |
| deepseek | 100.0% | — | 0.0% | 1338 ms |
| gemini | 100.0% | 60.2% | 17.7% | 1201 ms |
| mistral | 100.0% | — | 0.0% | 831 ms |
| openai | 100.0% | 89.1% | 0.0% | 1092 ms |
| openrouter | 100.0% | — | 0.0% | 1390 ms |
| xai | 100.0% | — | 0.0% | 816 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 93.9% | 98.5% | 100.0% | 100.0% | 100.0% | 106 s | 6 min |
| gemini | 96 | 96 | 0 | 0 | 97.9% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 93.8% | 93.8% | 97.9% | 100.0% | 100.0% | 22 s | 10 min |
| openai | 264 | 253 | 11 | 0 | 77.5% | 79.8% | 88.5% | 95.8% | 100.0% | 67 s | 170 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
