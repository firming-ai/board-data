# FILL — the inference availability index

*As of 2026-09-20T08:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 97.1** · FILL·FLEX 91.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1438 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 804 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 713 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1296 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1233 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1937 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1914 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1644 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1109 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1040 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1243 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 4661 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3050 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 742 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 740 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 93.3% | 6.7% | 7563 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 951 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1722 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 63.3% | 35.0% | 4142 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1580 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 91.7% | 8.3% | 3131 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1250 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 690 ms |  |
| mistral/mistral-small/standard | 60 | 85.0% | 15.0% | 609 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1192 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 972 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1067 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 758 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 90.0% | 0.0% | 1268 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 672 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 766 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 81.7% | 0.0% | 1429 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 956 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 816 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 890 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 764 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1447 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1218 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1577 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1509 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1806 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 939 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 727 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1476 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1250 ms |
| deepseek | 100.0% | — | 0.0% | 1138 ms |
| gemini | 100.0% | 86.1% | 7.6% | 921 ms |
| mistral | 92.5% | — | 7.5% | 655 ms |
| openai | 100.0% | 91.7% | 0.0% | 850 ms |
| openrouter | 100.0% | — | 0.0% | 1382 ms |
| xai | 100.0% | — | 0.0% | 733 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 86 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 113 s |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 32 s | 15 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 67 s | 13 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
