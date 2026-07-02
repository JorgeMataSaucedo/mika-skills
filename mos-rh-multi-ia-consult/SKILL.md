---
name: mos-rh-multi-ia-consult
description: Consult 4-6 Western AI models simultaneously on a real HR case for Mexican fleet operators · Sonnet 5 + Opus 4.7 + Fable 5 + GPT-5 + Gemini + DeepSeek · Mika orchestrates voting synthesis with dedup of conditions. Use when the user has a genuinely difficult hiring, promotion, disciplinary, or termination decision AND wants multi-model consensus with explicit dissent tracked.
---

# mos-rh-multi-ia-consult

You are orchestrating a **multi-IA consultation** on a real HR case for Mexican logistics fleet operators. The output is not a single opinion · it's a **structured voting synthesis** with explicit dissent tracking and deduped condition aggregation.

## When to use this skill

- User has a genuinely difficult HR decision (hire · promote · discipline · terminate · restructure)
- User wants multi-model consensus with dissent visibility (not just "ask one LLM")
- User is building MOS RH product features
- User wants to demonstrate multi-AI orchestration for portfolio purposes

**DON'T use for**: simple questions, casual chat, or when a single LLM opinion is enough.

## The 4-6 AI models orchestrated

**Anthropic**:
- `claude-sonnet-5` · cost-efficient · 96% golden set PASS
- `claude-opus-4-7` · high reasoning · 3x cost of Sonnet 5
- `claude-fable-5` · Anthropic Mythos-class · experimental

**OpenAI**:
- `gpt-5` · reasoning_effort tunable

**Google** (optional if `MIKA_GEMINI_API_KEY` configured):
- `gemini-3-pro` · Google's flagship

**DeepSeek** (optional if `MIKA_DEEPSEEK_API_KEY` configured):
- `deepseek-chat` · Chinese frontier · counterweight to Western consensus

## How to consult

### Step 1 · Structure the HR case

The case MUST include:
- Candidato/empleado data (edad · experiencia · docs · referencias)
- Contexto empresa (rotación · vacantes · políticas)
- Pregunta concreta (contratar · rechazar · condiciones)

Example:
```
CANDIDATO · Operador de camión
- Edad: 38 · Experiencia: 8 meses
- Licencia federal Tipo E: VENCIDA hace 45 días
- Apto médico: vigente
- Referencias: 1 positiva · 1 neutral con impuntualidad

Empresa:
- Flotilla 50+ unidades
- Rotación 24% · 2 vacantes 6 semanas

PREGUNTA: ¿Contratar, rechazar, o hire_with_conditions?
```

### Step 2 · Send to all available models in parallel

Each model responds in structured JSON:
```json
{
  "decision": "hire | reject | hire_with_conditions",
  "confidence": 0-100,
  "reasoning": "1-3 frases honest",
  "risk_flags": ["flag1", "flag2"],
  "conditions": ["condicion1"],
  "one_line_summary": "10-15 palabras"
}
```

### Step 3 · Mika orchestrates the voting synthesis

- **Majority vote** on `decision` field
- **Deduplicate conditions** (Levenshtein or semantic similarity)
- **Track dissent explicitly** · which models voted differently and why
- **Highlight unique contributions** · what each model added that others missed

### Step 4 · Present the synthesis

Report format:
```
CONSENSUS: <majority decision> · N/M models

CONDITIONS (deduped):
- <condition 1> [S,O,F,G] ← models that proposed
- <condition 2> [S,F] ← only Sonnet 5 + Fable 5
...

DISSENT:
- <model X>: <decision Y> · <reasoning>

UNIQUE CONTRIBUTIONS:
- Model X uniquely added: <what>
- Model Y uniquely added: <what>
```

## Canon rules for multi-IA consult

1. **Nunca ocultar dissent** · si un modelo discrepa, se reporta con reasoning
2. **Dedup honesto de condiciones** · agregar solo si son funcionalmente distintas
3. **Highlight diferenciales** · qué aportó cada modelo que otros no
4. **Costo tracking** · reportar total USD y latency
5. **Failure taxonomy** · si un modelo falló (parse error · timeout · api error), reportarlo explícitamente

## First orchestration proof (2026-07-03)

Real case tested: Operator Tipo E · licencia vencida 45 días · experiencia 8 meses · referencia impuntual.

Result: **4/4 models → hire_with_conditions** (Sonnet 5, Opus 4.7, Fable 5, GPT-5)

Consensus conditions (universal):
- Renovar licencia federal antes de primera ruta
- Periodo prueba 60-90 días
- Rutas iniciales con operador senior
- Capacitación doble remolque

Diferenciales por modelo:
- **GPT-5** unique: "Cláusula de rescisión si no renueva licencia en 10 días hábiles" (legal timing)
- **Opus 4.7** unique: "Validar referencia neutral con llamada directa" (due diligence)
- **Fable 5** unique: "Evaluación práctica de manejo con doble remolque supervisada" (experiential)
- **Sonnet 5** unique: "Asignar rutas cortas primeras 4 semanas" (progressive complexity)

## Reference

- Script: `mika-core/_track3_mos_rh_multiIA.py`
- MOS RH product: internal Dtroy engagement (Mikata AI Lab)
- Portfolio blog post: `mikatalab.com/blog/multi-ia-consensus` (semana 4)

**Infraestructura: Mika · Mikata AI Lab 🎀**
