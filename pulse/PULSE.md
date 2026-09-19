# FILL — the inference availability index

*As of 2026-09-19T21:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 97.7** · FILL·FLEX 94.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=88) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=44) | — |
| MIS·FILL | 97.7% | — | 97.7% (n=44) | — |
| OAI·FILL | 98.9% | 100.0% (n=17) | 96.6% (n=88) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1447 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 869 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 740 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1354 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1140 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1470 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1941 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1756 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1050 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 949 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1216 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 3168 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 2873 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 767 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 749 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 9595 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 939 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1644 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 48.3% | 51.7% | 3026 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1291 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 91.7% | 8.3% | 2771 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1354 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 689 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 596 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 947 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1136 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1120 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 908 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 947 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 708 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 724 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1067 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1074 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 812 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1015 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 838 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1168 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 1238 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1461 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1482 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1701 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1013 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 723 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1524 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1223 ms |
| deepseek | 100.0% | — | 0.0% | 1087 ms |
| gemini | 100.0% | 83.2% | 9.5% | 890 ms |
| mistral | 100.0% | — | 0.0% | 658 ms |
| openai | 100.0% | 99.5% | 0.0% | 881 ms |
| openrouter | 100.0% | — | 0.0% | 1398 ms |
| xai | 100.0% | — | 0.0% | 726 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 92 | 92 | 0 | 0 | 100.0% | 92 s | 2 min |
| gemini | 46 | 46 | 0 | 0 | 100.0% | 85 s | 116 s |
| mistral | 46 | 46 | 0 | 0 | 97.8% | 35 s | 11 min |
| openai | 92 | 92 | 0 | 0 | 96.7% | 68 s | 39 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
