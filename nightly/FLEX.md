# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 31 day(s) (2026-09-11 → 2026-10-11). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 530 | 68% | 24% | 4.9/66.4s | 4.4/5.9s | 64.1s | 0.85 | CHECKBOX |
| gemini/gemini-3.5-flash | 530 | 76% | 22% | 4.6/39.7s | 2.3/2.8s | 47.0s | 0.76 | OPEN |
| gemini/gemini-3.5-flash-lite | 530 | 96% | 2% | 0.9/12.7s | 1.0/1.4s | 14.5s | 0.59 | DEALER |
| gemini/gemini-3.7-flash | 530 | 38% | 59% | 5.8/55.5s | 2.4/4.9s | 49.4s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 530 | 14% | 0% | 2.6/12.9s | 2.2/4.0s | 12.8s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 530 | 11% | 0% | 2.7/8.4s | 2.8/3.9s | 7.5s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 530 | 14% | 0% | 2.4/3.2s | 2.2/3.3s | 3.4s | 0.50 | CHECKBOX |
| **pooled** | 3710 | 45% | 15% | 3.3/43.3s | 2.3/5.0s | 51.9s | 0.72 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 12.7666 USD.
