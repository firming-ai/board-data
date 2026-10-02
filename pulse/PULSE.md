# FILL — the inference availability index

*As of 2026-10-01T04:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-02T04:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-01/04.json`; their sha256 `3ea86ea41676…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 83.6** · FILL·FLEX 89.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 72.9% | — | 45.8% (n=192) | 100.0% (n=30) |
| GEM·FILL | 85.3% | 70.6% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 92.5% | 100.0% (n=32) | 77.3% (n=234) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1567 ms |
| bedrock | 100.0% | — | 0.0% | 751 ms |
| deepseek | 100.0% | — | 0.0% | 1299 ms |
| gemini | 100.0% | 79.9% | 10.2% | 1109 ms |
| mistral | 100.0% | — | 0.0% | 791 ms |
| openai | 99.5% | 99.7% | 0.0% | 1110 ms |
| openrouter | 100.0% | — | 0.0% | 1494 ms |
| xai | 100.0% | — | 0.0% | 966 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 191 | 1 | 0 | — | — | 49.7% | 61 min | 133 min |
| gemini | 48 | 48 | 0 | 0 | — | — | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | — | — | 100.0% | 23 s | 3 min |
| openai | 236 | 190 | 2 | 44 | — | — | 76.5% | 66 s | 71 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
