# FILL — the inference availability index

*As of 2026-09-28T18:05:03+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-29T18:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-28/18.json`; their sha256 `82d22e6414d9…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 83.1** · FILL·FLEX 52.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 94.4% | — | 88.9% (n=144) | 100.0% (n=30) |
| GEM·FILL | 61.8% | 23.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 93.0% | 79.0% (n=19) | 100.0% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1515 ms |
| bedrock | 100.0% | — | 0.0% | 689 ms |
| deepseek | 100.0% | — | 0.0% | 1235 ms |
| gemini | 99.3% | 15.5% | 45.9% | 1319 ms |
| mistral | 100.0% | — | 0.0% | 685 ms |
| openai | 96.6% | 93.4% | 0.0% | 1100 ms |
| openrouter | 100.0% | — | 0.0% | 1628 ms |
| xai | 98.7% | — | 0.0% | 830 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 143 | 1 | 0 | 88.8% | 2 min | 241 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 21 s | 52 s |
| openai | 192 | 191 | 1 | 0 | 100.0% | 66 s | 4 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
