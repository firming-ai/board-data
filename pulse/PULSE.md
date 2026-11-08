# FILL — the inference availability index

*As of 2026-11-07T08:05:03+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-08T08:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-07/08.json`; their sha256 `a0f5c153bc99…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.2** · FILL·FLEX 84.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 77.8% | 55.6% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 47.9% | — | 47.9% (n=48) | — |
| OAI·FILL | 95.8% | 100.0% (n=32) | 87.5% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1250 ms |
| bedrock | 100.0% | — | 0.0% | 623 ms |
| deepseek | 32.6% | — | 4.5% | 1810 ms |
| gemini | 100.0% | 59.7% | 10.3% | 1265 ms |
| mistral | 100.0% | — | 0.0% | 796 ms |
| openai | 100.0% | 96.3% | 0.0% | 936 ms |
| openrouter | 100.0% | — | 0.0% | 1447 ms |
| xai | 100.0% | — | 0.0% | 952 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 97.3% | 98.1% | 100.0% | 100.0% | 100.0% | 91 s | 3 min |
| gemini | 96 | 95 | 1 | 0 | 98.9% | 98.9% | 100.0% | 100.0% | 97.9% | 2 min | 4 min |
| mistral | 48 | 48 | 0 | 0 | 43.8% | 43.8% | 47.9% | 60.4% | 100.0% | 87 min | 595 min |
| openai | 312 | 304 | 8 | 0 | 80.9% | 84.2% | 89.8% | 93.9% | 100.0% | 66 s | 243 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
