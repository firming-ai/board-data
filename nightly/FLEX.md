# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 41 day(s) (2026-09-11 → 2026-10-21). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 769 | 53% | 34% | 5.1/77.7s | 4.5/8.8s | 64.5s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 769 | 76% | 17% | 3.1/35.1s | 2.4/3.1s | 42.2s | 0.74 | OPEN |
| gemini/gemini-3.5-flash-lite | 769 | 91% | 3% | 1.0/12.6s | 1.1/1.5s | 14.5s | 0.59 | DEALER |
| gemini/gemini-3.7-flash | 769 | 38% | 50% | 6.9/106.4s | 2.7/4.9s | 62.9s | 0.98 | CHECKBOX |
| openai/gpt-5.6-luna | 769 | 40% | 0% | 1.2/4.3s | 1.2/3.0s | 4.5s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 769 | 38% | 0% | 1.4/8.6s | 1.4/3.4s | 8.6s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 769 | 41% | 0% | 1.1/2.9s | 1.2/3.0s | 2.9s | 0.50 | CHECKBOX |
| **pooled** | 5383 | 54% | 15% | 2.3/40.8s | 2.2/5.0s | 54.9s | 0.73 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 16.6560 USD.
