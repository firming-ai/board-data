# FILL — the inference availability index

*As of 2026-09-21T10:05:03+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 92.3** · FILL·FLEX 73.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 88.8% | 70.6% (n=17) | 95.8% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1415 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 908 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 778 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1485 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1349 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1880 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2228 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1880 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1258 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1021 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1335 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 3038 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3239 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 848 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 862 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 6708 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 989 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1899 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 35.0% | 40.0% | 41069 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1467 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 75.0% | 25.0% | 2744 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1333 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 701 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 642 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1053 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1373 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1230 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 926 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 947 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 713 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 846 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 13.3% | 0.0% | 11126 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1677 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 841 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 979 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 921 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1245 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1641 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1684 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1580 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1651 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1120 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 780 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1415 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1360 ms |
| deepseek | 100.0% | — | 0.0% | 1152 ms |
| gemini | 100.0% | 78.3% | 7.8% | 972 ms |
| mistral | 100.0% | — | 0.0% | 664 ms |
| openai | 99.5% | 74.5% | 0.0% | 1015 ms |
| openrouter | 100.0% | — | 0.0% | 1482 ms |
| xai | 100.0% | — | 0.0% | 788 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 95 | 1 | 0 | 100.0% | 78 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 75 s | 105 s |
| mistral | 48 | 46 | 2 | 0 | 82.6% | 34 s | 214 min |
| openai | 96 | 96 | 0 | 0 | 95.8% | 69 s | 41 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
