# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 44 day(s) (2026-09-11 → 2026-10-24). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 840 | 51% | 36% | 5.2/76.2s | 4.5/9.0s | 64.4s | 0.92 | CHECKBOX |
| gemini/gemini-3.5-flash | 840 | 77% | 17% | 3.0/34.5s | 2.5/3.1s | 40.8s | 0.73 | OPEN |
| gemini/gemini-3.5-flash-lite | 840 | 91% | 3% | 1.0/13.8s | 1.1/1.5s | 14.9s | 0.59 | DEALER |
| gemini/gemini-3.7-flash | 840 | 36% | 51% | 7.4/115.4s | 2.8/5.1s | 63.2s | 1.00 | CHECKBOX |
| openai/gpt-5.6-luna | 384 | 99% | 0% | 1.2/4.3s | 1.2/2.9s | 4.5s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 384 | 94% | 0% | 1.5/7.9s | 1.3/3.2s | 7.9s | 0.58 | DEALER |
| openai/gpt-5.6-terra | 384 | 100% | 0% | 1.1/2.7s | 1.2/2.8s | 2.8s | 0.51 | DEALER |
| **pooled** | 4512 | 73% | 20% | 2.2/40.2s | 2.2/5.0s | 55.9s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 11.7761 USD.
