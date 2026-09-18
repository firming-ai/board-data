# FILL — the inference availability index

*As of 2026-09-18T16:05:01+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 63.3** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 30.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 616 ms |  |
| anthropic/claude-opus-5/standard | 60 | 58.3% | 0.0% | 1122 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1278 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 930 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1243 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | — | — | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | 100.0% | 0.0% | 3530 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 783 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 802 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 80.0% | 16.7% | 8822 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 978 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 0.0% | 98.3% | — ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 58.3% | 33.3% | 3608 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 711 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 581 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 86.7% | 0.0% | 1628 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 825 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 13.3% | 0.0% | 11103 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1384 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 935 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1749 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 700 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
