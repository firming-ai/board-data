# FILL — the inference availability index

*As of 2026-09-17T21:05:12+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 62.5** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 24.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 16 | 100.0% | 0.0% | 625 ms | ▲ |
| anthropic/claude-opus-5/standard | 16 | 12.5% | 0.0% | 999 ms | ▲ |
| anthropic/claude-sonnet-5/standard | 16 | 31.2% | 0.0% | 706 ms | ▲ |
| deepseek/deepseek-v4-flash/standard | 16 | 100.0% | 0.0% | 742 ms | ▲ |
| deepseek/deepseek-v4-pro/standard | 16 | 100.0% | 0.0% | 1189 ms | ▲ |
| gemini/gemini-3.1-pro-preview/flex | 12 | 8.3% | 0.0% | 4596 ms | ▲ |
| gemini/gemini-3.1-pro-preview/standard | 12 | 8.3% | 0.0% | 2641 ms | ▲ |
| gemini/gemini-3.5-flash-lite/flex | 16 | 31.2% | 0.0% | 737 ms | ▲ |
| gemini/gemini-3.5-flash-lite/standard | 16 | 31.2% | 0.0% | 701 ms | ▲ |
| gemini/gemini-3.5-flash/flex | 16 | 31.2% | 0.0% | 11193 ms | ▲ |
| gemini/gemini-3.5-flash/standard | 16 | 31.2% | 0.0% | 815 ms | ▲ |
| gemini/gemini-3.7-flash/flex | 16 | 0.0% | 56.2% | — ms | ▲ |
| gemini/gemini-3.7-flash/standard | 12 | 8.3% | 0.0% | 1076 ms | ▲ |
| mistral/mistral-large/standard | 16 | 100.0% | 0.0% | 647 ms | ▲ |
| mistral/mistral-small/standard | 16 | 100.0% | 0.0% | 586 ms | ▲ |
| openai/gpt-5.6-luna/flex | 16 | 6.2% | 0.0% | 3801 ms | ▲ |
| openai/gpt-5.6-luna/standard | 16 | 31.2% | 0.0% | 751 ms | ▲ |
| openai/gpt-5.6-sol/flex | 16 | 0.0% | 0.0% | — ms | ▲ |
| openai/gpt-5.6-sol/standard | 16 | 31.2% | 0.0% | 1063 ms | ▲ |
| openai/gpt-5.6-terra/flex | 16 | 31.2% | 0.0% | 721 ms | ▲ |
| openai/gpt-5.6-terra/standard | 16 | 18.8% | 0.0% | 850 ms | ▲ |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
