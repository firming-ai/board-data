# FILL — the inference availability index

*As of 2026-10-14T13:05:13+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-15T13:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-14/13.json`; their sha256 `aa129149ad61…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 73.4** · FILL·FLEX 50.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 33.3% | 0.0% (n=18) | 66.7% (n=60) | — |
| MIS·FILL | 95.8% | — | 95.8% (n=48) | — |
| OAI·FILL | 87.0% | 78.1% (n=32) | 83.0% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1368 ms |
| bedrock | 100.0% | — | 0.0% | 731 ms |
| deepseek | 100.0% | — | 0.0% | 1278 ms |
| gemini | 0.0% | 0.0% | 0.0% | — ms |
| mistral | 100.0% | — | 0.0% | 870 ms |
| openai | 99.7% | 91.2% | 0.0% | 1084 ms |
| openrouter | 100.0% | — | 0.0% | 1599 ms |
| xai | 100.0% | — | 0.0% | 799 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 97.0% | 98.9% | 100.0% | 100.0% | 100.0% | 108 s | 3 min |
| gemini | 62 | 38 | 0 | 24 | 61.3% | 61.3% | 61.3% | 85.2% | 100.0% | 107 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 87.5% | 95.8% | 100.0% | 100.0% | 28 s | 38 min |
| openai | 264 | 259 | 5 | 0 | 71.4% | 74.1% | 84.2% | 93.2% | 100.0% | 69 s | 269 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
