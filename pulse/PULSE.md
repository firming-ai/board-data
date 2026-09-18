# FILL — the inference availability index

*As of 2026-09-18T09:05:00+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 67.7** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 31.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 578 ms |  |
| anthropic/claude-opus-5/standard | 60 | 58.3% | 0.0% | 1074 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1238 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 945 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1182 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | 66.7% | 8.3% | 4243 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | 100.0% | 0.0% | 2833 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 734 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 729 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 63.3% | 26.7% | 6721 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 901 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 0.0% | 76.7% | — ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1739 ms |  |
| mistral/mistral-large/standard | 60 | 95.0% | 5.0% | 706 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 536 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1352 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 740 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 8.3% | 0.0% | 9967 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1021 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 860 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 852 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 625 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
