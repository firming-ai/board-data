# FILL — the inference availability index

*As of 2026-09-19T05:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 95.5** · FILL·FLEX 90.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 33.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=24) | 100.0% (n=30) |
| GEM·FILL | 90.6% | 81.2% (n=16) | 100.0% (n=12) | — |
| MIS·FILL | 91.7% | — | 91.7% (n=12) | — |
| OAI·FILL | 95.8% | 100.0% (n=17) | 87.5% (n=24) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1482 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 813 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 706 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1194 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1017 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 2678 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1785 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 985 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1127 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 985 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1291 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | — | — | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 2749 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 754 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 730 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 95.0% | 5.0% | 5636 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 932 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1589 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 68.3% | 30.0% | 4286 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1368 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 4118 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1161 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 686 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 580 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1089 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1168 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1149 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 836 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 98.3% | 0.0% | 1044 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 672 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 655 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 98.3% | 0.0% | 1265 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1009 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 807 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 935 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 877 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1028 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 1204 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1418 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1376 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1583 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 934 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 730 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1382 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 949 ms |
| deepseek | 100.0% | — | 0.0% | 1109 ms |
| gemini | 100.0% | 87.5% | 6.7% | 893 ms |
| mistral | 100.0% | — | 0.0% | 630 ms |
| openai | 99.5% | 98.5% | 0.0% | 906 ms |
| openrouter | 100.0% | — | 0.0% | 1296 ms |
| xai | 100.0% | — | 0.0% | 740 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 28 | 28 | 0 | 0 | 100.0% | 82 s | 2 min |
| gemini | 14 | 14 | 0 | 0 | 100.0% | 88 s | 118 s |
| mistral | 14 | 14 | 0 | 0 | 92.9% | 40 s | 30 min |
| openai | 28 | 28 | 0 | 0 | 89.3% | 68 s | 72 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
