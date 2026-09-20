# FILL — the inference availability index

*As of 2026-09-20T21:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 95.4** · FILL·FLEX 82.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 92.2% | 76.5% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1444 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 813 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 706 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1192 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1180 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1429 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2053 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1781 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1050 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 897 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1240 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 3398 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2428 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 746 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 783 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 4381 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 897 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1618 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 61.7% | 38.3% | 3616 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1299 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 58.3% | 41.7% | 2371 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1346 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 693 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 593 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1044 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 985 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1017 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 792 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1061 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 653 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 781 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 81.7% | 0.0% | 1384 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 960 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 758 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 960 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 796 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1278 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1228 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1641 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1518 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1638 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 930 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 694 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1283 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1228 ms |
| deepseek | 100.0% | — | 0.0% | 1089 ms |
| gemini | 100.0% | 85.6% | 8.1% | 886 ms |
| mistral | 100.0% | — | 0.0% | 647 ms |
| openai | 100.0% | 94.6% | 0.0% | 870 ms |
| openrouter | 100.0% | — | 0.0% | 1393 ms |
| xai | 100.0% | — | 0.0% | 707 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 80 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 108 s |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 30 s | 211 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 68 s | 14 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
