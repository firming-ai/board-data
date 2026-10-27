# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 47 day(s) (2026-09-11 → 2026-10-27). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 913 | 51% | 37% | 5.2/78.0s | 4.5/9.0s | 64.3s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 913 | 78% | 16% | 3.0/34.6s | 2.5/3.2s | 39.1s | 0.72 | OPEN |
| gemini/gemini-3.5-flash-lite | 913 | 92% | 3% | 1.0/14.4s | 1.1/1.5s | 15.0s | 0.58 | DEALER |
| gemini/gemini-3.7-flash | 913 | 34% | 51% | 8.4/117.5s | 2.9/5.1s | 63.4s | 1.02 | CHECKBOX |
| openai/gpt-5.6-luna | 457 | 99% | 0% | 1.2/4.1s | 1.2/2.9s | 4.4s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 457 | 95% | 0% | 1.5/7.8s | 1.4/3.1s | 7.8s | 0.57 | DEALER |
| openai/gpt-5.6-terra | 457 | 100% | 0% | 1.1/2.7s | 1.2/2.7s | 2.8s | 0.51 | DEALER |
| **pooled** | 5023 | 73% | 19% | 2.1/40.3s | 2.2/5.0s | 59.2s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 13.0982 USD.
