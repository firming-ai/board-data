# FILL — the inference availability index

*As of 2026-09-30T22:05:05+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-01T22:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-30/22.json`; their sha256 `fa7c5b8d5e22…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 80.4** · FILL·FLEX 78.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 37.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 68.0% | — | 35.9% (n=192) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 90.7% | 90.0% (n=20) | 82.0% (n=222) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1605 ms |
| bedrock | 100.0% | — | 0.0% | 731 ms |
| deepseek | 100.0% | — | 0.0% | 1182 ms |
| gemini | 100.0% | 75.3% | 13.9% | 1015 ms |
| mistral | 100.0% | — | 0.0% | 701 ms |
| openai | 95.6% | 87.9% | 0.0% | 1131 ms |
| openrouter | 100.0% | — | 0.0% | 1583 ms |
| xai | 100.0% | — | 0.0% | 860 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 190 | 2 | 0 | — | — | 35.3% | 80 min | 136 min |
| gemini | 48 | 48 | 0 | 0 | — | — | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | — | — | 100.0% | 23 s | 3 min |
| openai | 224 | 190 | 2 | 32 | — | — | 81.5% | 67 s | 32 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
