# FILL — the inference availability index

*As of 2026-09-18T06:05:00+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 86.7** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 30.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 630 ms |  |
| anthropic/claude-opus-5/standard | 60 | 65.0% | 0.0% | 1113 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1133 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1034 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1213 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | — | — | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | — | — | — ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 731 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 758 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 2777 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 852 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 65.0% | 35.0% | 6368 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1243 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 637 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 541 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1063 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 823 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 33.3% | 0.0% | 1491 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1175 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 820 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 807 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 654 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
