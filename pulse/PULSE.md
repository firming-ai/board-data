# FILL — the inference availability index

*As of 2026-09-18T04:05:00+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 83.3** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 30.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 646 ms |  |
| anthropic/claude-opus-5/standard | 60 | 68.3% | 0.0% | 1120 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1040 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 979 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1233 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | — | — | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | — | — | — ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 783 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 754 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 96.7% | 3.3% | 7310 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 876 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 80.0% | 20.0% | 4642 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 91.7% | 8.3% | 1180 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 617 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 551 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 95.0% | 0.0% | 1258 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 701 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 73.3% | 0.0% | 1980 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1019 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 874 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 799 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 681 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
