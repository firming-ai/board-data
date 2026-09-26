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

Reconciled 2026-09-26 against `firming.prices` sheet **2026-08-30**.

| source | status | mismatches | missing | unverifiable | models on page | classification |
| --- | --- | --- | --- | --- | --- | --- |
| `anthropic` | **drift** | 4 | 8 | 8 | 3 | unclassified (2026-09-24) |
| `google` | **drift** | 10 | 0 | 0 | 31 | price change (2026-09-25) |
| `groq` | skipped | 0 | 0 | 1 | 0 | copy change (2026-09-25) |
| `mistral` | unreadable | 0 | 10 | 0 | 0 | copy change (2026-09-19) |
| `openai` | **drift** | 2 | 2 | 4 | 7 | copy change (2026-09-26) |

## `anthropic`

Sheet watch's latest classification: **unclassified (2026-09-24)**.

### Mismatches

| model | field | page | sheet | note |
| --- | --- | --- | --- | --- |
| `claude-opus-4-8` | input | $10.00 | $5.00 |  |
| `claude-opus-4-8` | output | $50.00 | $25.00 |  |
| `claude-opus-5` | input | $10.00 | $5.00 |  |
| `claude-opus-5` | output | $50.00 | $25.00 |  |

### Missing from the page

- `claude-fable-5` — on the sheet, no row found on the page
- `claude-haiku-4-5` — on the sheet, no row found on the page
- `claude-opus-4-5` — on the sheet, no row found on the page
- `claude-opus-4-6` — on the sheet, no row found on the page
- `claude-opus-4-7` — on the sheet, no row found on the page
- `claude-sonnet-4-5` — on the sheet, no row found on the page
- `claude-sonnet-4-6` — on the sheet, no row found on the page
- `claude-sonnet-5` — on the sheet, no row found on the page

### Unverifiable (8)

Not compared, and not counted as agreement.

- no figure for this field in the page text — 8 field(s)

### On the page, not on the sheet (1)

Informational. The sheet omits models on purpose; see the comments in `prices.py` before adding one.

`claude-opus-5-5`

## `google`

Sheet watch's latest classification: **price change (2026-09-25)**.

### Mismatches

| model | field | page | sheet | note |
| --- | --- | --- | --- | --- |
| `gemini-3.1-pro-preview` | fast_input | $3.60 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.1-pro-preview` | fast_output | $21.60 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.5-flash` | fast_input | $2.70 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.5-flash` | fast_output | $16.20 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.5-flash-lite` | fast_input | $0.54 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.5-flash-lite` | fast_output | $4.50 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.6-flash` | fast_input | $1.35 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.6-flash` | fast_output | $6.75 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.7-flash` | fast_input | $1.35 | — | the page publishes this tier; the sheet carries no row for it |
| `gemini-3.7-flash` | fast_output | $6.75 | — | the page publishes this tier; the sheet carries no row for it |

### On the page, not on the sheet (25)

Informational. The sheet omits models on purpose; see the comments in `prices.py` before adding one.

`gemini-2.5-computer-use-preview-10-2025`, `gemini-2.5-flash`, `gemini-2.5-flash-image`, `gemini-2.5-flash-lite`, `gemini-2.5-flash-native-audio-preview-12-2025`, `gemini-2.5-flash-preview-tts`, `gemini-2.5-pro`, `gemini-2.5-pro-preview-tts`, `gemini-3-flash-preview`, `gemini-3-pro-image`, `gemini-3.1-flash-image`, `gemini-3.1-flash-lite`, `gemini-3.1-flash-lite-image`, `gemini-3.1-flash-tts-preview`, `gemini-3.1-pro-preview-customtools`, `gemini-3.5-live-translate-preview`, `gemini-3.5-transcribe`, `gemini-3.5-transcribe-live`, `gemini-3.8-flash`, `gemini-3.8-flash-lite-tts`, `gemini-3.8-flash-tts`, `gemini-omni-1.1-flash`, `gemini-omni-flash-preview`, `gemini-robotics-er-2-preview`, `gemini-robotics-er-2-streaming-preview`

## `groq`

Sheet watch's latest classification: **copy change (2026-09-25)**.

### Unverifiable (1)

Not compared, and not counted as agreement.

- groq.com/pricing renders its rate table client-side — the committed page text holds no per-model rates to reconcile against — 1 field(s)

## `mistral`

Sheet watch's latest classification: **copy change (2026-09-19)**.

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

Sheet watch's latest classification: **copy change (2026-09-26)**.

### Mismatches

| model | field | page | sheet | note |
| --- | --- | --- | --- | --- |
| `gpt-5.6-sol` | fast_input | $4.00 | $8.00 |  |
| `gpt-5.6-sol` | fast_output | $20.00 | $40.00 |  |

### Missing from the page

- `gpt-5.6-luna` — on the sheet, no row found on the page
- `gpt-5.6-terra` — on the sheet, no row found on the page

### Unverifiable (4)

Not compared, and not counted as agreement.

- no figure for this field in the page text — 4 field(s)

### On the page, not on the sheet (6)

Informational. The sheet omits models on purpose; see the comments in `prices.py` before adding one.

`chat-latest`, `gpt-5.3-codex`, `gpt-6-astra`, `gpt-6-luna`, `gpt-6-sol`, `gpt-rosalind-research`
