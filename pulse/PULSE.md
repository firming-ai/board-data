# FILL — the inference availability index

*As of 2026-10-29T10:05:03+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-10-30T10:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-29/10.json`; their sha256 `29149ebf4a67…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.8** · FILL·FLEX 80.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 80.0% | 61.1% (n=18) | 99.0% (n=96) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 95.3% | 90.6% (n=32) | 95.2% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1063 ms |
| bedrock | 100.0% | — | 0.0% | 685 ms |
| deepseek | 99.2% | — | 0.0% | 1365 ms |
| gemini | 100.0% | 65.5% | 7.9% | 1304 ms |
| mistral | 100.0% | — | 0.0% | 908 ms |
| openai | 99.3% | 92.5% | 0.0% | 1119 ms |
| openrouter | 100.0% | — | 0.0% | 1393 ms |
| xai | 100.0% | — | 0.0% | 857 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 99.2% | 100.0% | 100.0% | 100.0% | 100.0% | 96 s | 3 min |
| gemini | 96 | 96 | 0 | 0 | 99.0% | 99.0% | 99.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 22 s | 2 min |
| openai | 312 | 297 | 15 | 0 | 84.5% | 89.9% | 99.0% | 98.7% | 100.0% | 68 s | 27 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
