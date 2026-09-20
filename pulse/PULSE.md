# FILL — the inference availability index

*As of 2026-09-20T22:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 96.1** · FILL·FLEX 85.3

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 94.1% | 82.3% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1509 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 784 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 692 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1379 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1194 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1681 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1953 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1746 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 993 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 855 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1268 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 4226 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3453 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 743 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 769 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 8047 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 924 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1608 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 60.0% | 40.0% | 3106 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1317 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 2324 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1154 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 674 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 580 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 989 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 893 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1017 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 710 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 962 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 644 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 730 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 70.0% | 0.0% | 4260 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 941 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 717 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 870 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 758 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1230 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1182 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1349 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1444 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1667 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 970 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 710 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1225 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1258 ms |
| deepseek | 100.0% | — | 0.0% | 1034 ms |
| gemini | 100.0% | 86.6% | 7.6% | 899 ms |
| mistral | 100.0% | — | 0.0% | 640 ms |
| openai | 99.5% | 91.2% | 0.0% | 804 ms |
| openrouter | 100.0% | — | 0.0% | 1357 ms |
| xai | 100.0% | — | 0.0% | 716 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 79 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 108 s |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 34 s | 211 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 68 s | 14 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
