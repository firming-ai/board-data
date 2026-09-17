# FILL — the inference availability index

*As of 2026-09-17T22:05:00+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 80.6** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 31.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 56 | 100.0% | 0.0% | 621 ms |  |
| anthropic/claude-opus-5/standard | 56 | 37.5% | 0.0% | 1338 ms |  |
| anthropic/claude-sonnet-5/standard | 56 | 100.0% | 0.0% | 1175 ms |  |
| deepseek/deepseek-v4-flash/standard | 56 | 100.0% | 0.0% | 864 ms |  |
| deepseek/deepseek-v4-pro/standard | 56 | 100.0% | 0.0% | 1177 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 10 | 100.0% | 0.0% | 3100 ms | ▲ |
| gemini/gemini-3.1-pro-preview/standard | 10 | 100.0% | 0.0% | 2799 ms | ▲ |
| gemini/gemini-3.5-flash-lite/flex | 56 | 100.0% | 0.0% | 763 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 56 | 100.0% | 0.0% | 745 ms |  |
| gemini/gemini-3.5-flash/flex | 56 | 89.3% | 8.9% | 7194 ms |  |
| gemini/gemini-3.5-flash/standard | 56 | 100.0% | 0.0% | 921 ms |  |
| gemini/gemini-3.7-flash/flex | 56 | 50.0% | 33.9% | 33091 ms |  |
| gemini/gemini-3.7-flash/standard | 10 | 100.0% | 0.0% | 1421 ms | ▲ |
| mistral/mistral-large/standard | 56 | 100.0% | 0.0% | 645 ms |  |
| mistral/mistral-small/standard | 56 | 100.0% | 0.0% | 552 ms |  |
| openai/gpt-5.6-luna/flex | 56 | 96.4% | 0.0% | 1168 ms |  |
| openai/gpt-5.6-luna/standard | 56 | 94.6% | 0.0% | 727 ms |  |
| openai/gpt-5.6-sol/flex | 56 | 19.6% | 0.0% | 9927 ms |  |
| openai/gpt-5.6-sol/standard | 56 | 100.0% | 0.0% | 1038 ms |  |
| openai/gpt-5.6-terra/flex | 56 | 94.6% | 0.0% | 843 ms |  |
| openai/gpt-5.6-terra/standard | 56 | 98.2% | 0.0% | 895 ms |  |
| xai/grok-4.20/standard | 49 | 100.0% | 0.0% | 644 ms | ▲ |
| xai/grok-4.6/standard | 2 | 100.0% | 0.0% | 4861 ms | ▲ |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
