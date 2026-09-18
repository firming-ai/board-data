# FILL — the inference availability index

*As of 2026-09-18T14:05:01+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 63.3** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 30.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 611 ms |  |
| anthropic/claude-opus-5/standard | 60 | 63.3% | 1.7% | 1161 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1240 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 997 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1223 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | 0.0% | 0.0% | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | — | — | — ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 812 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 778 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 90.0% | 10.0% | 7887 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 947 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 0.0% | 96.7% | — ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 4277 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 704 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 569 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 95.0% | 0.0% | 1432 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 821 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 11.7% | 0.0% | 11148 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1424 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 876 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1120 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 653 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
