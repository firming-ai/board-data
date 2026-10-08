# FILL — the inference availability index

*As of 2026-10-07T10:05:05+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-08T10:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-07/10.json`; their sha256 `6560b7c49627…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 95.3** · FILL·FLEX 87.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.5% | — | 99.1% (n=216) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 92.4% | 87.5% (n=32) | 89.8% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 99.5% | — | 0.5% | 951 ms |
| bedrock | 100.0% | — | 0.0% | 710 ms |
| deepseek | 100.0% | — | 0.0% | 1278 ms |
| gemini | 100.0% | 62.4% | 20.6% | 1003 ms |
| mistral | 100.0% | — | 0.0% | 777 ms |
| openai | 99.7% | 90.6% | 0.0% | 984 ms |
| openrouter | 100.0% | — | 0.0% | 1651 ms |
| xai | 0.0% | — | 0.0% | — ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 216 | 215 | 1 | 0 | 88.8% | 96.3% | 99.1% | 100.0% | 100.0% | 2 min | 9 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 22 s | 114 s |
| openai | 264 | 256 | 7 | 1 | 81.7% | 86.0% | 91.4% | 98.1% | 100.0% | 67 s | 79 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
