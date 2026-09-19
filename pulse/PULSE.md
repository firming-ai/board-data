# FILL — the inference availability index

*As of 2026-09-19T23:05:02+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 93.9** · FILL·FLEX 78.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 33.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 90.6% | 81.2% (n=16) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 91.1% | 76.5% (n=17) | 96.9% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1527 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 908 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 742 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1401 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1152 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1687 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1725 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1053 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1080 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 945 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1273 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 3572 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 2371 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 774 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 1418 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 935 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1824 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 50.0% | 50.0% | 3324 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1118 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 2310 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1109 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 690 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 610 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 951 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1109 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1089 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 840 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 989 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 662 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 710 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 83.3% | 0.0% | 1138 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 934 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 813 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 966 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 831 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1019 ms |  |
| openai/gpt-6-astra/flex | 12 | 66.7% | 0.0% | 1301 ms |  |
| openai/gpt-6-astra/standard | 12 | 75.0% | 0.0% | 1415 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1407 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1708 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 987 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 713 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1250 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1050 ms |
| deepseek | 100.0% | — | 0.0% | 1100 ms |
| gemini | 100.0% | 83.7% | 9.2% | 890 ms |
| mistral | 100.0% | — | 0.0% | 659 ms |
| openai | 98.6% | 93.1% | 0.0% | 857 ms |
| openrouter | 100.0% | — | 0.0% | 1346 ms |
| xai | 100.0% | — | 0.0% | 723 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 95 | 1 | 0 | 100.0% | 92 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 116 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 34 s | 10 min |
| openai | 96 | 95 | 1 | 0 | 97.9% | 67 s | 31 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
