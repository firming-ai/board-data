# FILL — the inference availability index

*As of 2026-09-18T10:05:00+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 67.7** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 31.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 591 ms |  |
| anthropic/claude-opus-5/standard | 60 | 66.7% | 0.0% | 1044 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1441 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 95.0% | 1.7% | 926 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1216 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | 66.7% | 16.7% | 4251 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | 100.0% | 0.0% | 2867 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 696 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 737 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 5100 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 850 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 0.0% | 93.3% | — ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1270 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 678 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 542 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1170 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 769 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 11.7% | 0.0% | 10647 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1065 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 808 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 845 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 625 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
