# FILL — the inference availability index

*As of 2026-10-21T09:05:02+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-22T09:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-21/09.json`; their sha256 `a902198fcd0b…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 90.2** · FILL·FLEX 78.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.6% | — | 99.2% (n=264) | 100.0% (n=30) |
| GEM·FILL | 80.6% | 61.1% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 93.8% | — | 93.8% (n=48) | — |
| OAI·FILL | 90.4% | 87.5% (n=32) | 83.7% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1129 ms |
| bedrock | 100.0% | — | 0.0% | 731 ms |
| deepseek | 100.0% | — | 0.0% | 1376 ms |
| gemini | 100.0% | 59.7% | 10.9% | 1245 ms |
| mistral | 83.3% | — | 11.7% | 910 ms |
| openai | 99.7% | 87.0% | 0.0% | 1137 ms |
| openrouter | 100.0% | — | 0.0% | 1393 ms |
| xai | 100.0% | — | 0.0% | 845 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 93.9% | 98.5% | 99.2% | 100.0% | 100.0% | 111 s | 7 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 118 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 70.8% | 79.2% | 95.8% | 100.0% | 100.0% | 26 s | 56 min |
| openai | 264 | 260 | 4 | 0 | 70.8% | 74.2% | 84.2% | 95.1% | 100.0% | 68 s | 205 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
