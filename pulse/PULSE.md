# FILL — the inference availability index

*As of 2026-10-03T03:05:01+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-04T03:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-03/03.json`; their sha256 `dc31b734f22b…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 96.6** · FILL·FLEX 93.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=197) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 98.6% | 100.0% (n=32) | 95.9% (n=245) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1161 ms |
| bedrock | 100.0% | — | 0.0% | 751 ms |
| deepseek | 100.0% | — | 0.0% | 1149 ms |
| gemini | 100.0% | 82.5% | 9.6% | 987 ms |
| mistral | 100.0% | — | 0.0% | 694 ms |
| openai | 100.0% | 98.4% | 0.0% | 955 ms |
| openrouter | 100.0% | — | 0.0% | 1438 ms |
| xai | 100.0% | — | 0.0% | 928 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 198 | 198 | 0 | 0 | 97.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 5 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 87.5% | 91.7% | 100.0% | 100.0% | 100.0% | 32 s | 21 min |
| openai | 246 | 246 | 0 | 0 | 83.3% | 88.2% | 95.9% | 99.6% | 90.8% | 64 s | 39 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
