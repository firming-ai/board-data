# FILL — the inference availability index

*As of 2026-09-19T16:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 96.6** · FILL·FLEX 91.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=68) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=34) | — |
| MIS·FILL | 97.1% | — | 97.1% (n=34) | — |
| OAI·FILL | 98.5% | 100.0% (n=17) | 95.6% (n=68) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1625 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 845 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 764 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1577 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1170 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 2296 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2016 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1839 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1312 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1102 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1327 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 3002 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 3304 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 98.3% | 1.7% | 852 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 845 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 91.7% | 8.3% | 7533 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1015 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1792 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 58.3% | 41.7% | 5131 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1319 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 58.3% | 41.7% | 4469 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1301 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 757 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 640 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 968 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1240 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1113 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 981 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1074 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 742 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 729 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 93.3% | 0.0% | 1175 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1046 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 846 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1030 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 853 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1149 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1265 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1464 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1634 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1872 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1038 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 761 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1631 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1260 ms |
| deepseek | 100.0% | — | 0.0% | 1230 ms |
| gemini | 100.0% | 81.6% | 10.3% | 983 ms |
| mistral | 100.0% | — | 0.0% | 716 ms |
| openai | 99.5% | 98.0% | 0.0% | 901 ms |
| openrouter | 100.0% | — | 0.0% | 1452 ms |
| xai | 100.0% | — | 0.0% | 763 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 72 | 72 | 0 | 0 | 100.0% | 92 s | 2 min |
| gemini | 36 | 36 | 0 | 0 | 100.0% | 85 s | 116 s |
| mistral | 36 | 36 | 0 | 0 | 97.2% | 35 s | 4 min |
| openai | 72 | 72 | 0 | 0 | 95.8% | 67 s | 48 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
