# FILL — the inference availability index

*As of 2026-10-24T11:05:13+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-10-25T11:05:07+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-24/11.json`; their sha256 `c293dcd661c8…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 90.9** · FILL·FLEX 86.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 80.6% | 61.1% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 91.7% | — | 91.7% (n=48) | — |
| OAI·FILL | 92.2% | 100.0% (n=32) | 76.5% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 901 ms |
| bedrock | 100.0% | — | 0.0% | 679 ms |
| deepseek | 100.0% | — | 0.0% | 1250 ms |
| gemini | 100.0% | 66.0% | 9.0% | 1129 ms |
| mistral | 100.0% | — | 0.0% | 729 ms |
| openai | 100.0% | 97.9% | 0.0% | 940 ms |
| openrouter | 100.0% | — | 0.0% | 1432 ms |
| xai | 100.0% | — | 0.0% | 677 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 95.1% | 97.7% | 100.0% | 100.0% | 100.0% | 96 s | 4 min |
| gemini | 96 | 96 | 0 | 0 | 89.6% | 99.0% | 100.0% | 100.0% | 100.0% | 2 min | 7 min |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 87.5% | 95.8% | 100.0% | 100.0% | 22 s | 42 min |
| openai | 264 | 256 | 8 | 0 | 75.8% | 76.6% | 79.7% | 81.1% | 100.0% | 70 s | 360 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
