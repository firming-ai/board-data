# FILL — the inference availability index

*As of 2026-10-29T01:05:02+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-10-30T01:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-29/01.json`; their sha256 `fe5f6767ba6d…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 96.2** · FILL·FLEX 92.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 88.9% | 77.8% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 99.8% | 100.0% (n=32) | 99.4% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1113 ms |
| bedrock | 93.8% | — | 6.2% | 836 ms |
| deepseek | 100.0% | — | 0.0% | 1368 ms |
| gemini | 100.0% | 79.1% | 3.5% | 1213 ms |
| mistral | 100.0% | — | 0.0% | 884 ms |
| openai | 99.0% | 99.5% | 0.0% | 1251 ms |
| openrouter | 100.0% | — | 0.0% | 1592 ms |
| xai | 100.0% | — | 0.0% | 932 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 98.5% | 100.0% | 100.0% | 100.0% | 100.0% | 99 s | 3 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 32 s | 3 min |
| openai | 312 | 311 | 1 | 0 | 87.1% | 91.6% | 99.4% | 100.0% | 100.0% | 67 s | 21 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
