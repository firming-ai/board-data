# FILL — the inference availability index

*As of 2026-09-22T20:05:04+00:00 · probe pulse-1.3.0 · methodology 1.2.1*

*Published 2026-09-23T20:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-22/20.json`; their sha256 `94bad9163340…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 88.1** · FILL·FLEX 76.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.4% | — | 94.8% (n=96) | 100.0% (n=30) |
| GEM·FILL | 76.5% | 52.9% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 90.3% | 100.0% (n=17) | 70.8% (n=96) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1127 ms |
| deepseek | 100.0% | — | 0.0% | 1078 ms |
| gemini | 99.3% | 67.5% | 16.3% | 999 ms |
| mistral | 99.2% | — | 0.8% | 653 ms |
| openai | 99.5% | 100.0% | 0.0% | 1050 ms |
| openrouter | 100.0% | — | 0.0% | 1638 ms |
| xai | 100.0% | — | 0.0% | 760 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 94.8% | 2 min | 55 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 84 s | 115 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 48 s | 24 min |
| openai | 96 | 81 | 5 | 10 | 74.7% | 88 s | 97 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
