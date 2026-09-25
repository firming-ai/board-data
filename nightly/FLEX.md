# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 15 day(s) (2026-09-11 → 2026-09-25). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 155 | 59% | 35% | 4.6/40.3s | 4.3/5.1s | 64.0s | 0.84 | OPEN |
| gemini/gemini-3.5-flash | 155 | 74% | 23% | 6.0/52.4s | 2.3/2.5s | 61.9s | 0.78 | OPEN |
| gemini/gemini-3.5-flash-lite | 155 | 94% | 3% | 0.8/29.3s | 0.9/1.1s | 32.0s | 0.63 | DEALER |
| gemini/gemini-3.7-flash | 155 | 33% | 65% | 5.2/23.3s | 1.9/2.9s | 32.0s | 0.96 | CHECKBOX |
| openai/gpt-5.6-luna | 155 | 39% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.52 | CHECKBOX |
| openai/gpt-5.6-sol | 155 | 30% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.63 | CHECKBOX |
| openai/gpt-5.6-terra | 155 | 39% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.51 | CHECKBOX |
| **pooled** | 1085 | 53% | 18% | 2.9/25.4s | 2.2/4.6s | 35.2s | 0.74 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 3.4681 USD.
