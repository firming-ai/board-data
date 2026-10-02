# FILL — the inference availability index

*As of 2026-10-01T07:05:12+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-02T07:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-01/07.json`; their sha256 `bd92aff25bcf…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 84.5** · FILL·FLEX 87.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 79.2% | — | 58.3% (n=192) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 91.8% | 100.0% (n=32) | 75.4% (n=240) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1763 ms |
| bedrock | 100.0% | — | 0.0% | 720 ms |
| deepseek | 100.0% | — | 0.0% | 1312 ms |
| gemini | 100.0% | 78.9% | 11.9% | 1173 ms |
| mistral | 100.0% | — | 0.0% | 777 ms |
| openai | 99.2% | 100.0% | 0.0% | 1155 ms |
| openrouter | 100.0% | — | 0.0% | 1545 ms |
| xai | 100.0% | — | 0.0% | 997 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 189 | 3 | 0 | — | — | 61.9% | 10 min | 133 min |
| gemini | 48 | 48 | 0 | 0 | — | — | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | — | — | 100.0% | 23 s | 3 min |
| openai | 240 | 191 | 1 | 48 | — | — | 75.7% | 66 s | 48 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
