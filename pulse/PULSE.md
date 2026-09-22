# FILL — the inference availability index

*As of 2026-09-22T15:05:02+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 83.7** *(gap)* · FILL·FLEX 29.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 17.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.9% | — | 95.8% (n=96) | 100.0% (n=30) |
| GEM·FILL | 64.7% | 29.4% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 88.5% | — | 77.1% (n=96) | 100.0% (n=9) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1485 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 897 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 694 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1644 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1223 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 8665 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2584 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1941 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1120 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 935 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1317 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 0.0% | 100.0% | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3311 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 20.0% | 38.3% | 53370 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 1085 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 85.0% | 11.7% | 3763 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1046 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 2553 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 3.3% | 96.7% | 32241 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1846 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 0.0% | 100.0% | — ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1368 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 802 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 632 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1206 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1240 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1163 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1098 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 84.6% | 0.0% | 3200 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 1030 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 979 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1792 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 2662 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 958 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1253 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1325 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1268 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1589 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 2141 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1749 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1965 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1450 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 778 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1390 ms |  |
| xai/grok-4.7/standard | 12 | 91.7% | 0.0% | 4532 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1317 ms |
| deepseek | 100.0% | — | 0.0% | 1166 ms |
| gemini | 100.0% | 33.5% | 29.6% | 1098 ms |
| mistral | 100.0% | — | 0.0% | 727 ms |
| openai | 100.0% | 95.6% | 0.0% | 1362 ms |
| openrouter | 100.0% | — | 0.0% | 1725 ms |
| xai | 98.7% | — | 0.0% | 796 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 95 | 1 | 0 | 95.8% | 2 min | 45 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 75 s | 112 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 48 s | 24 min |
| openai | 96 | 94 | 0 | 2 | 75.0% | 2 min | 185 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
