# FILL — the inference availability index

*As of 2026-09-22T00:05:10+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 94.1** · FILL·FLEX 88.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 89.6% | — | 89.6% (n=48) | — |
| OAI·FILL | 91.0% | 94.1% (n=17) | 85.4% (n=96) | 93.3% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1570 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 884 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 751 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1352 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1258 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1641 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1476 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1255 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1102 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1036 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1301 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 2678 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3667 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 843 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 816 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 10353 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1017 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1854 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 71.7% | 28.3% | 3285 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1309 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 100.0% | 0.0% | 2799 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1299 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 745 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 664 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1061 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1061 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1201 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 945 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 93.3% | 0.0% | 4060 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 774 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 767 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 91.7% | 0.0% | 1028 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1036 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 831 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1011 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 943 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1161 ms |  |
| openai/gpt-6-astra/flex | 12 | 75.0% | 0.0% | 1354 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1774 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1485 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1858 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1201 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 816 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1570 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1168 ms |
| deepseek | 100.0% | — | 0.0% | 1194 ms |
| gemini | 100.0% | 91.2% | 4.9% | 964 ms |
| mistral | 100.0% | — | 0.0% | 713 ms |
| openai | 100.0% | 94.1% | 0.0% | 970 ms |
| openrouter | 100.0% | — | 0.0% | 1455 ms |
| xai | 100.0% | — | 0.0% | 830 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 94 | 2 | 0 | 100.0% | 96 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 78 s | 107 s |
| mistral | 48 | 46 | 2 | 0 | 89.1% | 44 s | 118 min |
| openai | 96 | 94 | 2 | 0 | 86.2% | 82 s | 185 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
