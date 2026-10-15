# FILL — the inference availability index

*As of 2026-10-14T07:05:13+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-15T07:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-14/07.json`; their sha256 `7b06c2eb2a3b…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 80.5** · FILL·FLEX 60.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 50.0% | 0.0% (n=18) | 100.0% (n=48) | — |
| MIS·FILL | 93.8% | — | 93.8% (n=48) | — |
| OAI·FILL | 91.6% | 93.8% (n=32) | 81.1% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1390 ms |
| bedrock | 98.4% | — | 1.6% | 736 ms |
| deepseek | 100.0% | — | 0.0% | 1407 ms |
| gemini | 79.8% | 41.6% | 14.7% | 1154 ms |
| mistral | 100.0% | — | 0.0% | 778 ms |
| openai | 100.0% | 98.7% | 0.0% | 1110 ms |
| openrouter | 100.0% | — | 0.0% | 1512 ms |
| xai | 100.0% | — | 0.0% | 884 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 97.0% | 98.9% | 100.0% | 100.0% | 100.0% | 108 s | 3 min |
| gemini | 50 | 48 | 0 | 2 | 96.0% | 96.0% | 96.0% | 100.0% | 100.0% | 108 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 75.0% | 85.4% | 93.8% | 100.0% | 100.0% | 72 s | 66 min |
| openai | 264 | 261 | 3 | 0 | 69.0% | 71.6% | 81.6% | 92.4% | 100.0% | 72 s | 309 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
