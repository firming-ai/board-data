# FILL — the inference availability index

*As of 2026-10-31T16:05:13+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-01T16:05:06+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-31/16.json`; their sha256 `ae12e61e42c6…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 92.4** · FILL·FLEX 86.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 83.3% | 66.7% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 81.3% | — | 81.2% (n=48) | — |
| OAI·FILL | 94.0% | 96.9% (n=32) | 85.3% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1371 ms |
| bedrock | 100.0% | — | 0.0% | 606 ms |
| deepseek | 100.0% | — | 0.0% | 1354 ms |
| gemini | 100.0% | 63.1% | 12.0% | 1248 ms |
| mistral | 100.0% | — | 0.0% | 777 ms |
| openai | 99.5% | 99.2% | 0.0% | 1006 ms |
| openrouter | 100.0% | — | 0.0% | 1296 ms |
| xai | 100.0% | — | 0.0% | 781 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 99.6% | 100.0% | 100.0% | 100.0% | 100.0% | 87 s | 2 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 47 | 1 | 0 | 57.4% | 59.6% | 80.9% | 95.8% | 100.0% | 68 s | 230 min |
| openai | 312 | 310 | 2 | 0 | 76.5% | 79.4% | 86.1% | 92.6% | 100.0% | 66 s | 243 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
