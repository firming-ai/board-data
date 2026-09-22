# FILL — the inference availability index

*As of 2026-09-22T01:05:02+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 97.3** · FILL·FLEX 97.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 87.5% | — | 87.5% (n=48) | — |
| OAI·FILL | 94.8% | 100.0% (n=17) | 84.4% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 91.7% | 8.3% | 1677 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 890 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 2128 ms |  |
| anthropic/claude-opus-5/standard | 60 | 98.3% | 1.7% | 1304 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1992 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1435 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1260 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1283 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1098 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1270 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 22226 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3718 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 836 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 804 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 0.0% | 11533 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1007 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1715 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 70.0% | 30.0% | 3050 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1317 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 100.0% | 0.0% | 2733 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1467 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 720 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 644 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1109 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1015 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1040 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 945 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 98.3% | 0.0% | 1352 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 838 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 737 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 91.7% | 0.0% | 1238 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 98.3% | 0.0% | 1070 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 860 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1184 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1024 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1349 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1464 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1781 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1573 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1828 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1159 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 781 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1647 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 99.0% | — | 1.0% | 1211 ms |
| deepseek | 100.0% | — | 0.0% | 1180 ms |
| gemini | 100.0% | 90.2% | 5.2% | 964 ms |
| mistral | 100.0% | — | 0.0% | 694 ms |
| openai | 99.5% | 97.1% | 0.0% | 981 ms |
| openrouter | 100.0% | — | 0.0% | 1518 ms |
| xai | 100.0% | — | 0.0% | 784 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 98 s | 4 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 76 s | 107 s |
| mistral | 48 | 48 | 0 | 0 | 87.5% | 56 s | 116 min |
| openai | 96 | 94 | 2 | 0 | 85.1% | 82 s | 185 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
