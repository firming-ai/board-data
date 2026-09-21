# FILL — the inference availability index

*As of 2026-09-21T05:05:02+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 92.0** · FILL·FLEX 70.6

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 84.9% | 58.8% (n=17) | 95.8% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1518 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 770 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 734 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1482 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1260 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1479 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1957 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1792 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1091 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 954 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1220 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 50.0% | 50.0% | 3502 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3118 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 98.3% | 1.7% | 764 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 740 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 1113 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 968 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1701 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 70.0% | 30.0% | 2738 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1338 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 2984 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1175 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 679 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 575 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1019 ms |  |
| openai/gpt-5.5/flex | 12 | 66.7% | 0.0% | 6445 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1208 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 924 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1030 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 638 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 775 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 68.3% | 0.0% | 1258 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 989 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 767 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 991 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 812 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1168 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 1832 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1854 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1552 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1742 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1009 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 716 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1521 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1335 ms |
| deepseek | 100.0% | — | 0.0% | 1089 ms |
| gemini | 100.0% | 88.7% | 6.4% | 926 ms |
| mistral | 100.0% | — | 0.0% | 635 ms |
| openai | 100.0% | 88.2% | 0.0% | 879 ms |
| openrouter | 100.0% | — | 0.0% | 1452 ms |
| xai | 100.0% | — | 0.0% | 721 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 78 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 75 s | 107 s |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 27 s | 211 min |
| openai | 96 | 95 | 1 | 0 | 96.8% | 68 s | 34 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
