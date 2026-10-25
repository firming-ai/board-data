# FILL — the inference availability index

*As of 2026-10-24T21:05:13+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-10-25T21:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-24/21.json`; their sha256 `47f34ec80a0b…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 96.7** · FILL·FLEX 98.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 97.2% | 94.4% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 92.9% | 100.0% (n=32) | 78.8% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 939 ms |
| bedrock | 100.0% | — | 0.0% | 681 ms |
| deepseek | 100.0% | — | 0.0% | 1245 ms |
| gemini | 100.0% | 85.0% | 1.6% | 1129 ms |
| mistral | 100.0% | — | 0.0% | 788 ms |
| openai | 99.7% | 100.0% | 0.0% | 969 ms |
| openrouter | 100.0% | — | 0.0% | 1309 ms |
| xai | 100.0% | — | 0.0% | 720 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 95.5% | 97.7% | 100.0% | 100.0% | 100.0% | 109 s | 4 min |
| gemini | 96 | 96 | 0 | 0 | 97.9% | 99.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 89.6% | 93.8% | 100.0% | 100.0% | 100.0% | 22 s | 14 min |
| openai | 264 | 238 | 4 | 22 | 74.2% | 75.4% | 79.2% | 87.1% | 100.0% | 67 s | 275 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
