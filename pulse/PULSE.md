# FILL — the inference availability index

*As of 2026-09-19T17:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 93.0** · FILL·FLEX 79.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=72) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=36) | — |
| MIS·FILL | 97.2% | — | 97.2% (n=36) | — |
| OAI·FILL | 96.7% | 94.1% (n=17) | 95.8% (n=72) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1634 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 850 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 780 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 2777 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1230 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1506 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2128 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1821 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1270 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1009 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1330 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 75.0% | 25.0% | 3460 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 3467 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 869 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 812 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 91.7% | 8.3% | 11081 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1015 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1628 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 53.3% | 46.7% | 5131 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1536 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 75.0% | 25.0% | 4201 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1799 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 777 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 633 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1138 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1291 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1133 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 962 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1003 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 777 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 766 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 96.7% | 0.0% | 1055 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1042 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 812 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1038 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 826 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1218 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1393 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1494 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1564 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1778 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1053 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 788 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1539 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1263 ms |
| deepseek | 100.0% | — | 0.0% | 1163 ms |
| gemini | 100.0% | 81.1% | 10.6% | 1001 ms |
| mistral | 100.0% | — | 0.0% | 726 ms |
| openai | 100.0% | 99.0% | 0.0% | 904 ms |
| openrouter | 100.0% | — | 0.0% | 1491 ms |
| xai | 100.0% | — | 0.0% | 794 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 76 | 76 | 0 | 0 | 100.0% | 93 s | 2 min |
| gemini | 38 | 38 | 0 | 0 | 100.0% | 85 s | 116 s |
| mistral | 38 | 38 | 0 | 0 | 97.4% | 35 s | 4 min |
| openai | 76 | 76 | 0 | 0 | 96.1% | 67 s | 46 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
