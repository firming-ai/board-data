# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 60 day(s) (2026-09-11 → 2026-11-09). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 1229 | 54% | 34% | 5.2/79.2s | 4.4/8.3s | 64.3s | 0.92 | CHECKBOX |
| gemini/gemini-3.5-flash | 1229 | 82% | 14% | 3.1/30.9s | 2.7/3.3s | 34.9s | 0.69 | DEALER |
| gemini/gemini-3.5-flash-lite | 1229 | 94% | 2% | 1.1/14.6s | 1.2/1.5s | 15.2s | 0.57 | DEALER |
| gemini/gemini-3.7-flash | 1229 | 28% | 52% | 12.1/136.2s | 3.3/5.2s | 63.7s | 1.08 | CHECKBOX |
| openai/gpt-5.6-luna | 773 | 99% | 0% | 1.2/5.3s | 1.2/2.6s | 5.4s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 773 | 96% | 0% | 1.4/5.6s | 1.4/3.0s | 6.5s | 0.56 | DEALER |
| openai/gpt-5.6-terra | 773 | 100% | 0% | 1.1/2.5s | 1.2/2.5s | 2.6s | 0.51 | DEALER |
| **pooled** | 7235 | 75% | 17% | 1.9/39.8s | 2.1/5.0s | 62.3s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 18.6119 USD.
