# FILL — the inference availability index

*As of 2026-11-06T22:05:02+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-07T22:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-06/22.json`; their sha256 `651bb5f5f991…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 92.3** · FILL·FLEX 86.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 80.6% | 61.1% (n=18) | 100.0% (n=94) | — |
| MIS·FILL | 47.9% | — | 47.9% (n=48) | — |
| OAI·FILL | 96.4% | 100.0% (n=32) | 89.1% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1429 ms |
| bedrock | 96.9% | — | 3.1% | 668 ms |
| deepseek | 100.0% | — | 0.0% | 1368 ms |
| gemini | 100.0% | 65.0% | 12.0% | 1122 ms |
| mistral | 100.0% | — | 0.0% | 841 ms |
| openai | 100.0% | 99.5% | 0.0% | 1101 ms |
| openrouter | 100.0% | — | 0.0% | 1412 ms |
| xai | 100.0% | — | 0.0% | 833 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 96.6% | 99.6% | 100.0% | 100.0% | 100.0% | 98 s | 3 min |
| gemini | 96 | 94 | 0 | 2 | 98.9% | 98.9% | 97.9% | 97.9% | 100.0% | 2 min | 4 min |
| mistral | 48 | 39 | 9 | 0 | 53.8% | 53.8% | 53.8% | 60.4% | 100.0% | 64 s | 608 min |
| openai | 312 | 307 | 5 | 0 | 81.4% | 85.0% | 90.6% | 93.9% | 100.0% | 67 s | 219 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
