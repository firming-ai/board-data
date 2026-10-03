# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 23 day(s) (2026-09-11 → 2026-10-03). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 346 | 68% | 26% | 4.7/58.4s | 4.3/5.2s | 64.1s | 0.83 | OPEN |
| gemini/gemini-3.5-flash | 346 | 73% | 24% | 8.4/47.5s | 2.3/2.6s | 52.7s | 0.78 | OPEN |
| gemini/gemini-3.5-flash-lite | 346 | 96% | 3% | 0.9/14.7s | 1.0/1.2s | 20.0s | 0.61 | DEALER |
| gemini/gemini-3.7-flash | 346 | 34% | 65% | 4.9/32.6s | 2.3/3.8s | 39.6s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 346 | 17% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 346 | 13% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.56 | CHECKBOX |
| openai/gpt-5.6-terra | 346 | 18% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.50 | CHECKBOX |
| **pooled** | 2422 | 46% | 17% | 3.5/34.3s | 2.3/4.7s | 43.2s | 0.73 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 8.2621 USD.
