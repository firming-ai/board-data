# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 48 day(s) (2026-09-11 → 2026-10-28). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 947 | 50% | 38% | 5.2/79.3s | 4.5/9.1s | 64.3s | 0.92 | CHECKBOX |
| gemini/gemini-3.5-flash | 947 | 79% | 15% | 3.1/34.7s | 2.5/3.2s | 38.2s | 0.71 | OPEN |
| gemini/gemini-3.5-flash-lite | 947 | 92% | 3% | 1.0/14.6s | 1.1/1.5s | 16.4s | 0.58 | DEALER |
| gemini/gemini-3.7-flash | 947 | 33% | 52% | 8.5/116.9s | 3.0/5.1s | 63.5s | 1.02 | CHECKBOX |
| openai/gpt-5.6-luna | 491 | 99% | 0% | 1.2/4.2s | 1.2/2.9s | 4.5s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 491 | 96% | 0% | 1.5/7.6s | 1.4/3.1s | 7.6s | 0.56 | DEALER |
| openai/gpt-5.6-terra | 491 | 100% | 0% | 1.1/2.7s | 1.2/2.7s | 2.7s | 0.50 | DEALER |
| **pooled** | 5261 | 73% | 20% | 2.1/39.9s | 2.2/5.0s | 60.3s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 13.7263 USD.
