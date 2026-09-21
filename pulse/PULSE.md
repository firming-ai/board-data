# FILL — the inference availability index

*As of 2026-09-21T21:05:09+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 92.0** · FILL·FLEX 73.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 89.6% | — | 89.6% (n=48) | — |
| OAI·FILL | 81.8% | 58.8% (n=17) | 86.5% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1545 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 843 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1384 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1145 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1407 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2180 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1788 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1065 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1015 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1317 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 8982 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3093 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 848 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 835 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 96.7% | 3.3% | 9927 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1003 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1739 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 66.7% | 33.3% | 3594 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1429 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 3667 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1435 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 758 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 649 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1149 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1418 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1228 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1017 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 63.3% | 0.0% | 6406 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 784 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 804 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 10.0% | 0.0% | 11885 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1173 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 841 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1087 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 985 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1240 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1452 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 2086 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1577 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1795 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1317 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 791 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1343 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1213 ms |
| deepseek | 100.0% | — | 0.0% | 1124 ms |
| gemini | 100.0% | 87.6% | 7.0% | 976 ms |
| mistral | 100.0% | — | 0.0% | 704 ms |
| openai | 100.0% | 62.8% | 0.0% | 1030 ms |
| openrouter | 100.0% | — | 0.0% | 1542 ms |
| xai | 100.0% | — | 0.0% | 794 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 89 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 76 s | 106 s |
| mistral | 48 | 47 | 1 | 0 | 89.4% | 38 s | 117 min |
| openai | 96 | 91 | 5 | 0 | 90.1% | 69 s | 97 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
