# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 61 day(s) (2026-09-11 → 2026-11-10). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 1251 | 54% | 34% | 5.3/86.9s | 4.4/8.3s | 64.3s | 0.92 | CHECKBOX |
| gemini/gemini-3.5-flash | 1251 | 82% | 13% | 3.1/31.9s | 2.7/3.3s | 34.9s | 0.69 | DEALER |
| gemini/gemini-3.5-flash-lite | 1251 | 94% | 2% | 1.1/14.5s | 1.2/1.6s | 15.0s | 0.57 | DEALER |
| gemini/gemini-3.7-flash | 1251 | 27% | 53% | 12.3/140.3s | 3.3/5.2s | 63.7s | 1.08 | CHECKBOX |
| openai/gpt-5.6-luna | 795 | 99% | 0% | 1.2/5.1s | 1.2/2.5s | 5.3s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 795 | 96% | 0% | 1.4/5.6s | 1.4/3.0s | 6.4s | 0.56 | DEALER |
| openai/gpt-5.6-terra | 795 | 100% | 0% | 1.1/2.5s | 1.2/2.4s | 2.6s | 0.51 | DEALER |
| **pooled** | 7389 | 75% | 17% | 1.9/40.1s | 2.1/5.0s | 62.3s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 19.0279 USD.
