# RECONCILE — sheet against page

`tools/sheet_watch.py` asks whether a page moved since yesterday. This asks
whether the page and `src/firming/prices.py` agree **today** — which is the only
question that catches a row that was already wrong when the watch took its first
reading, because no hash diff spans a baseline.

Rates are parsed out of the page text committed in `pages/`, so every figure
below is reproducible from this branch with no network at all.

**No number here has edited the price sheet**, and nothing in CI may. Same rule
as the watch, for the same reason: a parser confident enough to rewrite
`prices.py` from scraped text would eventually launder a table-layout change
into a receipt.

`classification` is the sheet watch's most recent LLM label for that source —
what moved, per the classifier that already ran. It answers a different question
than the rows below it and is here so a reader has both at once.

Reconciled 2026-10-29 against `firming.prices` sheet **2026-08-30**.

| source | status | mismatches | missing | unverifiable | models on page | classification |
| --- | --- | --- | --- | --- | --- | --- |
| `anthropic` | unreadable | 0 | 10 | 0 | 0 | copy change (2026-10-29) |
| `google` | **drift** | 12 | 1 | 0 | 30 | copy change (2026-10-29) |
| `groq` | skipped | 0 | 0 | 1 | 0 | copy change (2026-10-09) |
| `mistral` | unreadable | 0 | 10 | 0 | 0 | price change (2026-10-29) |
| `openai` | **drift** | 2 | 2 | 4 | 10 | copy change (2026-10-29) |

## `anthropic`

Sheet watch's latest classification: **copy change (2026-10-29)**.

### Missing from the page

- `claude-fable-5` — on the sheet, no row found on the page
- `claude-haiku-4-5` — on the sheet, no row found on the page
- `claude-opus-4-5` — on the sheet, no row found on the page
- `claude-opus-4-6` — on the sheet, no row found on the page
- `claude-opus-4-7` — on the sheet, no row found on the page
- `claude-opus-4-8` — on the sheet, no row found on the page
- `claude-opus-5` — on the sheet, no row found on the page
- `claude-sonnet-4-5` — on the sheet, no row found on the page
- `claude-sonnet-4-6` — on the sheet, no row found on the page
- `claude-sonnet-5` — on the sheet, no row found on the page

## `google`

Sheet watch's latest classification: **copy change (2026-10-29)**.

### Mismatches

| model | field | page | sheet | note |
| --- | --- | --- | --- | --- |
| `gemini-3.1-pro-preview` | fast_input | $3.60 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.1-pro-preview` | fast_output | $21.60 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.5-flash` | input | $0.30 | $1.50 |  |
| `gemini-3.5-flash` | output | $2.50 | $9.00 |  |
| `gemini-3.5-flash` | batch_input | $0.15 | $0.75 |  |
| `gemini-3.5-flash` | batch_output | $1.25 | $4.50 |  |
| `gemini-3.5-flash` | fast_input | $0.54 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.5-flash` | fast_output | $4.50 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.5-flash-lite` | fast_input | $0.54 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.5-flash-lite` | fast_output | $4.50 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.6-flash` | fast_input | $1.35 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.6-flash` | fast_output | $6.75 | — | the page publishes this tier; the sheet carries no row for it |

### Missing from the page

- `gemini-3.7-flash` — on the sheet, no row found on the page

### On the page, not on the sheet (26)

Informational. The sheet omits models on purpose; see the comments in `prices.py` before adding one.

`gemini-2.5-flash`, `gemini-2.5-flash-image`, `gemini-2.5-flash-lite`, `gemini-2.5-flash-native-audio-preview-12-2025`, `gemini-2.5-flash-preview-tts`, `gemini-2.5-pro`, `gemini-2.5-pro-preview-tts`, `gemini-3-flash-preview`, `gemini-3-pro-image`, `gemini-3.1-flash-image`, `gemini-3.1-flash-lite`, `gemini-3.1-flash-lite-image`, `gemini-3.1-flash-tts-preview`, `gemini-3.1-pro-preview-customtools`, `gemini-3.5-live-translate-preview`, `gemini-3.5-transcribe`, `gemini-3.5-transcribe-live`, `gemini-3.8-flash`, `gemini-3.8-flash-lite-tts`, `gemini-3.8-flash-tts`, `gemini-4-argon`, `gemini-embedding-001`, `gemini-nano-banana-2.1`, `gemini-omni-1.1-flash`, `gemini-robotics-er-2-preview`, `gemini-robotics-er-2-streaming-preview`

## `groq`

Sheet watch's latest classification: **copy change (2026-10-09)**.

### Unverifiable (1)

Not compared, and not counted as agreement.

- groq.com/pricing renders its rate table client-side — the committed page text holds no per-model rates to reconcile against — 1 field(s)

## `mistral`

Sheet watch's latest classification: **price change (2026-10-29)**.

### Missing from the page

- `codestral` — on the sheet, no row found on the page
- `glm-5-2` — on the sheet, no row found on the page
- `ministral-14b` — on the sheet, no row found on the page
- `ministral-3b` — on the sheet, no row found on the page
- `ministral-8b` — on the sheet, no row found on the page
- `mistral-embed` — on the sheet, no row found on the page
- `mistral-large` — on the sheet, no row found on the page
- `mistral-medium` — on the sheet, no row found on the page
- `mistral-small` — on the sheet, no row found on the page
- `zai-glm-5-2` — on the sheet, no row found on the page

## `openai`

Sheet watch's latest classification: **copy change (2026-10-29)**.

### Mismatches

| model | field | page | sheet | note |
| --- | --- | --- | --- | --- |
| `gpt-5.6-sol` | batch_input | $4.00 | $2.00 |  |
| `gpt-5.6-sol` | batch_output | $20.00 | $10.00 |  |

### Missing from the page

- `gpt-5.6-luna` — on the sheet, no row found on the page
- `gpt-5.6-terra` — on the sheet, no row found on the page

### Unverifiable (4)

Not compared, and not counted as agreement.

- no figure for this field in the page text — 4 field(s)

### On the page, not on the sheet (9)

Informational. The sheet omits models on purpose; see the comments in `prices.py` before adding one.

`chat-latest`, `gpt-5.3-codex`, `gpt-5.6-cyber`, `gpt-6-astra`, `gpt-6-luna`, `gpt-6.1-sol`, `gpt-6.1-terra`, `gpt-rosalind-discovery`, `gpt-rosalind-research`
