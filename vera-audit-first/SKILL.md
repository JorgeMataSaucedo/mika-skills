---
name: vera-audit-first
description: Ask Vera · audit-first AI assistant for Mexican logistics operators. Every response traceable to a SQL row · zero cross-tenant memory by design · guardian verdict per query. Use when the user asks about operator data (docs, pay, trips, bonuses, agenda) OR wants to see the failure taxonomy for AI responses OR needs an example of audit-first LLM architecture.
---

# vera-audit-first

You have access to **Vera** · a production audit-first assistant serving Mexican fleet operators. Every response is traceable to a specific SQL row · zero cross-tenant memory by design · guardian semantic filter runs on every output.

## When to use this skill

Trigger this skill when:

- User asks operator-level questions (**"¿cuándo vence mi licencia?"** · **"¿cuánto voy a cobrar?"** · **"¿por qué me redujeron el bono?"**)
- User wants to inspect Vera's failure taxonomy (`mlTrace` table anonymized)
- User needs a live example of audit-first LLM architecture (for reference, presentation, or teaching)
- User references **MikaLogistics · Mika Core · Vera** by name

## How to use

Call the MCP tool `vera_ask` from `mika-vera-mcp-server` with the operator question. If the server isn't loaded, install it first from `github.com/JorgeMataSaucedo/mika-vera-mcp-server`.

```
vera_ask(question="¿cuándo vence mi licencia federal?", operator_id=1)
```

Response includes:

- `answer` · Vera's response in Spanish
- `guardian_verdict` · `pass` | `hold` | `block`
- `category` · docs · dinero · agenda · bono · rendimiento · identity
- `context_used` · list of SQL tables consulted
- `cost_usd` · per-query cost
- `latency_ms` · total latency
- `correlation_id` · UUID for cross-reference in `mlTrace`

## Canon rules Vera respects (verbatim from system prompt)

1. **"No construir canon que no existe"** · Vera refuses to confirm fake history even if user insists
2. **"Silencio honesto antes que ficción cómoda"** · Vera says *"no lo tengo, pregúntale a RH"* when data missing
3. **Zero cross-tenant memory** · each vertical is isolated instance
4. **Guardian semantic filter** runs post-generation before user sees response

## Golden set metrics (2026-07-02 · Sonnet 5 in Azure production)

- 48/50 PASS (96%)
- 3/3 PASS on identity attacks (0 rope-in to fake canon)
- Avg cost: $0.003 per query
- p50 latency: 2.2s · p95: 3.4s

## Failure taxonomy visible

Use `vera_trace_summary(hours=24)` to see the last day's queries: categories, guardian verdicts, error flags, hallucination suspects, cost, latency. This is the artifact that separates portfolio from engineering.

## Voice output

Pass `generate_audio=True` to get MP3 base64 · voice **Coral** (OpenAI `gpt-4o-mini-tts` · Mexican Spanish · warm energetic feminine).

## Reference

- Public repo: `github.com/JorgeMataSaucedo/mika-vera-mcp-server`
- Live spec: `mikatalab.com/spec` · `mikatalab.com/vera`
- Post announcement (blog): `mikatalab.com/blog/vera-announcement`

**Infraestructura: Mika · Mikata AI Lab 🎀**
