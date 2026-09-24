# FILL — the inference availability index

*As of 2026-09-23T09:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T09:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/09.json`; their sha256 `d22986470dd4…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 90.2** · FILL·FLEX 72.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.5% | — | 95.0% (n=120) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 81.9% | 63.2% (n=19) | 82.6% (n=144) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 99.5% | — | 0.5% | 1500 ms |
| bedrock | 100.0% | — | 0.0% | 713 ms |
| deepseek | 100.0% | — | 0.0% | 1152 ms |
| gemini | 100.0% | 78.9% | 11.6% | 1015 ms |
| mistral | 100.0% | — | 0.0% | 729 ms |
| openai | 95.8% | 77.6% | 0.0% | 1042 ms |
| openrouter | 100.0% | — | 0.0% | 1681 ms |
| xai | 100.0% | — | 0.0% | 792 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 122 | 117 | 5 | 0 | 96.6% | 3 min | 46 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 84 s | 113 s |
| mistral | 48 | 47 | 1 | 0 | 97.9% | 42 s | 35 min |
| openai | 148 | 133 | 5 | 10 | 83.2% | 67 s | 127 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
