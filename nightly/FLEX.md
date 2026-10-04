# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 24 day(s) (2026-09-11 → 2026-10-04). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 361 | 68% | 26% | 4.7/57.2s | 4.3/5.2s | 64.0s | 0.83 | OPEN |
| gemini/gemini-3.5-flash | 361 | 74% | 23% | 8.4/44.6s | 2.3/2.6s | 52.1s | 0.77 | OPEN |
| gemini/gemini-3.5-flash-lite | 361 | 96% | 2% | 0.9/14.5s | 1.0/1.2s | 19.2s | 0.60 | DEALER |
| gemini/gemini-3.7-flash | 361 | 34% | 65% | 4.9/31.4s | 2.3/3.7s | 37.8s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 361 | 17% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 361 | 13% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.56 | CHECKBOX |
| openai/gpt-5.6-terra | 361 | 17% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.50 | CHECKBOX |
| **pooled** | 2527 | 46% | 17% | 3.5/35.1s | 2.3/4.7s | 43.0s | 0.73 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 8.6264 USD.
