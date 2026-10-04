# FILL — the inference availability index

*As of 2026-10-03T21:05:01+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-04T21:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-03/21.json`; their sha256 `929e29069180…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 94.3** · FILL·FLEX 85.7

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.8% | — | 99.5% (n=215) | 100.0% (n=30) |
| GEM·FILL | 85.3% | 70.6% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 97.7% | 93.8% (n=32) | 99.2% (n=263) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1057 ms |
| bedrock | 100.0% | — | 0.0% | 710 ms |
| deepseek | 100.0% | — | 0.0% | 1187 ms |
| gemini | 100.0% | 81.4% | 9.3% | 924 ms |
| mistral | 100.0% | — | 0.0% | 706 ms |
| openai | 99.5% | 96.1% | 0.0% | 1008 ms |
| openrouter | 100.0% | — | 0.0% | 1401 ms |
| xai | 100.0% | — | 0.0% | 993 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 216 | 216 | 0 | 0 | 98.6% | 99.5% | 99.5% | 100.0% | 100.0% | 108 s | 4 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 87.5% | 95.8% | 100.0% | 100.0% | 100.0% | 43 s | 7 min |
| openai | 264 | 260 | 3 | 1 | 89.7% | 95.4% | 99.6% | 99.2% | 100.0% | 66 s | 8 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
