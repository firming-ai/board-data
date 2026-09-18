# FILL — the inference availability index

*As of 2026-09-18T15:05:00+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 53.3** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 30.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 606 ms |  |
| anthropic/claude-opus-5/standard | 60 | 73.3% | 0.0% | 1065 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1263 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 919 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1253 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | — | — | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | — | — | — ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 774 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 767 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 60.0% | 38.3% | 8596 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 968 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 1.7% | 93.3% | 14200 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 2219 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 781 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 591 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 98.3% | 0.0% | 1283 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 890 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 13.3% | 0.0% | 13187 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1641 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 904 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1467 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 678 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
