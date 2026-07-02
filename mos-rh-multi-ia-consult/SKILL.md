---
name: mos-rh-multi-ia-consult
description: "Trigger: difficult Mexican logistics HR decision (hire, promote, discipline, terminate) needing 4-6 IA consensus with explicit dissent. Orchestrate voting synthesis and deduped condition aggregation."
license: MIT
metadata:
  author: Miguel Mata · Mikata AI Lab
  version: 1.0.0
---

# mos-rh-multi-ia-consult

## Activation Contract

Load this skill when the user:
- Presents a real HR case for a fleet operator (candidato/empleado data + empresa contexto + concrete question)
- Explicitly wants **multi-model consensus** (not a single opinion)
- Builds MOS RH product features
- Needs to demonstrate multi-AI orchestration for portfolio

Do NOT load for casual chat or when one LLM is enough.

## Hard Rules

1. NEVER hide dissent. If any model disagrees, report its decision + reasoning.
2. NEVER skip a required data field. Structured case MUST include operator data + empresa context + concrete question.
3. Dedupe conditions ONLY when functionally equivalent (same intent, different wording). Do NOT merge distinct constraints.
4. NEVER report a decision without confidence + one-line summary from each model.
5. Report cost and latency per model. Portfolio artifact requires transparency.

## Decision Gates

| Available API keys in env | Models to call |
|---|---|
| Anthropic only | Sonnet 5 · Opus 4.7 · Fable 5 (3-way Anthropic) |
| Anthropic + OpenAI | + GPT-5 (4-way West) |
| + `MIKA_GEMINI_API_KEY` | + Gemini 3 Pro (5-way) |
| + `MIKA_DEEPSEEK_API_KEY` | + DeepSeek Chat (6-way full zoo) |

| Consensus split | Report as |
|---|---|
| Unanimous | `CONSENSUS: <decision> · N/N models` |
| Majority ≥60% | `MAJORITY: <decision> · N/M · DISSENT: <models>` |
| Even split | `DEADLOCK · escalate to human` |

## Execution Steps

1. Validate case has all required fields; if missing, ask before calling
2. Dispatch parallel calls to all available models via `_track3_mos_rh_multiIA.py`
3. Parse each response as JSON strict; on parse error, retry once with explicit "JSON only" prompt
4. Group by `decision` field; count votes
5. Dedupe conditions from majority voters (keep unique intent)
6. Extract unique contributions per model (what only that model added)

## Output Contract

```
CONSENSUS / MAJORITY / DEADLOCK: <decision> · N/M models

DISSENT:
- <ModelName>: <decision> · <reasoning one-liner>

CONDITIONS (deduped from N models):
- <condition 1> · voted by [S, O, F, G]
- <condition 2> · voted by [S, F]

UNIQUE CONTRIBUTIONS:
- <Model>: added "<condition text>" not in any other model
- ...

METRICS:
- Total cost: $X.XXXX
- Avg latency: Xs
- Failed models: <none | list>
```

## References

- Script: `mika-core/_track3_mos_rh_multiIA.py`
- `../vera-audit-first/SKILL.md` · chain when case includes operator data lookup
