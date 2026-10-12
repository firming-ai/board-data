# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 32 day(s) (2026-09-11 → 2026-10-12). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 557 | 66% | 26% | 4.9/66.7s | 4.4/6.0s | 64.2s | 0.86 | CHECKBOX |
| gemini/gemini-3.5-flash | 557 | 77% | 21% | 3.6/38.6s | 2.3/2.8s | 46.8s | 0.76 | OPEN |
| gemini/gemini-3.5-flash-lite | 557 | 96% | 2% | 0.9/12.6s | 1.0/1.4s | 14.5s | 0.59 | DEALER |
| gemini/gemini-3.7-flash | 557 | 38% | 58% | 6.2/78.2s | 2.4/4.9s | 61.2s | 0.96 | CHECKBOX |
| openai/gpt-5.6-luna | 557 | 18% | 0% | 1.7/7.5s | 1.3/3.7s | 6.9s | 0.50 | CHECKBOX |
| openai/gpt-5.6-sol | 557 | 15% | 0% | 1.8/8.1s | 1.5/3.9s | 7.5s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 557 | 18% | 0% | 1.3/3.1s | 1.3/3.2s | 3.2s | 0.50 | CHECKBOX |
| **pooled** | 3899 | 47% | 15% | 3.0/43.2s | 2.3/5.0s | 52.9s | 0.72 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 13.2506 USD.
