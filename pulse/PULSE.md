# FILL — the inference availability index

*As of 2026-11-13T14:05:13+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-14T14:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-13/14.json`; their sha256 `22edd1cf00d9…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 87.3** · FILL·FLEX 72.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 51.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 96.6% | — | 100.0% (n=312) | 93.1% (n=29) |
| GEM·FILL | 76.3% | 52.6% (n=19) | 100.0% (n=158) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 89.1% | 84.4% (n=32) | 83.0% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 98.2% | — | 1.8% | 1421 ms |
| bedrock | 100.0% | — | 0.0% | 632 ms |
| deepseek | 100.0% | — | 0.0% | 1220 ms |
| gemini | 100.0% | 56.4% | 14.4% | 1220 ms |
| mistral | 50.0% | — | 0.0% | 761 ms |
| openai | 99.8% | 93.2% | 0.0% | 1153 ms |
| openrouter | 100.0% | — | 0.0% | 1395 ms |
| xai | 100.0% | — | 0.0% | 783 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 312 | 312 | 0 | 0 | 99.7% | 100.0% | 100.0% | 100.0% | 100.0% | 95 s | 2 min |
| gemini | 160 | 160 | 0 | 0 | 97.5% | 98.8% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 95.8% | 95.8% | 100.0% | 100.0% | 100.0% | 23 s | 93 s |
| openai | 312 | 293 | 19 | 0 | 83.6% | 85.7% | 88.7% | 84.6% | 100.0% | 66 s | 630 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
