# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 65 day(s) (2026-09-11 → 2026-11-14). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 1344 | 54% | 33% | 5.5/93.0s | 4.5/8.4s | 64.5s | 0.93 | CHECKBOX |
| gemini/gemini-3.5-flash | 1344 | 83% | 13% | 3.1/33.9s | 2.7/3.3s | 35.9s | 0.69 | DEALER |
| gemini/gemini-3.5-flash-lite | 1344 | 94% | 2% | 1.1/13.4s | 1.2/1.6s | 14.4s | 0.56 | DEALER |
| gemini/gemini-3.7-flash | 1344 | 26% | 53% | 13.1/140.8s | 3.3/5.1s | 63.8s | 1.10 | CHECKBOX |
| openai/gpt-5.6-luna | 888 | 99% | 0% | 1.2/5.4s | 1.2/2.4s | 5.5s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 888 | 96% | 0% | 1.4/5.4s | 1.4/2.9s | 6.0s | 0.55 | DEALER |
| openai/gpt-5.6-terra | 888 | 100% | 0% | 1.1/2.5s | 1.2/2.0s | 2.5s | 0.51 | DEALER |
| **pooled** | 8040 | 76% | 17% | 1.8/41.0s | 2.0/5.0s | 62.6s | 0.80 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 20.7028 USD.
