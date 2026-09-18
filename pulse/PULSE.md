# FILL — the inference availability index

*As of 2026-09-18T12:05:01+00:00 · probe pulse-1.0.0 · methodology 1.0.0*

**FILL 80.6** *(gap)*

Share of frontier discount-lane requests served inside 60 s, across venues, last five minutes (n = 31.0).

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 615 ms |  |
| anthropic/claude-opus-5/standard | 60 | 56.7% | 0.0% | 1026 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1199 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 899 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1220 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 12 | 33.3% | 25.0% | 20931 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 12 | 100.0% | 0.0% | 2733 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 749 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 757 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 5739 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 901 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 0.0% | 66.7% | — ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1301 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 692 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 555 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1216 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 714 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 93.3% | 0.0% | 1558 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1036 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 98.3% | 0.0% | 831 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 830 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 645 ms |  |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
