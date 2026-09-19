# FILL — the inference availability index

*As of 2026-09-19T07:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 95.0** · FILL·FLEX 85.3

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=32) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=16) | — |
| MIS·FILL | 93.8% | — | 93.8% (n=16) | — |
| OAI·FILL | 91.0% | 82.3% (n=17) | 90.6% (n=32) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1376 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 820 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 713 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1452 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1147 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1461 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1996 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1698 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1189 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 960 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1278 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | — | — | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | — | — | — ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 784 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 763 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 96.7% | 3.3% | 4900 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 924 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1545 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 55.0% | 45.0% | 4416 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1283 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 66.7% | 33.3% | 4134 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1240 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 679 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 571 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 952 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1218 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1161 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 812 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 96.7% | 0.0% | 1421 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 668 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 692 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 81.7% | 0.0% | 1032 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1124 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 836 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 979 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 850 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1156 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1976 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1438 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1452 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1763 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 941 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 755 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1491 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1223 ms |
| deepseek | 100.0% | — | 0.0% | 1133 ms |
| gemini | 100.0% | 82.8% | 9.7% | 910 ms |
| mistral | 100.0% | — | 0.0% | 640 ms |
| openai | 100.0% | 93.6% | 0.0% | 919 ms |
| openrouter | 100.0% | — | 0.0% | 1357 ms |
| xai | 100.0% | — | 0.0% | 770 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 36 | 36 | 0 | 0 | 100.0% | 96 s | 3 min |
| gemini | 18 | 18 | 0 | 0 | 100.0% | 86 s | 117 s |
| mistral | 18 | 18 | 0 | 0 | 94.4% | 34 s | 15 min |
| openai | 36 | 35 | 1 | 0 | 91.4% | 68 s | 66 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
