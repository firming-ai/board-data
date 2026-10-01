# FILL — the inference availability index

*As of 2026-09-30T02:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-01T02:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-30/02.json`; their sha256 `da568f36dab2…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 89.2** · FILL·FLEX 77.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 86.5% | — | 73.1% (n=182) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 92.8% | 79.0% (n=19) | 99.5% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1564 ms |
| bedrock | 98.4% | — | 1.6% | 739 ms |
| deepseek | 100.0% | — | 0.0% | 1187 ms |
| gemini | 100.0% | 85.6% | 8.1% | 1036 ms |
| mistral | 100.0% | — | 0.0% | 686 ms |
| openai | 97.5% | 87.7% | 0.0% | 1063 ms |
| openrouter | 100.0% | — | 0.0% | 1631 ms |
| xai | 100.0% | — | 0.0% | 877 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 184 | 170 | 10 | 4 | 73.0% | 10 min | 83 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 47 | 0 | 1 | 97.9% | 35 s | 13 min |
| openai | 192 | 190 | 2 | 0 | 100.0% | 68 s | 22 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
