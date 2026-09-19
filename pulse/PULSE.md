# FILL — the inference availability index

*As of 2026-09-19T12:05:02+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 95.4** · FILL·FLEX 88.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=52) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=26) | — |
| MIS·FILL | 96.2% | — | 96.2% (n=26) | — |
| OAI·FILL | 98.1% | 100.0% (n=17) | 94.2% (n=52) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1539 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 840 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 745 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1206 ms |  |
| anthropic/claude-opus-5/standard | 60 | 98.3% | 1.7% | 1109 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1618 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2037 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1742 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1087 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1013 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1273 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 3050 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 2978 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 813 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 805 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 6641 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 930 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1592 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 55.0% | 45.0% | 6242 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1398 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 100.0% | 0.0% | 2744 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1286 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 713 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 586 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 876 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1115 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1129 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 796 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1245 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 670 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 718 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 91.7% | 0.0% | 1028 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 949 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 98.3% | 0.0% | 825 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1005 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 841 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 972 ms |  |
| openai/gpt-6-astra/flex | 12 | 83.3% | 0.0% | 1275 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1564 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1548 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1644 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 970 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 716 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1319 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 99.5% | — | 0.5% | 1180 ms |
| deepseek | 100.0% | — | 0.0% | 1152 ms |
| gemini | 100.0% | 86.2% | 7.8% | 901 ms |
| mistral | 100.0% | — | 0.0% | 667 ms |
| openai | 100.0% | 96.1% | 0.0% | 870 ms |
| openrouter | 100.0% | — | 0.0% | 1424 ms |
| xai | 100.0% | — | 0.0% | 730 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 56 | 56 | 0 | 0 | 100.0% | 95 s | 2 min |
| gemini | 28 | 28 | 0 | 0 | 100.0% | 82 s | 112 s |
| mistral | 28 | 28 | 0 | 0 | 96.4% | 32 s | 5 min |
| openai | 56 | 55 | 1 | 0 | 94.5% | 67 s | 56 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
