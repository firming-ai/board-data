# FILL — the inference availability index

*As of 2026-10-01T12:05:13+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-02T12:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-01/12.json`; their sha256 `b548dc01a0d2…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 82.7** · FILL·FLEX 77.6

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 86.5% | — | 72.9% (n=192) | 100.0% (n=30) |
| GEM·FILL | 70.6% | 41.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 90.9% | 96.9% (n=32) | 75.8% (n=240) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1728 ms |
| bedrock | 100.0% | — | 0.0% | 723 ms |
| deepseek | 100.0% | — | 0.0% | 1354 ms |
| gemini | 100.0% | 76.3% | 12.8% | 1111 ms |
| mistral | 100.0% | — | 0.0% | 835 ms |
| openai | 99.2% | 97.1% | 0.0% | 1137 ms |
| openrouter | 100.0% | — | 0.0% | 1621 ms |
| xai | 90.8% | — | 0.0% | 1067 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 180 | 12 | 0 | — | — | 77.8% | 7 min | 128 min |
| gemini | 48 | 48 | 0 | 0 | — | — | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | — | — | 100.0% | 22 s | 12 min |
| openai | 240 | 192 | 0 | 48 | — | — | 75.8% | 68 s | 54 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
