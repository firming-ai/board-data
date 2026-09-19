# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 9 day(s) (2026-09-11 → 2026-09-19). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 46 | 65% | 20% | 4.4/55.1s | 4.3/5.1s | 65.6s | 0.88 | CHECKBOX |
| gemini/gemini-3.5-flash | 46 | 87% | 13% | 2.4/14.5s | 2.0/2.3s | 27.3s | 0.65 | DEALER |
| gemini/gemini-3.5-flash-lite | 46 | 100% | 0% | 0.8/3.2s | 0.7/0.8s | 3.2s | 0.50 | DEALER |
| gemini/gemini-3.7-flash | 46 | 48% | 46% | 5.4/24.4s | 1.7/2.3s | 61.5s | 0.92 | CHECKBOX |
| openai/gpt-5.6-luna | 46 | 98% | 0% | 2.9/13.2s | 2.9/4.4s | 13.1s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 46 | 72% | 0% | 3.4/10.4s | 3.1/3.9s | 9.1s | 0.81 | OPEN |
| openai/gpt-5.6-terra | 46 | 98% | 0% | 2.7/3.7s | 2.7/3.3s | 4.1s | 0.54 | DEALER |
| **pooled** | 322 | 81% | 11% | 2.8/14.1s | 2.4/4.5s | 27.6s | 0.73 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 0.7921 USD.
