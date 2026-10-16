# FILL — the inference availability index

*As of 2026-10-15T22:05:13+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-16T22:05:04+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-15/22.json`; their sha256 `248a3f22052c…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 66.7** · FILL·FLEX 64.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.8% | — | 99.6% (n=264) | 100.0% (n=30) |
| GEM·FILL | 3.3% | 5.6% (n=18) | 1.0% (n=96) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 96.9% | 96.9% (n=32) | 93.9% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1154 ms |
| bedrock | 98.4% | — | 1.6% | 734 ms |
| deepseek | 100.0% | — | 0.0% | 1255 ms |
| gemini | 0.0% | 0.0% | 0.0% | — ms |
| mistral | 100.0% | — | 0.0% | 792 ms |
| openai | 100.0% | 99.2% | 0.0% | 1000 ms |
| openrouter | 100.0% | — | 0.0% | 1395 ms |
| xai | 100.0% | — | 0.0% | 892 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 263 | 1 | 0 | 96.6% | 98.1% | 99.6% | 100.0% | 100.0% | 111 s | 4 min |
| gemini | 96 | 1 | 0 | 95 | 0.0% | 0.0% | 1.0% | 1.0% | 25.0% | 35 min | 35 min |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 97.9% | 100.0% | 100.0% | 100.0% | 22 s | 76 s |
| openai | 264 | 261 | 3 | 0 | 87.0% | 89.7% | 95.0% | 98.9% | 100.0% | 68 s | 59 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
