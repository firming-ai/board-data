# FILL — the inference availability index

*As of 2026-09-18T11:05:00+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 83.9** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 31.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 615 ms |  |
| anthropic/claude-opus-5/standard | 60 | 63.3% | 0.0% | 997 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1424 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 924 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1268 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | 75.0% | 0.0% | 5625 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | 100.0% | 0.0% | 2948 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 729 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 774 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 5459 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 922 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 0.0% | 80.0% | — ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 2180 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 720 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 555 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1223 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 764 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 38.3% | 0.0% | 1876 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1042 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 98.3% | 0.0% | 843 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 864 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 661 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
