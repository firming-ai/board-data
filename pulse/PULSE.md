# FILL — the inference availability index

*As of 2026-09-20T20:05:02+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 92.8** · FILL·FLEX 73.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 85.4% | — | 85.4% (n=48) | — |
| OAI·FILL | 90.2% | 70.6% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1545 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 893 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 733 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1240 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1159 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1558 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1926 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1735 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1072 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 937 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1220 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 2884 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3026 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 789 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 772 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 6509 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 921 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1509 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 55.0% | 45.0% | 3481 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1497 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 3948 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1306 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 687 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 609 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 876 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 964 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1001 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 757 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 98.3% | 0.0% | 1102 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 649 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 767 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 73.3% | 0.0% | 2032 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 913 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 96.7% | 0.0% | 690 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 858 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1100 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1228 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1384 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1452 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1599 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 999 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 716 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1243 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1230 ms |
| deepseek | 100.0% | — | 0.0% | 1091 ms |
| gemini | 100.0% | 85.0% | 8.4% | 899 ms |
| mistral | 100.0% | — | 0.0% | 644 ms |
| openai | 99.5% | 90.7% | 0.0% | 835 ms |
| openrouter | 100.0% | — | 0.0% | 1393 ms |
| xai | 100.0% | — | 0.0% | 718 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 78 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 82 s | 108 s |
| mistral | 48 | 39 | 9 | 0 | 100.0% | 22 s | 3 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 68 s | 14 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
