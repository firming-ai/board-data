# FILL — the inference availability index

*As of 2026-09-22T08:05:12+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 93.1** · FILL·FLEX 88.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 98.4% | — | 96.9% (n=96) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 87.5% | — | 87.5% (n=48) | — |
| OAI·FILL | 92.7% | 100.0% (n=17) | 78.1% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1628 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 841 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 749 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1687 ms |  |
| anthropic/claude-opus-5/standard | 60 | 85.0% | 15.0% | 1354 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 3893 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 93.3% | 0.0% | 2468 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1996 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1354 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1065 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1325 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 31039 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3453 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 840 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 823 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 85.0% | 6.7% | 11766 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1021 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1657 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 46.7% | 23.3% | 22005 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1664 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 91.7% | 8.3% | 5287 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1488 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 813 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 659 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1038 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1034 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1072 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 949 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 98.3% | 0.0% | 1080 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 800 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 792 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1223 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1074 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 833 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1055 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 970 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1545 ms |  |
| openai/gpt-6-astra/flex | 12 | 83.3% | 0.0% | 1352 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1858 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1760 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1839 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1138 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 774 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1605 ms |  |
| xai/grok-4.7/standard | 12 | 100.0% | 0.0% | 3816 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 95.5% | — | 4.5% | 1441 ms |
| deepseek | 100.0% | — | 0.0% | 1213 ms |
| gemini | 100.0% | 78.3% | 5.5% | 1001 ms |
| mistral | 100.0% | — | 0.0% | 749 ms |
| openai | 100.0% | 98.5% | 0.0% | 974 ms |
| openrouter | 100.0% | — | 0.0% | 1583 ms |
| xai | 100.0% | — | 0.0% | 810 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 94 | 2 | 0 | 97.9% | 104 s | 17 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 84 s | 107 s |
| mistral | 48 | 48 | 0 | 0 | 87.5% | 64 s | 116 min |
| openai | 96 | 94 | 2 | 0 | 78.7% | 100 s | 185 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
