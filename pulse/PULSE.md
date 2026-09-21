# FILL — the inference availability index

*As of 2026-09-21T09:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 90.4** · FILL·FLEX 67.6

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 88.8% | 70.6% (n=17) | 95.8% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1530 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 845 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 767 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1479 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1354 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1835 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2090 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1869 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1078 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1034 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1220 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 4093 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3285 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 816 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 784 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 8193 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 976 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1694 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 55.0% | 28.3% | 17001 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1450 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 66.7% | 33.3% | 4052 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1376 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 743 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 616 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1059 ms |  |
| openai/gpt-5.5/flex | 12 | 91.7% | 0.0% | 1515 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1189 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1026 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 98.3% | 0.0% | 964 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 754 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 892 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 6.7% | 0.0% | 9691 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1250 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 98.3% | 0.0% | 904 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1124 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 98.3% | 1.7% | 995 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1223 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1485 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1701 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1570 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1854 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1111 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 774 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1567 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1373 ms |
| deepseek | 100.0% | — | 0.0% | 1115 ms |
| gemini | 100.0% | 83.5% | 6.4% | 952 ms |
| mistral | 100.0% | — | 0.0% | 662 ms |
| openai | 99.5% | 71.1% | 0.2% | 1040 ms |
| openrouter | 100.0% | — | 0.0% | 1476 ms |
| xai | 100.0% | — | 0.0% | 780 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 78 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 75 s | 105 s |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 32 s | 211 min |
| openai | 96 | 96 | 0 | 0 | 95.8% | 68 s | 41 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
