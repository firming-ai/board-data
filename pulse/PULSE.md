# FILL — the inference availability index

*As of 2026-09-26T10:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-27T10:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-26/10.json`; their sha256 `344f80905191…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 95.1** · FILL·FLEX 88.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.6% | — | 95.1% (n=144) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 99.5% | 100.0% (n=19) | 98.4% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1404 ms |
| bedrock | 100.0% | — | 0.0% | 723 ms |
| deepseek | 100.0% | — | 0.0% | 1228 ms |
| gemini | 100.0% | 72.7% | 15.4% | 1038 ms |
| mistral | 96.7% | — | 3.3% | 687 ms |
| openai | 97.0% | 92.5% | 0.0% | 1040 ms |
| openrouter | 100.0% | — | 0.0% | 1524 ms |
| xai | 100.0% | — | 0.0% | 770 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 144 | 0 | 0 | 95.1% | 116 s | 39 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 30 s | 3 min |
| openai | 192 | 192 | 0 | 0 | 98.4% | 67 s | 22 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
