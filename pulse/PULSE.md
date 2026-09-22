# FILL — the inference availability index

*As of 2026-09-22T06:05:03+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 92.5** · FILL·FLEX 85.3

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.0% | — | 97.9% (n=96) | 100.0% (n=30) |
| GEM·FILL | 85.3% | 70.6% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 87.5% | — | 87.5% (n=48) | — |
| OAI·FILL | 93.1% | 100.0% (n=17) | 79.2% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1382 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 754 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 707 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1404 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1184 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1746 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1518 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1735 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1187 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1040 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1250 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 8111 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3200 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 850 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 828 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 96.7% | 3.3% | 11766 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 979 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1839 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 70.0% | 30.0% | 4077 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1175 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 91.7% | 8.3% | 3831 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1296 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 701 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 592 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 993 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 913 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1065 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1061 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1042 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 758 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 745 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1189 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 956 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 789 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 997 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 879 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1558 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 1206 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1667 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1545 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1810 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1042 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 1187 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 24909 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1228 ms |
| deepseek | 100.0% | — | 0.0% | 1163 ms |
| gemini | 100.0% | 89.2% | 6.1% | 976 ms |
| mistral | 100.0% | — | 0.0% | 636 ms |
| openai | 100.0% | 99.5% | 0.0% | 899 ms |
| openrouter | 100.0% | — | 0.0% | 1421 ms |
| xai | 100.0% | — | 0.0% | 1268 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 95 | 1 | 0 | 97.9% | 100 s | 16 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 82 s | 107 s |
| mistral | 48 | 48 | 0 | 0 | 87.5% | 66 s | 116 min |
| openai | 96 | 94 | 2 | 0 | 79.8% | 100 s | 185 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
