# FILL — the inference availability index

*As of 2026-09-19T10:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 98.3** · FILL·FLEX 97.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=44) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=22) | — |
| MIS·FILL | 95.5% | — | 95.5% (n=22) | — |
| OAI·FILL | 97.7% | 100.0% (n=17) | 93.2% (n=44) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1429 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 783 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 721 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1265 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1255 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 2371 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2041 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1767 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1173 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 956 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1268 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 3741 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 2984 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 780 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 783 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 9200 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 952 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1470 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 66.7% | 33.3% | 5426 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1365 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 75.0% | 25.0% | 3689 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1352 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 740 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 611 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1028 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1218 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1152 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 820 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 96.7% | 0.0% | 913 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 683 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 670 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 88.3% | 0.0% | 1122 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 943 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 858 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 976 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 845 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1061 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1335 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1467 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1647 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1760 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 993 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 745 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1341 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1283 ms |
| deepseek | 100.0% | — | 0.0% | 1136 ms |
| gemini | 100.0% | 87.8% | 6.9% | 943 ms |
| mistral | 100.0% | — | 0.0% | 671 ms |
| openai | 100.0% | 95.6% | 0.0% | 853 ms |
| openrouter | 100.0% | — | 0.0% | 1390 ms |
| xai | 100.0% | — | 0.0% | 748 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 48 | 48 | 0 | 0 | 100.0% | 97 s | 2 min |
| gemini | 24 | 24 | 0 | 0 | 100.0% | 86 s | 114 s |
| mistral | 24 | 24 | 0 | 0 | 95.8% | 32 s | 3 min |
| openai | 48 | 48 | 0 | 0 | 93.8% | 68 s | 58 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
