# FILL — the inference availability index

*As of 2026-10-01T02:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-02T02:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-01/02.json`; their sha256 `d4924d996fb5…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 86.3** · FILL·FLEX 98.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 68.8% | — | 37.5% (n=192) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 92.9% | 100.0% (n=32) | 78.7% (n=230) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1533 ms |
| bedrock | 100.0% | — | 0.0% | 742 ms |
| deepseek | 100.0% | — | 0.0% | 1156 ms |
| gemini | 100.0% | 84.5% | 8.7% | 1067 ms |
| mistral | 100.0% | — | 0.0% | 726 ms |
| openai | 93.7% | 94.6% | 0.0% | 1047 ms |
| openrouter | 100.0% | — | 0.0% | 1503 ms |
| xai | 100.0% | — | 0.0% | 917 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 191 | 1 | 0 | — | — | 41.4% | 70 min | 134 min |
| gemini | 48 | 48 | 0 | 0 | — | — | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | — | — | 100.0% | 23 s | 3 min |
| openai | 232 | 191 | 1 | 40 | — | — | 77.9% | 63 s | 70 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
