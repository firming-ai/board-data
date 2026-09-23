# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 13 day(s) (2026-09-11 → 2026-09-23). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 97 | 68% | 23% | 4.5/50.1s | 4.4/4.9s | 64.6s | 0.83 | OPEN |
| gemini/gemini-3.5-flash | 97 | 80% | 15% | 5.1/55.7s | 2.2/2.6s | 62.0s | 0.74 | OPEN |
| gemini/gemini-3.5-flash-lite | 97 | 96% | 2% | 0.8/13.8s | 0.8/1.1s | 15.9s | 0.61 | DEALER |
| gemini/gemini-3.7-flash | 97 | 44% | 53% | 5.0/24.2s | 1.7/2.7s | 46.5s | 0.93 | CHECKBOX |
| openai/gpt-5.6-luna | 97 | 62% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.53 | OPEN |
| openai/gpt-5.6-sol | 97 | 47% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.69 | CHECKBOX |
| openai/gpt-5.6-terra | 97 | 63% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.52 | OPEN |
| **pooled** | 679 | 66% | 13% | 2.9/22.7s | 2.1/4.6s | 42.7s | 0.73 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 1.9698 USD.
