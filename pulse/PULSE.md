# FILL — the inference availability index

*As of 2026-09-30T00:05:12+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-01T00:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-30/00.json`; their sha256 `16ffc46af2d9…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.2** · FILL·FLEX 86.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 87.1% | — | 74.2% (n=178) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 92.3% | 84.2% (n=19) | 99.5% (n=192) | 93.3% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1432 ms |
| bedrock | 90.6% | — | 9.4% | 754 ms |
| deepseek | 100.0% | — | 0.0% | 1161 ms |
| gemini | 99.3% | 73.7% | 13.4% | 983 ms |
| mistral | 100.0% | — | 0.0% | 687 ms |
| openai | 97.5% | 86.0% | 0.0% | 999 ms |
| openrouter | 100.0% | — | 0.0% | 1533 ms |
| xai | 100.0% | — | 0.0% | 895 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 180 | 170 | 6 | 4 | 73.6% | 5 min | 83 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 47 | 0 | 1 | 97.9% | 35 s | 13 min |
| openai | 192 | 190 | 2 | 0 | 99.5% | 68 s | 24 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
