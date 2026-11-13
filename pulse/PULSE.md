# FILL — the inference availability index

*As of 2026-11-12T06:05:13+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-13T06:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-12/06.json`; their sha256 `77300d83fff1…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 92.7** · FILL·FLEX 88.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 51.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=312) | 100.0% (n=30) |
| GEM·FILL | 84.2% | 68.4% (n=19) | 100.0% (n=142) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 94.0% | 100.0% (n=32) | 82.0% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 956 ms |
| bedrock | 100.0% | — | 0.0% | 609 ms |
| deepseek | 100.0% | — | 0.0% | 1306 ms |
| gemini | 100.0% | 61.0% | 10.7% | 1260 ms |
| mistral | 100.0% | — | 0.0% | 764 ms |
| openai | 98.8% | 99.5% | 0.0% | 992 ms |
| openrouter | 100.0% | — | 0.0% | 1327 ms |
| xai | 100.0% | — | 0.0% | 780 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 312 | 312 | 0 | 0 | 99.7% | 100.0% | 100.0% | 100.0% | 100.0% | 94 s | 3 min |
| gemini | 144 | 144 | 0 | 0 | 99.3% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 95.8% | 95.8% | 100.0% | 100.0% | 100.0% | 45 s | 4 min |
| openai | 312 | 290 | 22 | 0 | 78.3% | 82.1% | 87.9% | 87.8% | 100.0% | 68 s | 607 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
