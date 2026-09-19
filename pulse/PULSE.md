# FILL — the inference availability index

*As of 2026-09-19T04:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 96.3** · FILL·FLEX 93.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 33.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=20) | 100.0% (n=30) |
| GEM·FILL | 93.8% | 87.5% (n=16) | 100.0% (n=10) | — |
| MIS·FILL | 90.0% | — | 90.0% (n=10) | — |
| OAI·FILL | 95.0% | 100.0% (n=17) | 85.0% (n=20) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1704 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 800 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 700 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1156 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1113 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1441 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1795 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1063 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1074 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 991 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1218 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | — | — | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | — | — | — ms |  |
| gemini/gemini-3.5-flash-lite/cache | 1 | 100.0% | 0.0% | 1260 ms | ▲ |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 748 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 731 ms |  |
| gemini/gemini-3.5-flash/cache | 1 | 0.0% | 100.0% | — ms | ▲ |
| gemini/gemini-3.5-flash/flex | 60 | 96.7% | 3.3% | 5547 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 926 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1354 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 65.0% | 33.3% | 6204 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1268 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 100.0% | 0.0% | 3291 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1124 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 685 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 582 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 864 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1026 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1089 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 852 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 91.7% | 0.0% | 981 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 650 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 675 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 995 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 966 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 755 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1059 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 807 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1017 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1253 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1515 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1438 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1580 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 897 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 708 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1161 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1007 ms |
| deepseek | 100.0% | — | 0.0% | 1091 ms |
| gemini | 100.0% | 88.0% | 6.5% | 888 ms |
| mistral | 100.0% | — | 0.0% | 632 ms |
| openai | 99.5% | 97.5% | 0.0% | 858 ms |
| openrouter | 100.0% | — | 0.0% | 1362 ms |
| xai | 100.0% | — | 0.0% | 718 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 24 | 24 | 0 | 0 | 100.0% | 84 s | 2 min |
| gemini | 12 | 12 | 0 | 0 | 100.0% | 81 s | 105 s |
| mistral | 12 | 12 | 0 | 0 | 91.7% | 46 s | 38 min |
| openai | 24 | 24 | 0 | 0 | 87.5% | 68 s | 76 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
