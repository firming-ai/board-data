# FILL — the inference availability index

*As of 2026-09-18T05:05:01+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 80.0** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 30.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 653 ms |  |
| anthropic/claude-opus-5/standard | 60 | 60.0% | 0.0% | 1107 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1061 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 890 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1147 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | — | — | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | — | — | — ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 706 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 751 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 5580 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 858 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 73.3% | 26.7% | 5203 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1233 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 662 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 557 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 96.7% | 0.0% | 985 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 784 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 85.0% | 0.0% | 1100 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 976 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 841 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 797 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 682 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
