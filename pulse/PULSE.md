# FILL — the inference availability index

*As of 2026-09-21T07:05:12+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 94.0** · FILL·FLEX 82.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 85.3% | 70.6% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 96.7% | 94.1% (n=17) | 95.8% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1435 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 857 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 749 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1223 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1330 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1404 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2090 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1861 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1180 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1080 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1253 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 8095 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3131 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 781 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 800 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 7919 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 893 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 2404 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 63.3% | 36.7% | 3331 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1273 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 75.0% | 25.0% | 2631 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1189 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 687 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 591 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1100 ms |  |
| openai/gpt-5.5/flex | 12 | 91.7% | 0.0% | 1133 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1238 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1050 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 989 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 708 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 964 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 80.0% | 0.0% | 1168 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1082 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 919 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1053 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 926 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1349 ms |  |
| openai/gpt-6-astra/flex | 12 | 75.0% | 0.0% | 1458 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1980 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1638 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1858 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1078 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 729 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1515 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1330 ms |
| deepseek | 100.0% | — | 0.0% | 1168 ms |
| gemini | 100.0% | 87.1% | 7.3% | 879 ms |
| mistral | 100.0% | — | 0.0% | 640 ms |
| openai | 100.0% | 92.2% | 0.0% | 995 ms |
| openrouter | 100.0% | — | 0.0% | 1447 ms |
| xai | 100.0% | — | 0.0% | 731 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 78 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 75 s | 105 s |
| mistral | 48 | 47 | 1 | 0 | 83.0% | 29 s | 212 min |
| openai | 96 | 96 | 0 | 0 | 95.8% | 69 s | 41 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
