# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 14 day(s) (2026-09-11 → 2026-09-24). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 130 | 61% | 32% | 4.6/34.1s | 4.3/5.2s | 64.3s | 0.83 | OPEN |
| gemini/gemini-3.5-flash | 130 | 78% | 18% | 4.1/49.7s | 2.2/2.6s | 61.9s | 0.75 | OPEN |
| gemini/gemini-3.5-flash-lite | 130 | 94% | 3% | 0.8/30.3s | 0.9/1.1s | 32.7s | 0.64 | DEALER |
| gemini/gemini-3.7-flash | 130 | 35% | 63% | 5.0/24.0s | 1.8/2.7s | 33.9s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 130 | 46% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.52 | CHECKBOX |
| openai/gpt-5.6-sol | 130 | 35% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.65 | CHECKBOX |
| openai/gpt-5.6-terra | 130 | 47% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.51 | CHECKBOX |
| **pooled** | 910 | 57% | 17% | 2.9/24.8s | 2.2/4.6s | 36.5s | 0.74 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 2.8240 USD.
