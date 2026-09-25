# FILL — the inference availability index

*As of 2026-09-24T15:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-25T15:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-24/15.json`; their sha256 `6e8cec6f0f94…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 82.0** · FILL·FLEX 50.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 96.9% | — | 93.8% (n=144) | 100.0% (n=30) |
| GEM·FILL | 64.7% | 29.4% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 84.3% | 68.4% (n=19) | 84.4% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1500 ms |
| bedrock | 100.0% | — | 0.0% | 745 ms |
| deepseek | 99.2% | — | 0.0% | 1288 ms |
| gemini | 99.3% | 32.0% | 34.3% | 1253 ms |
| mistral | 100.0% | — | 0.0% | 807 ms |
| openai | 98.3% | 81.6% | 0.0% | 1240 ms |
| openrouter | 100.0% | — | 0.0% | 1767 ms |
| xai | 100.0% | — | 0.0% | 901 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 144 | 0 | 0 | 95.1% | 117 s | 47 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 116 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 36 s | 8 min |
| openai | 192 | 179 | 13 | 0 | 91.1% | 66 s | 135 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
