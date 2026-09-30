# FILL — the inference availability index

*As of 2026-09-29T11:05:03+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-30T11:05:02+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-29/11.json`; their sha256 `fbf8db27038d…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 89.2** · FILL·FLEX 69.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.7% | — | 95.4% (n=152) | 100.0% (n=30) |
| GEM·FILL | 73.5% | 47.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 96.3% | 89.5% (n=19) | 99.5% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1654 ms |
| bedrock | 84.4% | — | 15.6% | 788 ms |
| deepseek | 100.0% | — | 0.0% | 1243 ms |
| gemini | 100.0% | 57.2% | 22.1% | 997 ms |
| mistral | 100.0% | — | 0.0% | 678 ms |
| openai | 96.6% | 93.9% | 0.0% | 952 ms |
| openrouter | 100.0% | — | 0.0% | 1608 ms |
| xai | 100.0% | — | 0.0% | 757 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 154 | 154 | 0 | 0 | 96.8% | 2 min | 21 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 46 | 2 | 0 | 100.0% | 26 s | 8 min |
| openai | 192 | 191 | 1 | 0 | 99.5% | 66 s | 25 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
