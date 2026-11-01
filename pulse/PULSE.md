# FILL — the inference availability index

*As of 2026-10-31T21:05:13+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-01T21:05:06+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-31/21.json`; their sha256 `4f135a35a905…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 96.2** · FILL·FLEX 94.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 94.4% | 88.9% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 81.3% | — | 81.2% (n=48) | — |
| OAI·FILL | 94.2% | 96.9% (n=32) | 85.6% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1309 ms |
| bedrock | 98.4% | — | 1.6% | 609 ms |
| deepseek | 100.0% | — | 0.0% | 1322 ms |
| gemini | 100.0% | 78.6% | 4.9% | 1283 ms |
| mistral | 100.0% | — | 0.0% | 781 ms |
| openai | 99.8% | 97.9% | 0.0% | 1033 ms |
| openrouter | 100.0% | — | 0.0% | 1317 ms |
| xai | 100.0% | — | 0.0% | 808 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 99.6% | 100.0% | 100.0% | 100.0% | 100.0% | 92 s | 2 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 54.2% | 54.2% | 85.4% | 95.8% | 100.0% | 3 min | 138 min |
| openai | 312 | 304 | 8 | 0 | 79.3% | 82.2% | 88.2% | 95.2% | 100.0% | 66 s | 176 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
