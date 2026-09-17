# FILL — the inference availability index

*As of 2026-09-17T23:05:01+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 93.5** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 31.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 657 ms |  |
| anthropic/claude-opus-5/standard | 60 | 35.0% | 0.0% | 1017 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1019 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 958 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1230 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | 91.7% | 8.3% | 4541 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | 100.0% | 0.0% | 2788 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 707 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 726 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 93.3% | 6.7% | 7563 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 921 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 81.7% | 18.3% | 6021 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1421 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 670 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 533 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1143 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 682 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 60.0% | 0.0% | 1268 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1009 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 989 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 879 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 632 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
