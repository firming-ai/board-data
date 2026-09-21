# FILL — the inference availability index

*As of 2026-09-21T16:05:03+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 89.7** · FILL·FLEX 64.7

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 72.9% | — | 72.9% (n=48) | — |
| OAI·FILL | 86.8% | 64.7% (n=17) | 95.8% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1661 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 870 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 696 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1407 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1278 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 3081 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2128 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1770 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1129 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 972 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1230 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 50.0% | 50.0% | 6601 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3616 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 90.0% | 1.7% | 4478 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 934 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 35.0% | 56.7% | 18380 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1028 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 2347 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 8.3% | 71.7% | 24367 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 2137 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 16.7% | 83.3% | 8193 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 2065 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 884 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 638 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1346 ms |  |
| openai/gpt-5.5/flex | 12 | 91.7% | 0.0% | 1527 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1447 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1113 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 53.3% | 0.0% | 10047 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 881 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 1080 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 8.3% | 0.0% | 8857 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1899 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 1080 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1365 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1216 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1548 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 10168 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1824 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1527 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1698 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1304 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 777 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1828 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1322 ms |
| deepseek | 100.0% | — | 0.0% | 1078 ms |
| gemini | 100.0% | 42.8% | 25.9% | 1055 ms |
| mistral | 100.0% | — | 0.0% | 737 ms |
| openai | 100.0% | 58.8% | 0.0% | 1296 ms |
| openrouter | 100.0% | — | 0.0% | 1455 ms |
| xai | 100.0% | — | 0.0% | 792 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 85 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 82 s | 106 s |
| mistral | 48 | 48 | 0 | 0 | 75.0% | 38 s | 190 min |
| openai | 96 | 94 | 2 | 0 | 95.7% | 69 s | 47 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
