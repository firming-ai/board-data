# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 24 day(s) (2026-09-11 → 2026-10-04). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 370 | 69% | 25% | 4.6/56.7s | 4.3/5.1s | 64.0s | 0.82 | OPEN |
| gemini/gemini-3.5-flash | 370 | 75% | 22% | 8.4/43.2s | 2.3/2.6s | 50.9s | 0.77 | OPEN |
| gemini/gemini-3.5-flash-lite | 370 | 96% | 2% | 0.9/14.5s | 1.0/1.2s | 17.9s | 0.60 | DEALER |
| gemini/gemini-3.7-flash | 370 | 35% | 64% | 4.7/30.6s | 2.3/4.1s | 36.6s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 370 | 16% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 370 | 12% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.56 | CHECKBOX |
| openai/gpt-5.6-terra | 370 | 16% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.50 | CHECKBOX |
| **pooled** | 2590 | 46% | 16% | 3.5/34.3s | 2.3/4.7s | 42.5s | 0.72 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 8.8355 USD.
