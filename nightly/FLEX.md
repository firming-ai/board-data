# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 34 day(s) (2026-09-11 → 2026-10-14). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 610 | 63% | 26% | 5.0/68.7s | 4.5/7.1s | 64.4s | 0.87 | CHECKBOX |
| gemini/gemini-3.5-flash | 610 | 74% | 21% | 3.5/37.7s | 2.3/3.0s | 47.0s | 0.76 | OPEN |
| gemini/gemini-3.5-flash-lite | 610 | 93% | 3% | 0.9/13.1s | 1.1/1.4s | 14.7s | 0.60 | DEALER |
| gemini/gemini-3.7-flash | 610 | 36% | 57% | 6.2/87.7s | 2.5/4.9s | 61.7s | 0.97 | CHECKBOX |
| openai/gpt-5.6-luna | 610 | 25% | 0% | 1.4/5.9s | 1.3/3.4s | 5.7s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 610 | 22% | 0% | 1.8/9.9s | 1.4/3.8s | 9.9s | 0.55 | CHECKBOX |
| openai/gpt-5.6-terra | 610 | 25% | 0% | 1.1/3.0s | 1.3/3.2s | 3.0s | 0.50 | CHECKBOX |
| **pooled** | 4270 | 48% | 15% | 2.7/42.4s | 2.3/5.0s | 55.7s | 0.73 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 14.0546 USD.
