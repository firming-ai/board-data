# FILL — the inference availability index

*As of 2026-09-20T02:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 99.0** · FILL·FLEX 97.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 33.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 96.9% | 93.8% (n=16) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1494 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 816 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 708 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 2424 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1371 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1527 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1832 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1057 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1096 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 943 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1211 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 3 | — | — | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 3 | 100.0% | 0.0% | 2942 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 740 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 727 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 93.3% | 6.7% | 4920 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 930 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1589 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 63.3% | 36.7% | 5481 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1218 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 50.0% | 50.0% | 4093 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1096 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 687 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 586 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1091 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 939 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1089 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 757 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 999 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 649 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 761 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 88.3% | 0.0% | 1074 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1001 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 764 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 870 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 764 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1253 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1194 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1352 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1438 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1506 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 951 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 737 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1509 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1143 ms |
| deepseek | 100.0% | — | 0.0% | 1111 ms |
| gemini | 100.0% | 83.3% | 9.4% | 858 ms |
| mistral | 100.0% | — | 0.0% | 627 ms |
| openai | 100.0% | 96.6% | 0.0% | 852 ms |
| openrouter | 100.0% | — | 0.0% | 1343 ms |
| xai | 100.0% | — | 0.0% | 740 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 89 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 116 s |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 34 s | 10 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 67 s | 24 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
