# FILL — the inference availability index

*As of 2026-11-13T11:05:12+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-14T11:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-13/11.json`; their sha256 `750981c5dfed…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 86.1** · FILL·FLEX 76.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 51.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 92.9% | — | 100.0% (n=312) | 85.7% (n=28) |
| GEM·FILL | 73.7% | 47.4% (n=19) | 100.0% (n=152) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 91.8% | 93.8% (n=32) | 81.7% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 92.4% | — | 7.6% | 1371 ms |
| bedrock | 100.0% | — | 0.0% | 630 ms |
| deepseek | 100.0% | — | 0.0% | 1268 ms |
| gemini | 100.0% | 58.3% | 12.6% | 1218 ms |
| mistral | 50.0% | — | 0.0% | 737 ms |
| openai | 99.3% | 99.2% | 0.0% | 1077 ms |
| openrouter | 100.0% | — | 0.0% | 1306 ms |
| xai | 100.0% | — | 0.0% | 736 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 312 | 312 | 0 | 0 | 99.7% | 100.0% | 100.0% | 100.0% | 100.0% | 94 s | 2 min |
| gemini | 154 | 154 | 0 | 0 | 96.8% | 98.1% | 100.0% | 100.0% | 100.0% | 2 min | 4 min |
| mistral | 48 | 48 | 0 | 0 | 95.8% | 95.8% | 100.0% | 100.0% | 100.0% | 23 s | 93 s |
| openai | 312 | 289 | 23 | 0 | 82.4% | 84.1% | 88.2% | 85.3% | 100.0% | 67 s | 641 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
