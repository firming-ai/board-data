# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 9 day(s) (2026-09-11 → 2026-09-19). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 49 | 67% | 18% | 4.5/45.8s | 4.3/5.0s | 65.5s | 0.86 | CHECKBOX |
| gemini/gemini-3.5-flash | 49 | 86% | 14% | 2.7/19.5s | 2.1/2.3s | 33.2s | 0.67 | DEALER |
| gemini/gemini-3.5-flash-lite | 49 | 100% | 0% | 0.8/3.1s | 0.7/0.8s | 3.1s | 0.50 | DEALER |
| gemini/gemini-3.7-flash | 49 | 47% | 47% | 6.2/24.2s | 1.7/2.3s | 61.5s | 0.92 | CHECKBOX |
| openai/gpt-5.6-luna | 49 | 98% | 0% | 2.9/13.1s | 2.9/4.3s | 13.0s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 49 | 73% | 0% | 3.4/10.0s | 3.1/3.9s | 9.0s | 0.79 | OPEN |
| openai/gpt-5.6-terra | 49 | 98% | 0% | 2.6/3.6s | 2.7/3.3s | 4.0s | 0.53 | DEALER |
| **pooled** | 343 | 81% | 11% | 2.8/14.2s | 2.3/4.5s | 27.5s | 0.72 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 0.8395 USD.
