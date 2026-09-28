# FILL — the inference availability index

*As of 2026-09-27T11:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-28T11:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-27/11.json`; their sha256 `458e87c2f1b6…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 96.1** · FILL·FLEX 88.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=144) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 100.0% | 100.0% (n=19) | 100.0% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1352 ms |
| bedrock | 100.0% | — | 0.0% | 685 ms |
| deepseek | 100.0% | — | 0.0% | 1192 ms |
| gemini | 100.0% | 85.6% | 8.1% | 962 ms |
| mistral | 100.0% | — | 0.0% | 616 ms |
| openai | 98.7% | 97.4% | 0.0% | 932 ms |
| openrouter | 100.0% | — | 0.0% | 1488 ms |
| xai | 100.0% | — | 0.0% | 683 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 144 | 0 | 0 | 100.0% | 102 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 22 s | 4 min |
| openai | 192 | 192 | 0 | 0 | 100.0% | 46 s | 3 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
