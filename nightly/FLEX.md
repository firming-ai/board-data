# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 26 day(s) (2026-09-11 → 2026-10-06). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 397 | 68% | 26% | 4.7/59.6s | 4.3/5.2s | 64.1s | 0.83 | OPEN |
| gemini/gemini-3.5-flash | 397 | 75% | 22% | 8.5/42.3s | 2.3/2.6s | 49.0s | 0.77 | OPEN |
| gemini/gemini-3.5-flash-lite | 397 | 96% | 2% | 0.9/13.2s | 1.0/1.3s | 15.1s | 0.59 | DEALER |
| gemini/gemini-3.7-flash | 397 | 35% | 64% | 4.7/32.0s | 2.3/4.3s | 36.7s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 397 | 15% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 397 | 12% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.56 | CHECKBOX |
| openai/gpt-5.6-terra | 397 | 15% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.50 | CHECKBOX |
| **pooled** | 2779 | 45% | 16% | 3.5/35.5s | 2.3/4.7s | 42.7s | 0.72 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 9.5322 USD.
