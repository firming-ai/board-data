# FILL — the inference availability index

*As of 2026-09-22T12:05:03+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 89.9** · FILL·FLEX 79.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.9% | — | 95.8% (n=96) | 100.0% (n=30) |
| GEM·FILL | 79.4% | 58.8% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 95.8% | — | 95.8% (n=48) | — |
| OAI·FILL | 92.4% | 100.0% (n=17) | 77.1% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1555 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 930 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 813 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1491 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1127 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1612 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2419 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 2045 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1076 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1040 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1395 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 4708 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3143 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 877 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 843 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 91.7% | 1.7% | 8209 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 951 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 2028 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 56.7% | 41.7% | 5855 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1275 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 66.7% | 33.3% | 3925 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1589 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 830 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 649 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1304 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1036 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1140 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1050 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1304 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 841 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 867 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1005 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1102 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 924 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1127 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1082 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1275 ms |  |
| openai/gpt-6-astra/flex | 12 | 83.3% | 0.0% | 1739 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 2124 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1850 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1701 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1184 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 758 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1373 ms |  |
| xai/grok-4.7/standard | 12 | 100.0% | 0.0% | 2158 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1360 ms |
| deepseek | 100.0% | — | 0.0% | 1168 ms |
| gemini | 100.0% | 82.0% | 8.7% | 934 ms |
| mistral | 100.0% | — | 0.0% | 724 ms |
| openai | 100.0% | 99.0% | 0.0% | 1034 ms |
| openrouter | 100.0% | — | 0.0% | 1580 ms |
| xai | 100.0% | — | 0.0% | 804 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 93 | 3 | 0 | 96.8% | 110 s | 30 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 84 s | 112 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 42 s | 18 min |
| openai | 96 | 95 | 1 | 0 | 76.8% | 112 s | 185 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
