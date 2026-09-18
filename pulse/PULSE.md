# FILL — the inference availability index

*As of 2026-09-18T03:05:01+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 80.0** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 30.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 654 ms |  |
| anthropic/claude-opus-5/standard | 60 | 70.0% | 0.0% | 1102 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1036 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 987 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1206 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | 100.0% | 0.0% | 6775 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | 100.0% | 0.0% | 2855 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 761 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 740 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 95.0% | 5.0% | 5172 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 846 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 80.0% | 20.0% | 4930 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1213 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 620 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 532 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 95.0% | 0.0% | 1059 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 726 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 21.7% | 0.0% | 1074 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1076 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 91.7% | 0.0% | 901 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 788 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 644 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
