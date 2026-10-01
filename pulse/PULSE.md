# FILL — the inference availability index

*As of 2026-09-30T17:05:03+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-01T17:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-30/17.json`; their sha256 `705790073684…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 80.3** · FILL·FLEX 81.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 37.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 65.4% | — | 30.7% (n=192) | 100.0% (n=30) |
| GEM·FILL | 79.4% | 58.8% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 96.2% | 100.0% (n=20) | 88.7% (n=212) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1813 ms |
| bedrock | 100.0% | — | 0.0% | 734 ms |
| deepseek | 100.0% | — | 0.0% | 1301 ms |
| gemini | 100.0% | 64.4% | 18.9% | 1138 ms |
| mistral | 100.0% | — | 0.0% | 808 ms |
| openai | 96.8% | 85.4% | 0.0% | 1268 ms |
| openrouter | 100.0% | — | 0.0% | 1861 ms |
| xai | 100.0% | — | 0.0% | 1061 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 180 | 12 | 0 | — | — | 32.8% | 90 min | 137 min |
| gemini | 48 | 48 | 0 | 0 | — | — | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | — | — | 100.0% | 24 s | 2 min |
| openai | 214 | 190 | 2 | 22 | — | — | 88.2% | 68 s | 21 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
