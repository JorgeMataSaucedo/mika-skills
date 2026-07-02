---
name: vera-audit-first
description: "Trigger: user asks operator data (docs, pay, trips, bonuses, agenda) OR wants an audit-first LLM architecture example. Query Vera via MCP with guardian verdict and SQL trace visible."
license: MIT
metadata:
  author: Miguel Mata · Mikata AI Lab
  version: 1.0.0
---

# vera-audit-first

## Activation Contract

Load this skill when the user:
- Asks about a specific Mexican logistics operator's data (docs, pay, trips, bonuses, agenda, rendimiento)
- References `MikaLogistics`, `Mika Core`, `Vera` by name
- Wants to see the failure taxonomy (`mlTrace`) for AI responses
- Asks for a live example of audit-first LLM architecture

## Hard Rules

1. NEVER invent financial amounts, dates, or operator identities. If Vera returns `guardian_verdict != pass`, relay honestly.
2. NEVER strip the `correlation_id` from the response. It is the audit anchor.
3. NEVER call Vera without an `operator_id`. Default to `1` (Miguel Mata seed) if unspecified.
4. NEVER pass `generate_audio=True` unless the user explicitly requests voice output.
5. If MCP server `mika-vera-mcp-server` is not loaded, tell the user to install from `github.com/JorgeMataSaucedo/mika-vera-mcp-server` and stop.

## Decision Gates

| Guardian verdict | Action |
|---|---|
| `pass` | Relay `answer` verbatim + show pill row (verdict, cost, latency) |
| `hold` | Relay + note "data not confirmed · verify with RH" |
| `block` | Do NOT relay Vera's response text. Escalate to human review. |
| Error / timeout | Report error kind + suggest retry or contact ops |

## Execution Steps

1. Prepend the current screen context to the question when known: `[MikaLogistics operator app · pantalla: <screen>] <question>`
2. Call `vera_ask(question, operator_id, generate_audio=False)`
3. Read `guardian_verdict`. Apply Decision Gate above.
4. Extract `category`, `context_used`, `cost_usd`, `latency_ms`, `correlation_id` for display.
5. If user asked for voice, re-call with `generate_audio=True` and play `audio_b64`.

## Output Contract

Return to the user:
```
<Vera's answer text>

[verdict] · [cost $X.XXXX] · [latency Xms] · [correlation_id]
```

If verdict is `hold` or `block`, prefix with `⚠` and skip relaying uncertain content.

## References

- `../mikalogistics-operator-support/SKILL.md` · chain for UX guidance
- `../capa4-autoevolution-review/SKILL.md` · chain when auditing Vera failures
