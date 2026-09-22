# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 12 day(s) (2026-09-11 → 2026-09-22). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 73 | 70% | 18% | 4.5/70.6s | 4.3/4.9s | 64.8s | 0.85 | OPEN |
| gemini/gemini-3.5-flash | 73 | 82% | 16% | 3.1/22.4s | 2.1/2.3s | 49.9s | 0.70 | OPEN |
| gemini/gemini-3.5-flash-lite | 73 | 100% | 0% | 0.8/2.9s | 0.8/1.0s | 2.9s | 0.50 | DEALER |
| gemini/gemini-3.7-flash | 73 | 52% | 44% | 5.0/25.3s | 1.7/2.2s | 43.9s | 0.90 | CHECKBOX |
| openai/gpt-5.6-luna | 73 | 82% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.53 | DEALER |
| openai/gpt-5.6-sol | 73 | 63% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.74 | OPEN |
| openai/gpt-5.6-terra | 73 | 84% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.52 | DEALER |
| **pooled** | 511 | 76% | 11% | 2.8/15.1s | 2.0/4.5s | 29.7s | 0.71 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 1.3562 USD.
