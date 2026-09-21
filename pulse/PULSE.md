# FILL — the inference availability index

*As of 2026-09-21T02:05:02+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 96.0** · FILL·FLEX 85.3

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 93.8% | 82.3% (n=17) | 99.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1376 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 796 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 740 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1265 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1238 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1929 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2020 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1704 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1098 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1001 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1194 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 18939 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3318 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 73.3% | 8.3% | 1996 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 775 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 5670 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 949 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1677 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 55.0% | 45.0% | 2925 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1338 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 66.7% | 33.3% | 2793 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1545 ms |  |
| mistral/mistral-large/standard | 60 | 98.3% | 1.7% | 657 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 559 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 951 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1078 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1074 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 935 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1072 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 653 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 723 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 65.0% | 0.0% | 1213 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 921 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 726 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 956 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 791 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1124 ms |  |
| openai/gpt-6-astra/flex | 12 | 83.3% | 0.0% | 1263 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1545 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1548 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1899 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 98.3% | 0.0% | 985 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 681 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1521 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1250 ms |
| deepseek | 100.0% | — | 0.0% | 1089 ms |
| gemini | 100.0% | 75.8% | 10.5% | 939 ms |
| mistral | 99.2% | — | 0.8% | 625 ms |
| openai | 100.0% | 88.7% | 0.0% | 850 ms |
| openrouter | 99.4% | — | 0.0% | 1479 ms |
| xai | 100.0% | — | 0.0% | 685 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 80 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 82 s | 107 s |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 24 s | 211 min |
| openai | 96 | 95 | 1 | 0 | 98.9% | 68 s | 27 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
