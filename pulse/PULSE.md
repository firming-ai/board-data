# FILL — the inference availability index

*As of 2026-09-18T00:05:00+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 93.5** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 31.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 651 ms |  |
| anthropic/claude-opus-5/standard | 60 | 60.0% | 0.0% | 1050 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1040 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 893 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1201 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | 100.0% | 0.0% | 2855 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | 100.0% | 0.0% | 2438 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 675 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 716 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 11626 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 846 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 85.0% | 15.0% | 4939 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1187 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 637 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 538 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1278 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 651 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 40.0% | 0.0% | 1450 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1019 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 98.3% | 0.0% | 818 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 794 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 616 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
