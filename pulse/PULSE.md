# FILL — the inference availability index

*As of 2026-10-16T07:05:13+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-17T07:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-16/07.json`; their sha256 `3076399d7aa9…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 79.1** · FILL·FLEX 80.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.8% | — | 99.6% (n=264) | 100.0% (n=30) |
| GEM·FILL | 39.4% | 44.4% (n=18) | 34.4% (n=96) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 98.1% | 100.0% (n=32) | 94.3% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1100 ms |
| bedrock | 98.4% | — | 1.6% | 710 ms |
| deepseek | 100.0% | — | 0.0% | 1278 ms |
| gemini | 100.0% | 56.3% | 24.2% | 1166 ms |
| mistral | 100.0% | — | 0.0% | 729 ms |
| openai | 100.0% | 99.7% | 0.0% | 967 ms |
| openrouter | 100.0% | — | 0.0% | 1441 ms |
| xai | 100.0% | — | 0.0% | 807 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 262 | 2 | 0 | 96.6% | 98.5% | 99.6% | 100.0% | 100.0% | 108 s | 4 min |
| gemini | 96 | 37 | 0 | 59 | 37.5% | 37.5% | 38.5% | 21.9% | 2.1% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 97.9% | 100.0% | 100.0% | 100.0% | 22 s | 65 s |
| openai | 264 | 264 | 0 | 0 | 85.2% | 89.8% | 94.3% | 98.9% | 100.0% | 68 s | 69 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
