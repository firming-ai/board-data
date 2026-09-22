# FILL — the inference availability index

*As of 2026-09-22T09:05:03+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 91.1** · FILL·FLEX 82.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 98.4% | — | 96.9% (n=96) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 87.5% | — | 87.5% (n=48) | — |
| OAI·FILL | 92.4% | 100.0% (n=17) | 77.1% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1592 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 840 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 737 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1335 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1223 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 4028 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2128 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1795 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1161 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1038 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1296 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 50.0% | 0.0% | 62131 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3258 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 823 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 70.0% | 18.3% | 12345 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1015 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1661 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 43.3% | 30.0% | 23553 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1398 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 4717 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1354 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 745 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 649 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1087 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 983 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1032 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 958 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1007 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 791 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 780 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1170 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1152 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 774 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1074 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 995 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1429 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1314 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1861 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1704 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1854 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1177 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 742 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1228 ms |  |
| xai/grok-4.7/standard | 12 | 100.0% | 0.0% | 4505 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1291 ms |
| deepseek | 100.0% | — | 0.0% | 1163 ms |
| gemini | 100.0% | 71.7% | 9.0% | 954 ms |
| mistral | 100.0% | — | 0.0% | 706 ms |
| openai | 100.0% | 100.0% | 0.0% | 991 ms |
| openrouter | 100.0% | — | 0.0% | 1539 ms |
| xai | 100.0% | — | 0.0% | 780 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 94 | 2 | 0 | 96.8% | 106 s | 19 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 84 s | 107 s |
| mistral | 48 | 48 | 0 | 0 | 87.5% | 64 s | 116 min |
| openai | 96 | 95 | 1 | 0 | 77.9% | 98 s | 185 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
