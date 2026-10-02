# FILL — the inference availability index

*As of 2026-10-01T01:05:02+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-02T01:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-01/01.json`; their sha256 `ffa3aa7af4e9…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 83.1** · FILL·FLEX 86.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 37.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 68.5% | — | 37.0% (n=192) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 89.7% | 90.0% (n=20) | 79.0% (n=228) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 99.5% | — | 0.5% | 1509 ms |
| bedrock | 100.0% | — | 0.0% | 713 ms |
| deepseek | 100.0% | — | 0.0% | 1120 ms |
| gemini | 100.0% | 78.3% | 12.2% | 974 ms |
| mistral | 100.0% | — | 0.0% | 721 ms |
| openai | 96.8% | 92.1% | 0.0% | 997 ms |
| openrouter | 100.0% | — | 0.0% | 1447 ms |
| xai | 100.0% | — | 0.0% | 876 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 191 | 1 | 0 | — | — | 37.2% | 77 min | 134 min |
| gemini | 48 | 48 | 0 | 0 | — | — | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | — | — | 100.0% | 24 s | 3 min |
| openai | 230 | 191 | 1 | 38 | — | — | 79.0% | 58 s | 48 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
