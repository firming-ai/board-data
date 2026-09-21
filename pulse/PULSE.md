# FILL — the inference availability index

*As of 2026-09-21T00:05:02+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 92.6** · FILL·FLEX 76.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 89.6% | 76.5% (n=17) | 99.0% (n=96) | 93.3% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1398 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 751 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 730 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1275 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1163 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1631 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1961 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1694 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 924 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 890 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1213 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 50.0% | 0.0% | 66238 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3194 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 745 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 697 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 0.0% | 6654 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 904 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1612 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 71.7% | 28.3% | 2385 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1218 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 2695 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1192 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 649 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 555 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 937 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 908 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 991 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 734 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 3014 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 631 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 748 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 66.7% | 0.0% | 2482 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 951 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 745 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 804 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 729 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1098 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1177 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1260 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1464 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1749 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 999 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 720 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1291 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1245 ms |
| deepseek | 100.0% | — | 0.0% | 1017 ms |
| gemini | 100.0% | 89.2% | 5.5% | 864 ms |
| mistral | 100.0% | — | 0.0% | 612 ms |
| openai | 99.5% | 90.2% | 0.0% | 830 ms |
| openrouter | 100.0% | — | 0.0% | 1368 ms |
| xai | 100.0% | — | 0.0% | 727 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 78 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 108 s |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 30 s | 211 min |
| openai | 96 | 94 | 2 | 0 | 100.0% | 68 s | 13 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
