# FILL — the inference availability index

*As of 2026-09-20T16:05:02+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 97.7** · FILL·FLEX 91.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 96.1% | 88.2% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1387 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 841 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 745 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1278 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1187 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1410 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2028 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1763 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1067 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1011 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1312 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 2984 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2990 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 831 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 780 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 5831 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 943 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1599 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 60.0% | 40.0% | 3956 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1450 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 75.0% | 25.0% | 3516 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1357 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 692 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 580 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1026 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 917 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 997 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 754 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1100 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 664 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 760 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 76.7% | 0.0% | 1482 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 952 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 757 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 966 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 825 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1398 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1199 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1452 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1548 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1573 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 966 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 733 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1341 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1235 ms |
| deepseek | 100.0% | — | 0.0% | 1175 ms |
| gemini | 100.0% | 85.6% | 8.1% | 904 ms |
| mistral | 100.0% | — | 0.0% | 642 ms |
| openai | 100.0% | 93.1% | 0.0% | 865 ms |
| openrouter | 100.0% | — | 0.0% | 1387 ms |
| xai | 100.0% | — | 0.0% | 736 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 84 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 78 s | 108 s |
| mistral | 48 | 47 | 1 | 0 | 100.0% | 25 s | 15 min |
| openai | 96 | 95 | 1 | 0 | 100.0% | 68 s | 12 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
