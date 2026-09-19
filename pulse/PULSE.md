# FILL — the inference availability index

*As of 2026-09-19T19:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 96.3** · FILL·FLEX 88.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=80) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=40) | — |
| MIS·FILL | 97.5% | — | 97.5% (n=40) | — |
| OAI·FILL | 94.8% | 88.2% (n=17) | 96.2% (n=80) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1500 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 892 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 724 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1368 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1248 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1824 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2078 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1806 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1152 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1011 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1255 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 4068 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 3014 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 98.3% | 1.7% | 777 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 784 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 63.3% | 23.3% | 6355 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 958 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1722 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 60.0% | 35.0% | 3239 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1527 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 2984 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1189 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 716 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 626 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 960 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1211 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1136 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 895 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 98.3% | 0.0% | 1441 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 767 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 721 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 98.3% | 0.0% | 1228 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 968 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 825 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1065 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 879 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1280 ms |  |
| openai/gpt-6-astra/flex | 12 | 75.0% | 0.0% | 1357 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1476 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1605 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1641 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1040 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 751 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1354 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1286 ms |
| deepseek | 100.0% | — | 0.0% | 1152 ms |
| gemini | 100.0% | 75.0% | 10.9% | 937 ms |
| mistral | 100.0% | — | 0.0% | 679 ms |
| openai | 99.5% | 97.5% | 0.0% | 910 ms |
| openrouter | 100.0% | — | 0.0% | 1427 ms |
| xai | 100.0% | — | 0.0% | 757 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 84 | 84 | 0 | 0 | 100.0% | 92 s | 2 min |
| gemini | 42 | 42 | 0 | 0 | 100.0% | 85 s | 116 s |
| mistral | 42 | 42 | 0 | 0 | 97.6% | 37 s | 13 min |
| openai | 84 | 83 | 1 | 0 | 96.4% | 67 s | 43 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
