# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 47 day(s) (2026-09-11 → 2026-10-27). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 923 | 50% | 38% | 5.2/79.4s | 4.5/8.9s | 64.3s | 0.92 | CHECKBOX |
| gemini/gemini-3.5-flash | 923 | 79% | 16% | 3.0/34.7s | 2.5/3.2s | 38.9s | 0.72 | OPEN |
| gemini/gemini-3.5-flash-lite | 923 | 92% | 3% | 1.0/14.5s | 1.1/1.5s | 15.2s | 0.58 | DEALER |
| gemini/gemini-3.7-flash | 923 | 34% | 52% | 8.4/117.3s | 3.0/5.1s | 63.4s | 1.01 | CHECKBOX |
| openai/gpt-5.6-luna | 467 | 99% | 0% | 1.2/4.3s | 1.2/2.9s | 4.5s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 467 | 95% | 0% | 1.5/7.8s | 1.4/3.1s | 7.8s | 0.57 | DEALER |
| openai/gpt-5.6-terra | 467 | 100% | 0% | 1.1/2.7s | 1.2/2.7s | 2.8s | 0.51 | DEALER |
| **pooled** | 5093 | 73% | 20% | 2.1/40.2s | 2.2/5.0s | 59.1s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 13.2788 USD.
