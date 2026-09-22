# FILL — the inference availability index

*As of 2026-09-22T07:05:02+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 95.1** · FILL·FLEX 91.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.0% | — | 97.9% (n=96) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 87.5% | — | 87.5% (n=48) | — |
| OAI·FILL | 89.1% | 88.2% (n=17) | 79.2% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1494 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 835 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 748 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1444 ms |  |
| anthropic/claude-opus-5/standard | 60 | 80.0% | 20.0% | 1147 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 5234 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2193 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1835 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1293 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1098 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1333 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 7080 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3181 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 872 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 836 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 88.3% | 10.0% | 12645 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1013 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1691 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 63.3% | 36.7% | 9349 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1447 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 4569 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1194 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 740 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 609 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1098 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1048 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 935 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 972 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1013 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 821 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1145 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 983 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 764 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1011 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 932 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1173 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 1253 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 2145 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1725 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1992 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1087 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 751 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1429 ms |  |
| xai/grok-4.7/standard | 7 | 100.0% | 0.0% | 3801 ms | ▲ |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 94.0% | — | 6.0% | 1265 ms |
| deepseek | 100.0% | — | 0.0% | 1208 ms |
| gemini | 100.0% | 84.0% | 8.7% | 978 ms |
| mistral | 100.0% | — | 0.0% | 674 ms |
| openai | 100.0% | 99.5% | 0.0% | 932 ms |
| openrouter | 100.0% | — | 0.0% | 1615 ms |
| xai | 100.0% | — | 0.0% | 780 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 95 | 1 | 0 | 97.9% | 102 s | 16 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 84 s | 107 s |
| mistral | 48 | 48 | 0 | 0 | 87.5% | 64 s | 116 min |
| openai | 96 | 95 | 1 | 0 | 78.9% | 103 s | 185 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
