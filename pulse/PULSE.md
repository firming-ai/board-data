# FILL — the inference availability index

*As of 2026-09-24T18:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-25T18:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-24/18.json`; their sha256 `fd3b428d9380…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 82.1** · FILL·FLEX 47.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 98.6% | — | 97.2% (n=144) | 100.0% (n=30) |
| GEM·FILL | 64.7% | 29.4% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 83.0% | 63.2% (n=19) | 85.9% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1506 ms |
| bedrock | 100.0% | — | 0.0% | 758 ms |
| deepseek | 100.0% | — | 0.0% | 1250 ms |
| gemini | 99.3% | 29.9% | 39.5% | 1189 ms |
| mistral | 100.0% | — | 0.0% | 778 ms |
| openai | 98.7% | 88.2% | 0.0% | 1145 ms |
| openrouter | 100.0% | — | 0.0% | 1573 ms |
| xai | 100.0% | — | 0.0% | 858 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 144 | 0 | 0 | 97.9% | 116 s | 20 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 35 s | 8 min |
| openai | 192 | 172 | 20 | 0 | 94.8% | 64 s | 59 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
