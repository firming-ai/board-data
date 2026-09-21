# FILL — the inference availability index

*As of 2026-09-21T12:05:02+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 91.4** · FILL·FLEX 70.6

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 85.3% | 70.6% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 75.0% | — | 75.0% (n=48) | — |
| OAI·FILL | 88.8% | 70.6% (n=17) | 95.8% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1545 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 886 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 791 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1494 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1243 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 2477 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2012 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1722 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1154 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1050 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1333 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 5151 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3175 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 869 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 813 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 96.7% | 3.3% | 7578 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 987 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1846 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 58.3% | 33.3% | 17137 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1732 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 91.7% | 8.3% | 4085 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1491 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 472 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 630 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1115 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1583 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1131 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1032 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1143 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 736 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 831 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 8.3% | 0.0% | 11956 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1265 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 781 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1096 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 945 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1421 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 2810 ms |  |
| openai/gpt-6-astra/standard | 12 | 75.0% | 0.0% | 1621 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1536 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1785 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1240 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 767 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1972 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1312 ms |
| deepseek | 100.0% | — | 0.0% | 1168 ms |
| gemini | 100.0% | 85.6% | 6.7% | 949 ms |
| mistral | 100.0% | — | 0.0% | 592 ms |
| openai | 98.6% | 73.0% | 0.0% | 1026 ms |
| openrouter | 100.0% | — | 0.0% | 1494 ms |
| xai | 100.0% | — | 0.0% | 770 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 81 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 75 s | 106 s |
| mistral | 48 | 42 | 6 | 0 | 81.0% | 36 s | 221 min |
| openai | 96 | 96 | 0 | 0 | 95.8% | 69 s | 41 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
