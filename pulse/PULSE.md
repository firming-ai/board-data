# FILL — the inference availability index

*As of 2026-09-18T13:05:01+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 67.7** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 31.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 621 ms |  |
| anthropic/claude-opus-5/standard | 60 | 63.3% | 0.0% | 1050 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1450 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 876 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1233 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | 50.0% | 0.0% | 44223 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | 100.0% | 0.0% | 3093 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 98.3% | 0.0% | 792 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 763 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 2128 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 883 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 0.0% | 81.7% | — ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1521 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 683 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 573 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 93.3% | 0.0% | 1333 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 766 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 50.0% | 0.0% | 1865 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1301 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 821 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 935 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 659 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
