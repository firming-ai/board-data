# FILL — the inference availability index

*As of 2026-09-22T18:05:01+00:00 · probe pulse-1.2.4 · methodology 1.2.0*

**FILL 87.9** · FILL·FLEX 76.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.4% | — | 94.8% (n=96) | 100.0% (n=30) |
| GEM·FILL | 76.5% | 52.9% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 89.9% | 100.0% (n=17) | 69.8% (n=96) | 100.0% (n=11) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 11 | 100.0% | 0.0% | 1647 ms |  |
| anthropic/claude-haiku-4-5/cache | 14 | 100.0% | 0.0% | 812 ms |  |
| anthropic/claude-haiku-4-5/standard | 59 | 100.0% | 0.0% | 737 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 2573 ms |  |
| anthropic/claude-opus-5/standard | 59 | 100.0% | 0.0% | 1175 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1674 ms |  |
| anthropic/claude-sonnet-5/cache | 14 | 100.0% | 0.0% | 2424 ms |  |
| anthropic/claude-sonnet-5/standard | 59 | 100.0% | 0.0% | 1432 ms |  |
| deepseek/deepseek-flash/standard | 11 | 100.0% | 0.0% | 1138 ms |  |
| deepseek/deepseek-v4-flash/standard | 59 | 100.0% | 0.0% | 960 ms |  |
| deepseek/deepseek-v4-pro/standard | 59 | 100.0% | 0.0% | 1230 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 0.0% | 100.0% | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3156 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 59 | 50.9% | 32.2% | 33692 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 59 | 100.0% | 0.0% | 937 ms |  |
| gemini/gemini-3.5-flash/flex | 59 | 72.9% | 20.3% | 4670 ms |  |
| gemini/gemini-3.5-flash/standard | 59 | 100.0% | 0.0% | 1007 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1933 ms |  |
| gemini/gemini-3.7-flash/flex | 59 | 0.0% | 100.0% | — ms |  |
| gemini/gemini-3.7-flash/standard | 11 | 100.0% | 0.0% | 1806 ms |  |
| gemini/gemini-3.8-flash/flex | 11 | 0.0% | 100.0% | — ms |  |
| gemini/gemini-3.8-flash/standard | 11 | 100.0% | 0.0% | 1213 ms |  |
| mistral/mistral-large/standard | 59 | 100.0% | 0.0% | 706 ms |  |
| mistral/mistral-small/standard | 59 | 100.0% | 0.0% | 606 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1163 ms |  |
| openai/gpt-5.5/flex | 11 | 100.0% | 0.0% | 1173 ms |  |
| openai/gpt-5.5/standard | 11 | 100.0% | 0.0% | 1253 ms |  |
| openai/gpt-5.6-luna/cache | 14 | 100.0% | 0.0% | 1038 ms |  |
| openai/gpt-5.6-luna/flex | 59 | 100.0% | 0.0% | 1288 ms |  |
| openai/gpt-5.6-luna/priority | 59 | 100.0% | 0.0% | 860 ms |  |
| openai/gpt-5.6-luna/standard | 59 | 100.0% | 0.0% | 845 ms |  |
| openai/gpt-5.6-sol/flex | 59 | 100.0% | 0.0% | 2086 ms |  |
| openai/gpt-5.6-sol/standard | 59 | 100.0% | 0.0% | 1076 ms |  |
| openai/gpt-5.6-terra/flex | 59 | 97.7% | 0.0% | 932 ms |  |
| openai/gpt-5.6-terra/priority | 11 | 100.0% | 0.0% | 1235 ms |  |
| openai/gpt-5.6-terra/standard | 59 | 100.0% | 0.0% | 1100 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1605 ms |  |
| openai/gpt-6-astra/flex | 11 | 100.0% | 0.0% | 1296 ms |  |
| openai/gpt-6-astra/standard | 11 | 100.0% | 0.0% | 2497 ms |  |
| openrouter/claude-sonnet-5/standard | 59 | 100.0% | 0.0% | 1687 ms |  |
| openrouter/gemini-3.7-flash/standard | 59 | 100.0% | 0.0% | 1806 ms |  |
| openrouter/gpt-5.6-terra/standard | 59 | 100.0% | 0.0% | 1263 ms |  |
| xai/grok-4.20/standard | 59 | 100.0% | 0.0% | 694 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1742 ms |  |
| xai/grok-4.7/standard | 11 | 100.0% | 0.0% | 2357 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1216 ms |
| deepseek | 100.0% | — | 0.0% | 1140 ms |
| gemini | 100.0% | 38.4% | 30.6% | 1021 ms |
| mistral | 100.0% | — | 0.0% | 657 ms |
| openai | 100.0% | 99.3% | 0.0% | 1053 ms |
| openrouter | 100.0% | — | 0.0% | 1589 ms |
| xai | 100.0% | — | 0.0% | 751 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 94.8% | 118 s | 55 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 80 s | 115 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 44 s | 24 min |
| openai | 96 | 85 | 1 | 10 | 71.6% | 110 s | 138 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
