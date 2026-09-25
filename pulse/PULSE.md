# FILL — the inference availability index

*As of 2026-09-24T14:05:02+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-25T14:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-24/14.json`; their sha256 `d01db2706c31…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 83.6** · FILL·FLEX 58.3

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 96.5% | — | 93.1% (n=144) | 100.0% (n=30) |
| GEM·FILL | 64.7% | 29.4% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 89.5% | 84.2% (n=19) | 84.4% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1638 ms |
| bedrock | 100.0% | — | 0.0% | 734 ms |
| deepseek | 100.0% | — | 0.0% | 1283 ms |
| gemini | 100.0% | 46.4% | 25.3% | 1175 ms |
| mistral | 100.0% | — | 0.0% | 820 ms |
| openai | 97.0% | 83.8% | 0.0% | 1156 ms |
| openrouter | 100.0% | — | 0.0% | 1828 ms |
| xai | 100.0% | — | 0.0% | 877 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 144 | 0 | 0 | 93.8% | 2 min | 81 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 116 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 36 s | 8 min |
| openai | 192 | 182 | 10 | 0 | 89.0% | 67 s | 137 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
