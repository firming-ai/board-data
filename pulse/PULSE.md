# FILL — the inference availability index

*As of 2026-09-19T11:05:03+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 97.3** · FILL·FLEX 94.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=48) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=24) | — |
| MIS·FILL | 95.8% | — | 95.8% (n=24) | — |
| OAI·FILL | 97.9% | 100.0% (n=17) | 93.8% (n=48) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1494 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 836 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 718 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1235 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1136 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 2008 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2049 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1644 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1138 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 993 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1270 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 4118 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 2907 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 731 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 774 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 12271 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 966 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1464 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 66.7% | 31.7% | 4842 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1288 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 5925 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1304 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 700 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 575 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 908 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1140 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1102 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 792 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1473 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 687 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 683 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 86.7% | 0.0% | 1028 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 960 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 96.7% | 0.0% | 826 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1024 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 807 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1034 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1283 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1435 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1441 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1770 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 947 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 700 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1317 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1175 ms |
| deepseek | 100.0% | — | 0.0% | 1140 ms |
| gemini | 100.0% | 88.3% | 6.3% | 943 ms |
| mistral | 100.0% | — | 0.0% | 644 ms |
| openai | 100.0% | 95.1% | 0.0% | 858 ms |
| openrouter | 100.0% | — | 0.0% | 1379 ms |
| xai | 100.0% | — | 0.0% | 704 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 52 | 52 | 0 | 0 | 100.0% | 97 s | 2 min |
| gemini | 26 | 26 | 0 | 0 | 100.0% | 82 s | 114 s |
| mistral | 26 | 25 | 1 | 0 | 96.0% | 32 s | 3 min |
| openai | 52 | 52 | 0 | 0 | 94.2% | 67 s | 57 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
