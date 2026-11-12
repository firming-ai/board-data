# FILL — the inference availability index

*As of 2026-11-11T16:05:14+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-12T16:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-11/16.json`; their sha256 `0c6334be4971…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 90.4** · FILL·FLEX 76.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 51.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=312) | 100.0% (n=30) |
| GEM·FILL | 81.6% | 63.2% (n=19) | 100.0% (n=114) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 89.7% | 84.4% (n=32) | 84.6% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1053 ms |
| bedrock | 100.0% | — | 0.0% | 625 ms |
| deepseek | 100.0% | — | 0.0% | 1314 ms |
| gemini | 100.0% | 58.3% | 12.8% | 1173 ms |
| mistral | 100.0% | — | 0.0% | 843 ms |
| openai | 99.5% | 81.8% | 0.0% | 1110 ms |
| openrouter | 100.0% | — | 0.0% | 1438 ms |
| xai | 100.0% | — | 0.0% | 807 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 312 | 312 | 0 | 0 | 98.4% | 100.0% | 100.0% | 100.0% | 100.0% | 98 s | 3 min |
| gemini | 116 | 116 | 0 | 0 | 99.1% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 97.9% | 100.0% | 100.0% | 100.0% | 50 s | 3 min |
| openai | 312 | 289 | 23 | 0 | 83.4% | 86.2% | 90.3% | 93.9% | 100.0% | 67 s | 211 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
