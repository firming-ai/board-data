# FILL — the inference availability index

*As of 2026-09-30T12:05:02+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-01T12:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-30/12.json`; their sha256 `583253dc6a94…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 79.3** · FILL·FLEX 67.6

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 37.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 67.5% | — | 34.9% (n=192) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 88.0% | 70.0% (n=20) | 94.1% (n=202) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1774 ms |
| bedrock | 100.0% | — | 0.0% | 700 ms |
| deepseek | 100.0% | — | 0.0% | 1245 ms |
| gemini | 100.0% | 73.7% | 13.9% | 1007 ms |
| mistral | 100.0% | — | 0.0% | 713 ms |
| openai | 97.2% | 85.4% | 0.0% | 1120 ms |
| openrouter | 100.0% | — | 0.0% | 1667 ms |
| xai | 94.7% | — | 0.0% | 864 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 180 | 8 | 4 | 32.1% | 74 min | 128 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 47 | 0 | 1 | 97.9% | 24 s | 63 s |
| openai | 204 | 192 | 0 | 12 | 93.1% | 68 s | 21 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
