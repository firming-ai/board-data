# FILL — the inference availability index

*As of 2026-09-24T01:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-25T01:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-24/01.json`; their sha256 `c0342a8621e8…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 87.1** · FILL·FLEX 75.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 93.8% | — | 87.5% (n=144) | 100.0% (n=30) |
| GEM·FILL | 76.5% | 52.9% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 91.1% | 94.7% (n=19) | 78.7% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1418 ms |
| bedrock | 100.0% | — | 0.0% | 758 ms |
| deepseek | 100.0% | — | 0.0% | 1076 ms |
| gemini | 100.0% | 65.0% | 19.5% | 1034 ms |
| mistral | 100.0% | — | 0.0% | 708 ms |
| openai | 98.3% | 93.9% | 0.0% | 1042 ms |
| openrouter | 100.0% | — | 0.0% | 1539 ms |
| xai | 100.0% | — | 0.0% | 804 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 141 | 3 | 0 | 88.7% | 5 min | 256 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 104 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 37 s | 18 min |
| openai | 192 | 190 | 2 | 0 | 78.9% | 67 s | 278 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
