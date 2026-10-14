# FILL — the inference availability index

*As of 2026-10-13T03:05:02+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-14T03:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-13/03.json`; their sha256 `a76f3d592a17…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 94.1** · FILL·FLEX 89.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 85.3% | 70.6% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 97.0% | 100.0% (n=32) | 90.9% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1098 ms |
| bedrock | 100.0% | — | 0.0% | 734 ms |
| deepseek | 100.0% | — | 0.0% | 1238 ms |
| gemini | 100.0% | 89.7% | 4.7% | 1102 ms |
| mistral | 100.0% | — | 0.0% | 761 ms |
| openai | 99.5% | 98.7% | 0.0% | 1031 ms |
| openrouter | 100.0% | — | 0.0% | 1485 ms |
| xai | 100.0% | — | 0.0% | 783 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 97.0% | 99.2% | 100.0% | 100.0% | 100.0% | 96 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 75.0% | 95.8% | 100.0% | 100.0% | 100.0% | 2 min | 10 min |
| openai | 264 | 264 | 0 | 0 | 79.5% | 85.2% | 90.9% | 97.7% | 100.0% | 68 s | 127 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
