# FILL — the inference availability index

*As of 2026-09-21T18:05:03+00:00 · probe pulse-1.2.2 · methodology 1.2.0*

**FILL 85.5** · FILL·FLEX 52.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 70.6% | 41.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 79.2% | — | 79.2% (n=48) | — |
| OAI·FILL | 85.8% | 64.7% (n=17) | 92.7% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1444 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 883 ms |  |
| anthropic/claude-haiku-4-5/standard | 59 | 100.0% | 0.0% | 733 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1175 ms |  |
| anthropic/claude-opus-5/standard | 59 | 100.0% | 0.0% | 1201 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1530 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1992 ms |  |
| anthropic/claude-sonnet-5/standard | 59 | 100.0% | 0.0% | 1746 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1168 ms |  |
| deepseek/deepseek-v4-flash/standard | 59 | 100.0% | 0.0% | 932 ms |  |
| deepseek/deepseek-v4-pro/standard | 59 | 100.0% | 0.0% | 1268 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 50.0% | 50.0% | 2919 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 4784 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 59 | 100.0% | 0.0% | 852 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 59 | 100.0% | 0.0% | 865 ms |  |
| gemini/gemini-3.5-flash/flex | 59 | 39.0% | 54.2% | 15108 ms |  |
| gemini/gemini-3.5-flash/standard | 59 | 100.0% | 0.0% | 995 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1858 ms |  |
| gemini/gemini-3.7-flash/flex | 59 | 11.9% | 78.0% | 30853 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1503 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 8.3% | 91.7% | 2228 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1278 ms |  |
| mistral/mistral-large/standard | 59 | 100.0% | 0.0% | 745 ms |  |
| mistral/mistral-small/standard | 59 | 100.0% | 0.0% | 612 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1124 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1778 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1509 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1138 ms |  |
| openai/gpt-5.6-luna/flex | 59 | 61.0% | 0.0% | 5961 ms |  |
| openai/gpt-5.6-luna/priority | 59 | 100.0% | 0.0% | 816 ms |  |
| openai/gpt-5.6-luna/standard | 59 | 100.0% | 0.0% | 964 ms |  |
| openai/gpt-5.6-sol/flex | 59 | 8.5% | 0.0% | 8544 ms |  |
| openai/gpt-5.6-sol/standard | 59 | 100.0% | 0.0% | 1265 ms |  |
| openai/gpt-5.6-terra/flex | 59 | 100.0% | 0.0% | 993 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1268 ms |  |
| openai/gpt-5.6-terra/standard | 59 | 100.0% | 0.0% | 1111 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1530 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1552 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 2053 ms |  |
| openrouter/claude-sonnet-5/standard | 59 | 100.0% | 0.0% | 1506 ms |  |
| openrouter/gemini-3.7-flash/standard | 59 | 100.0% | 0.0% | 1767 ms |  |
| openrouter/gpt-5.6-terra/standard | 59 | 100.0% | 0.0% | 1255 ms |  |
| xai/grok-4.20/standard | 59 | 100.0% | 0.0% | 739 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1464 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1240 ms |
| deepseek | 100.0% | — | 0.0% | 1147 ms |
| gemini | 100.0% | 47.6% | 26.6% | 991 ms |
| mistral | 100.0% | — | 0.0% | 657 ms |
| openai | 100.0% | 61.7% | 0.0% | 1166 ms |
| openrouter | 100.0% | — | 0.0% | 1482 ms |
| xai | 100.0% | — | 0.0% | 745 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 88 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 82 s | 106 s |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 38 s | 130 min |
| openai | 96 | 92 | 4 | 0 | 94.6% | 69 s | 56 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
