# FILL — the inference availability index

*As of 2026-09-25T22:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-26T22:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-25/22.json`; their sha256 `f1ff15aec8c5…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 92.1** · FILL·FLEX 80.6

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 96.9% | — | 93.8% (n=144) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 96.9% | 94.7% (n=19) | 95.8% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1412 ms |
| bedrock | 100.0% | — | 0.0% | 729 ms |
| deepseek | 100.0% | — | 0.0% | 1263 ms |
| gemini | 100.0% | 47.4% | 29.6% | 1017 ms |
| mistral | 100.0% | — | 0.0% | 694 ms |
| openai | 97.9% | 94.7% | 0.0% | 1111 ms |
| openrouter | 100.0% | — | 0.0% | 1573 ms |
| xai | 96.0% | — | 0.0% | 805 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 143 | 1 | 0 | 94.4% | 117 s | 60 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 36 s | 20 min |
| openai | 192 | 191 | 1 | 0 | 97.4% | 67 s | 35 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
