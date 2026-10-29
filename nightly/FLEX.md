# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 49 day(s) (2026-09-11 → 2026-10-29). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 971 | 50% | 38% | 5.2/76.6s | 4.5/9.0s | 64.3s | 0.92 | CHECKBOX |
| gemini/gemini-3.5-flash | 971 | 79% | 15% | 3.0/34.5s | 2.5/3.2s | 37.4s | 0.71 | OPEN |
| gemini/gemini-3.5-flash-lite | 971 | 92% | 3% | 1.0/14.8s | 1.1/1.6s | 16.3s | 0.58 | DEALER |
| gemini/gemini-3.7-flash | 971 | 33% | 52% | 8.9/123.8s | 3.0/5.1s | 63.5s | 1.03 | CHECKBOX |
| openai/gpt-5.6-luna | 515 | 99% | 0% | 1.2/4.2s | 1.2/2.9s | 4.4s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 515 | 96% | 0% | 1.4/7.3s | 1.4/3.1s | 7.3s | 0.56 | DEALER |
| openai/gpt-5.6-terra | 515 | 100% | 0% | 1.1/2.7s | 1.2/2.7s | 2.8s | 0.50 | DEALER |
| **pooled** | 5429 | 73% | 19% | 2.1/40.2s | 2.2/5.0s | 60.7s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 14.1414 USD.
