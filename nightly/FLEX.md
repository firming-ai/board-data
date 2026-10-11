# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 31 day(s) (2026-09-11 → 2026-10-11). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 539 | 68% | 24% | 4.9/66.4s | 4.4/5.9s | 64.1s | 0.85 | OPEN |
| gemini/gemini-3.5-flash | 539 | 77% | 21% | 3.9/39.5s | 2.3/2.8s | 47.0s | 0.76 | OPEN |
| gemini/gemini-3.5-flash-lite | 539 | 96% | 2% | 0.9/12.6s | 1.0/1.4s | 14.5s | 0.59 | DEALER |
| gemini/gemini-3.7-flash | 539 | 38% | 59% | 6.1/65.3s | 2.4/4.9s | 56.0s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 539 | 15% | 0% | 2.4/12.6s | 2.0/3.9s | 12.0s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 539 | 12% | 0% | 2.3/7.9s | 2.1/3.9s | 7.2s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 539 | 15% | 0% | 2.3/3.2s | 1.9/3.2s | 3.2s | 0.50 | CHECKBOX |
| **pooled** | 3773 | 46% | 15% | 3.1/43.3s | 2.3/5.0s | 52.1s | 0.72 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 12.9150 USD.
