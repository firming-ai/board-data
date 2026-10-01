# FILL — the inference availability index

*As of 2026-09-30T18:05:03+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-01T18:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-30/18.json`; their sha256 `a3230d0cd4c1…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 75.9** · FILL·FLEX 64.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 37.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 66.4% | — | 32.8% (n=192) | 100.0% (n=30) |
| GEM·FILL | 70.6% | 41.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 90.8% | 85.0% (n=20) | 87.4% (n=214) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1854 ms |
| bedrock | 100.0% | — | 0.0% | 733 ms |
| deepseek | 100.0% | — | 0.0% | 1238 ms |
| gemini | 100.0% | 65.5% | 18.3% | 1072 ms |
| mistral | 100.0% | — | 0.0% | 755 ms |
| openai | 96.4% | 94.1% | 0.0% | 1208 ms |
| openrouter | 100.0% | — | 0.0% | 1763 ms |
| xai | 100.0% | — | 0.0% | 934 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 188 | 4 | 0 | — | — | 34.0% | 82 min | 136 min |
| gemini | 48 | 48 | 0 | 0 | — | — | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | — | — | 100.0% | 23 s | 2 min |
| openai | 216 | 190 | 2 | 24 | — | — | 86.9% | 68 s | 22 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
