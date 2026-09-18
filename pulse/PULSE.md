# FILL — the inference availability index

*As of 2026-09-18T07:05:00+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 74.2** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 31.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 635 ms |  |
| anthropic/claude-opus-5/standard | 60 | 70.0% | 0.0% | 1168 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1059 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1087 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1206 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | 100.0% | 0.0% | 2913 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | — | — | — ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 807 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 774 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 3391 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 869 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 56.7% | 28.3% | 9274 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1461 ms |  |
| mistral/mistral-large/standard | 60 | 98.3% | 1.7% | 655 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 548 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1373 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 764 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 11.7% | 0.0% | 8665 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 91.7% | 0.0% | 2902 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 98.3% | 0.0% | 852 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 825 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 661 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
