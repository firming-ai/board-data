# FILL — the inference availability index

*As of 2026-09-27T07:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-28T07:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-27/07.json`; their sha256 `9ee7f82e7387…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 100.0** · FILL·FLEX 100.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=144) | 100.0% (n=30) |
| GEM·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 100.0% | 100.0% (n=19) | 100.0% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1333 ms |
| bedrock | 100.0% | — | 0.0% | 696 ms |
| deepseek | 100.0% | — | 0.0% | 1213 ms |
| gemini | 100.0% | 84.5% | 8.7% | 968 ms |
| mistral | 99.2% | — | 0.8% | 632 ms |
| openai | 100.0% | 97.8% | 0.0% | 952 ms |
| openrouter | 100.0% | — | 0.0% | 1561 ms |
| xai | 97.4% | — | 0.0% | 737 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 144 | 0 | 0 | 100.0% | 101 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 22 s | 117 s |
| openai | 192 | 192 | 0 | 0 | 100.0% | 49 s | 3 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
