# FILL — the inference availability index

*As of 2026-09-19T06:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 97.1** · FILL·FLEX 93.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 33.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=28) | 100.0% (n=30) |
| GEM·FILL | 96.9% | 93.8% (n=16) | 100.0% (n=14) | — |
| MIS·FILL | 92.9% | — | 92.9% (n=14) | — |
| OAI·FILL | 94.5% | 94.1% (n=17) | 89.3% (n=28) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1235 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 858 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 677 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1175 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1013 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1255 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1824 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1201 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1201 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 985 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1250 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | — | — | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 2850 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 754 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 720 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 5383 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 939 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1491 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 48.3% | 51.7% | 4159 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1401 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 4277 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1159 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 670 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 580 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 915 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1140 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1098 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 764 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 970 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 636 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 654 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 98.3% | 0.0% | 1046 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 949 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 794 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 939 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 897 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1238 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1245 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1404 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1435 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1681 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 983 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 729 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1317 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 985 ms |
| deepseek | 100.0% | — | 0.0% | 1147 ms |
| gemini | 100.0% | 82.3% | 10.0% | 908 ms |
| mistral | 100.0% | — | 0.0% | 620 ms |
| openai | 100.0% | 99.5% | 0.0% | 884 ms |
| openrouter | 100.0% | — | 0.0% | 1330 ms |
| xai | 100.0% | — | 0.0% | 737 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 32 | 32 | 0 | 0 | 100.0% | 90 s | 2 min |
| gemini | 16 | 16 | 0 | 0 | 100.0% | 86 s | 117 s |
| mistral | 16 | 16 | 0 | 0 | 93.8% | 37 s | 22 min |
| openai | 32 | 32 | 0 | 0 | 90.6% | 68 s | 69 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
