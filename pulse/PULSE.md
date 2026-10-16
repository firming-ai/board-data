# FILL — the inference availability index

*As of 2026-10-15T05:05:11+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-16T05:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-15/05.json`; their sha256 `9bd9c2883ece…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 67.0** · FILL·FLEX 64.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 4.4% | 0.0% (n=18) | 8.7% (n=92) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 96.7% | 100.0% (n=32) | 90.2% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1059 ms |
| bedrock | 100.0% | — | 0.0% | 703 ms |
| deepseek | 12.9% | — | 0.0% | 1651 ms |
| gemini | 0.0% | 0.0% | 0.5% | — ms |
| mistral | 100.0% | — | 0.0% | 729 ms |
| openai | 100.0% | 99.0% | 0.0% | 1008 ms |
| openrouter | 100.0% | — | 0.0% | 1485 ms |
| xai | 100.0% | — | 0.0% | 784 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 96.6% | 98.5% | 100.0% | 100.0% | 100.0% | 117 s | 4 min |
| gemini | 94 | 6 | 0 | 88 | 6.4% | 6.4% | 6.4% | 16.3% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 95.8% | 97.9% | 100.0% | 100.0% | 100.0% | 22 s | 105 s |
| openai | 264 | 264 | 0 | 0 | 79.9% | 82.2% | 90.5% | 99.2% | 100.0% | 68 s | 154 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
