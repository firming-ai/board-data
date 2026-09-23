# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 13 day(s) (2026-09-11 → 2026-09-23). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 106 | 65% | 26% | 4.6/46.0s | 4.3/5.1s | 64.5s | 0.84 | OPEN |
| gemini/gemini-3.5-flash | 106 | 77% | 19% | 4.8/54.9s | 2.2/2.6s | 62.0s | 0.76 | OPEN |
| gemini/gemini-3.5-flash-lite | 106 | 94% | 3% | 0.8/23.8s | 0.8/1.1s | 25.8s | 0.63 | DEALER |
| gemini/gemini-3.7-flash | 106 | 42% | 56% | 5.1/24.1s | 1.8/2.7s | 40.9s | 0.94 | CHECKBOX |
| openai/gpt-5.6-luna | 106 | 57% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.52 | OPEN |
| openai/gpt-5.6-sol | 106 | 43% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.68 | CHECKBOX |
| openai/gpt-5.6-terra | 106 | 58% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.52 | OPEN |
| **pooled** | 742 | 62% | 15% | 2.9/24.2s | 2.2/4.6s | 42.8s | 0.74 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 2.2125 USD.
