# FILL — the inference availability index

*As of 2026-10-11T23:05:01+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-12T23:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-11/23.json`; their sha256 `2a6ac4698c53…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 92.5** · FILL·FLEX 87.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 95.2% | 100.0% (n=32) | 85.6% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 970 ms |
| bedrock | 100.0% | — | 0.0% | 699 ms |
| deepseek | 100.0% | — | 0.0% | 1199 ms |
| gemini | 100.0% | 70.6% | 15.7% | 951 ms |
| mistral | 100.0% | — | 0.0% | 683 ms |
| openai | 99.7% | 100.0% | 0.0% | 938 ms |
| openrouter | 100.0% | — | 0.0% | 1365 ms |
| xai | 43.4% | — | 0.0% | 746 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 93 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 91.7% | 100.0% | 100.0% | 100.0% | 100.0% | 42 s | 6 min |
| openai | 264 | 264 | 0 | 0 | 76.5% | 80.7% | 86.4% | 92.4% | 100.0% | 67 s | 264 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
