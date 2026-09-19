# FILL — the inference availability index

*As of 2026-09-19T18:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 95.6** · FILL·FLEX 88.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=76) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=38) | — |
| MIS·FILL | 97.4% | — | 97.4% (n=38) | — |
| OAI·FILL | 98.7% | 100.0% (n=17) | 96.0% (n=76) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1872 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 831 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 723 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1296 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1177 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1384 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2103 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1803 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1067 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 981 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1265 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 3824 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 2827 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 792 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 791 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 88.3% | 11.7% | 10087 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 989 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1615 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 61.7% | 36.7% | 3689 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1524 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 2625 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1387 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 736 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 637 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 932 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1154 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1080 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 893 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1250 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 751 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 726 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1265 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 913 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 804 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 976 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 840 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1011 ms |  |
| openai/gpt-6-astra/flex | 12 | 83.3% | 0.0% | 1638 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1387 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1467 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1667 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1042 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 761 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 2424 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1228 ms |
| deepseek | 100.0% | — | 0.0% | 1127 ms |
| gemini | 100.0% | 83.7% | 8.9% | 964 ms |
| mistral | 100.0% | — | 0.0% | 687 ms |
| openai | 99.5% | 99.0% | 0.0% | 857 ms |
| openrouter | 100.0% | — | 0.0% | 1373 ms |
| xai | 100.0% | — | 0.0% | 767 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 80 | 80 | 0 | 0 | 100.0% | 94 s | 2 min |
| gemini | 40 | 40 | 0 | 0 | 100.0% | 82 s | 116 s |
| mistral | 40 | 38 | 2 | 0 | 97.4% | 35 s | 4 min |
| openai | 80 | 80 | 0 | 0 | 96.3% | 67 s | 44 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
