# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 12 day(s) (2026-09-11 → 2026-09-22). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 82 | 65% | 24% | 4.5/67.9s | 4.3/4.9s | 64.7s | 0.86 | CHECKBOX |
| gemini/gemini-3.5-flash | 82 | 80% | 16% | 3.6/50.5s | 2.1/2.5s | 61.9s | 0.73 | OPEN |
| gemini/gemini-3.5-flash-lite | 82 | 95% | 2% | 0.8/13.5s | 0.8/1.1s | 14.8s | 0.63 | DEALER |
| gemini/gemini-3.7-flash | 82 | 48% | 49% | 4.7/25.0s | 1.7/2.5s | 32.3s | 0.92 | CHECKBOX |
| openai/gpt-5.6-luna | 82 | 73% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.53 | OPEN |
| openai/gpt-5.6-sol | 82 | 56% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.72 | OPEN |
| openai/gpt-5.6-terra | 82 | 74% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.52 | OPEN |
| **pooled** | 574 | 70% | 13% | 2.8/21.2s | 2.1/4.5s | 39.9s | 0.73 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 1.6005 USD.
