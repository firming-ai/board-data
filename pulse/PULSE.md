# FILL — the inference availability index

*As of 2026-09-22T23:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-23T23:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-22/23.json`; their sha256 `693302b7cb6c…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.9** · FILL·FLEX 88.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.0% | — | 94.0% (n=100) | 100.0% (n=29) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 90.4% | 100.0% (n=19) | 71.2% (n=104) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1204 ms |
| bedrock | 100.0% | — | 0.0% | 742 ms |
| deepseek | 100.0% | — | 0.0% | 1138 ms |
| gemini | 100.0% | 73.2% | 14.5% | 1009 ms |
| mistral | 100.0% | — | 0.0% | 677 ms |
| openai | 98.3% | 96.5% | 0.0% | 978 ms |
| openrouter | 100.0% | — | 0.0% | 1573 ms |
| xai | 100.0% | — | 0.0% | 749 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 102 | 101 | 1 | 0 | 95.0% | 2 min | 52 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 84 s | 115 s |
| mistral | 48 | 47 | 1 | 0 | 97.9% | 42 s | 29 min |
| openai | 108 | 95 | 3 | 10 | 74.3% | 73 s | 131 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
