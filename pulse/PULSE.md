# FILL — the inference availability index

*As of 2026-09-20T01:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 96.9** · FILL·FLEX 90.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 33.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 90.6% | 81.2% (n=16) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1404 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 901 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 706 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1455 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1360 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1835 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1749 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1011 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1053 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 949 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1122 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | — | — | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 2890 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 754 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 733 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 3412 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 98.3% | 1.7% | 928 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1599 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 58.3% | 41.7% | 3252 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1240 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 91.7% | 8.3% | 6562 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1213 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 699 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 596 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 952 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 976 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 995 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 748 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 913 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 645 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 736 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 88.3% | 0.0% | 970 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 947 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 751 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 877 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 730 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1156 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1427 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1349 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1444 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1763 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 976 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 731 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1506 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1048 ms |
| deepseek | 100.0% | — | 0.0% | 1040 ms |
| gemini | 99.3% | 85.9% | 8.2% | 901 ms |
| mistral | 100.0% | — | 0.0% | 644 ms |
| openai | 100.0% | 96.6% | 0.0% | 802 ms |
| openrouter | 100.0% | — | 0.0% | 1346 ms |
| xai | 100.0% | — | 0.0% | 743 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 89 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 116 s |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 34 s | 10 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 67 s | 24 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
