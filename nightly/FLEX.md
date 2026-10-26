# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 46 day(s) (2026-09-11 → 2026-10-26). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 890 | 51% | 37% | 5.2/79.2s | 4.5/9.1s | 64.3s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 890 | 78% | 16% | 3.0/32.4s | 2.5/3.1s | 39.2s | 0.72 | OPEN |
| gemini/gemini-3.5-flash-lite | 890 | 92% | 3% | 1.0/13.3s | 1.1/1.5s | 14.7s | 0.59 | DEALER |
| gemini/gemini-3.7-flash | 890 | 35% | 50% | 8.4/116.1s | 2.9/5.1s | 63.4s | 1.01 | CHECKBOX |
| openai/gpt-5.6-luna | 434 | 99% | 0% | 1.2/4.1s | 1.2/2.9s | 4.3s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 434 | 95% | 0% | 1.5/7.9s | 1.3/3.1s | 7.9s | 0.57 | DEALER |
| openai/gpt-5.6-terra | 434 | 100% | 0% | 1.1/2.7s | 1.2/2.7s | 2.7s | 0.51 | DEALER |
| **pooled** | 4862 | 73% | 19% | 2.2/40.6s | 2.2/5.0s | 59.1s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 12.6629 USD.
