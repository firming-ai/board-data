# FILL — the inference availability index

*As of 2026-09-18T01:05:00+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 100.0** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 30.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 638 ms |  |
| anthropic/claude-opus-5/standard | 60 | 63.3% | 0.0% | 1074 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1021 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1050 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1147 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | 100.0% | 0.0% | 3087 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | 100.0% | 0.0% | 2605 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 693 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 701 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 96.7% | 3.3% | 11350 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 869 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 83.3% | 16.7% | 5213 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1177 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 618 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 528 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1201 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 740 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 60.0% | 0.0% | 1322 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 995 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 804 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 781 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 618 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
