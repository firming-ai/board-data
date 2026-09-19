# FILL — the inference availability index

*As of 2026-09-19T20:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 96.7** · FILL·FLEX 91.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=84) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=42) | — |
| MIS·FILL | 97.6% | — | 97.6% (n=42) | — |
| OAI·FILL | 98.8% | 100.0% (n=17) | 96.4% (n=84) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1527 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 815 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 729 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1255 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1180 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1684 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2145 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1806 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1087 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 981 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1248 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 3232 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 3265 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 769 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 781 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 95.0% | 5.0% | 11126 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 937 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1711 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 68.3% | 31.7% | 3291 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1384 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 4126 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1312 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 721 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 612 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1076 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1180 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1199 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 843 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 96.7% | 0.0% | 852 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 736 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 711 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1152 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 991 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 820 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 979 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 841 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1173 ms |  |
| openai/gpt-6-astra/flex | 12 | 58.3% | 0.0% | 1304 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1410 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1612 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1651 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 978 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 748 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1288 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1255 ms |
| deepseek | 100.0% | — | 0.0% | 1120 ms |
| gemini | 100.0% | 87.8% | 6.9% | 908 ms |
| mistral | 100.0% | — | 0.0% | 681 ms |
| openai | 99.5% | 96.6% | 0.0% | 883 ms |
| openrouter | 100.0% | — | 0.0% | 1455 ms |
| xai | 100.0% | — | 0.0% | 757 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 88 | 87 | 1 | 0 | 100.0% | 94 s | 2 min |
| gemini | 44 | 44 | 0 | 0 | 100.0% | 85 s | 116 s |
| mistral | 44 | 44 | 0 | 0 | 97.7% | 37 s | 12 min |
| openai | 88 | 88 | 0 | 0 | 96.6% | 68 s | 41 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
