# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 50 day(s) (2026-09-11 → 2026-10-30). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 986 | 51% | 37% | 5.2/73.7s | 4.4/8.9s | 64.3s | 0.92 | CHECKBOX |
| gemini/gemini-3.5-flash | 986 | 79% | 15% | 3.0/34.2s | 2.6/3.3s | 37.1s | 0.71 | OPEN |
| gemini/gemini-3.5-flash-lite | 986 | 92% | 3% | 1.1/14.9s | 1.1/1.6s | 16.0s | 0.58 | DEALER |
| gemini/gemini-3.7-flash | 986 | 33% | 51% | 9.4/130.0s | 3.1/5.1s | 63.5s | 1.04 | CHECKBOX |
| openai/gpt-5.6-luna | 530 | 99% | 0% | 1.2/4.3s | 1.2/2.9s | 4.5s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 530 | 96% | 0% | 1.4/7.1s | 1.4/3.1s | 7.1s | 0.56 | DEALER |
| openai/gpt-5.6-terra | 530 | 100% | 0% | 1.1/2.7s | 1.2/2.7s | 2.8s | 0.50 | DEALER |
| **pooled** | 5534 | 74% | 19% | 2.1/41.0s | 2.2/5.0s | 60.9s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 14.3900 USD.
