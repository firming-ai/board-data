# FILL — the inference availability index

*As of 2026-09-23T14:05:02+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T14:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/14.json`; their sha256 `fa7f55c8455c…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 86.4** · FILL·FLEX 66.7

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 95.8% | — | 91.5% (n=130) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 81.1% | 68.4% (n=19) | 75.0% (n=164) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1644 ms |
| bedrock | 100.0% | — | 0.0% | 746 ms |
| deepseek | 100.0% | — | 0.0% | 1288 ms |
| gemini | 100.0% | 52.1% | 23.8% | 1175 ms |
| mistral | 100.0% | — | 0.0% | 800 ms |
| openai | 96.6% | 86.0% | 0.0% | 1275 ms |
| openrouter | 100.0% | — | 0.0% | 1858 ms |
| xai | 100.0% | — | 0.0% | 901 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 132 | 126 | 6 | 0 | 95.2% | 3 min | 50 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 90 s | 108 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 52 s | 44 min |
| openai | 168 | 145 | 13 | 10 | 80.0% | 66 s | 134 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
