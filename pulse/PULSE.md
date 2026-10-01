# FILL — the inference availability index

*As of 2026-09-30T08:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-01T08:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-30/08.json`; their sha256 `03ae9e2ef0be…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 86.8** · FILL·FLEX 86.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 37.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 74.7% | — | 49.5% (n=192) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 97.6% | 95.0% (n=20) | 97.9% (n=194) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1778 ms |
| bedrock | 100.0% | — | 0.0% | 723 ms |
| deepseek | 100.0% | — | 0.0% | 1223 ms |
| gemini | 100.0% | 75.3% | 13.7% | 976 ms |
| mistral | 99.2% | — | 0.8% | 685 ms |
| openai | 97.2% | 87.9% | 0.0% | 1136 ms |
| openrouter | 100.0% | — | 0.0% | 1684 ms |
| xai | 100.0% | — | 0.0% | 804 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 172 | 16 | 4 | 49.4% | 54 min | 118 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 47 | 0 | 1 | 97.9% | 25 s | 11 min |
| openai | 196 | 192 | 0 | 4 | 96.9% | 68 s | 21 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
