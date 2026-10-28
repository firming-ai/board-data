# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 48 day(s) (2026-09-11 → 2026-10-28). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 938 | 50% | 38% | 5.2/79.3s | 4.5/8.9s | 64.3s | 0.92 | CHECKBOX |
| gemini/gemini-3.5-flash | 938 | 79% | 16% | 3.1/34.6s | 2.5/3.2s | 38.6s | 0.72 | OPEN |
| gemini/gemini-3.5-flash-lite | 938 | 92% | 3% | 1.0/14.3s | 1.1/1.5s | 14.9s | 0.58 | DEALER |
| gemini/gemini-3.7-flash | 938 | 34% | 52% | 8.5/116.9s | 3.0/5.1s | 63.4s | 1.02 | CHECKBOX |
| openai/gpt-5.6-luna | 482 | 99% | 0% | 1.2/4.2s | 1.2/2.9s | 4.4s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 482 | 95% | 0% | 1.5/7.7s | 1.4/3.1s | 7.7s | 0.56 | DEALER |
| openai/gpt-5.6-terra | 482 | 100% | 0% | 1.1/2.7s | 1.2/2.7s | 2.7s | 0.51 | DEALER |
| **pooled** | 5198 | 73% | 20% | 2.1/40.1s | 2.2/5.0s | 59.6s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 13.5582 USD.
