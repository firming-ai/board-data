# FILL — the inference availability index

*As of 2026-10-03T15:05:02+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-04T15:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-03/15.json`; their sha256 `5f42a903206e…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 95.8** · FILL·FLEX 91.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=209) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 99.1% | 100.0% (n=32) | 97.3% (n=257) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1028 ms |
| bedrock | 100.0% | — | 0.0% | 716 ms |
| deepseek | 100.0% | — | 0.0% | 1278 ms |
| gemini | 100.0% | 91.8% | 3.8% | 939 ms |
| mistral | 100.0% | — | 0.0% | 714 ms |
| openai | 99.7% | 100.0% | 0.0% | 1016 ms |
| openrouter | 100.0% | — | 0.0% | 1500 ms |
| xai | 100.0% | — | 0.0% | 978 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 210 | 209 | 1 | 0 | 98.1% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 4 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 47 | 1 | 0 | 83.0% | 89.4% | 100.0% | 100.0% | 100.0% | 72 s | 22 min |
| openai | 258 | 257 | 0 | 1 | 86.4% | 92.2% | 97.3% | 99.6% | 100.0% | 66 s | 14 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
