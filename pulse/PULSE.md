# FILL — the inference availability index

*As of 2026-09-20T15:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 95.1** · FILL·FLEX 85.3

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 85.3% | 70.6% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1476 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 810 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 711 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 2448 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1189 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1506 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1996 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1788 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1182 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 968 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1250 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 5182 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3226 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 792 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 799 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 7856 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 911 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1774 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 60.0% | 40.0% | 3980 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1371 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 3763 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1357 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 686 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 587 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 884 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1007 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1206 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 774 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1007 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 692 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 763 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 86.7% | 0.0% | 1201 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 932 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 780 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 865 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 826 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1273 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1250 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1542 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1567 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1570 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 974 ms |  |
| xai/grok-4.20/standard | 60 | 93.3% | 0.0% | 731 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1491 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1260 ms |
| deepseek | 100.0% | — | 0.0% | 1087 ms |
| gemini | 100.0% | 86.1% | 7.8% | 902 ms |
| mistral | 100.0% | — | 0.0% | 649 ms |
| openai | 99.5% | 96.1% | 0.0% | 864 ms |
| openrouter | 100.0% | — | 0.0% | 1346 ms |
| xai | 93.8% | — | 0.0% | 754 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 83 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 75 s | 108 s |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 25 s | 15 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 68 s | 9 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
