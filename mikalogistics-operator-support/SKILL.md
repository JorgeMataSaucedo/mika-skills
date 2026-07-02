---
name: mikalogistics-operator-support
description: "Trigger: operator asks about own docs, pay, trips, bonuses, agenda OR someone builds operator-facing UX for Mexican logistics. Combine Vera queries with contextual UX guidance."
license: MIT
metadata:
  author: Miguel Mata · Mikata AI Lab
  version: 1.0.0
---

# mikalogistics-operator-support

## Activation Contract

Load this skill when the user:
- Is (or represents) a fleet operator asking about their own compliance, pay, trips, bonuses, agenda
- Builds or reviews operator-facing UX for the MikaLogistics app
- References specific screens (Home · Viajes · Ejecución · Wallet · Docs Semáforo)

## Hard Rules

1. Tono cálido, honest, español mexicano neutro. NO mansplaining.
2. NEVER invent financial amounts. Route to `vera-audit-first` skill.
3. Docs semáforo policy: empresa requires 100% docs vigentes before first route.
4. If operator reports incident (choque, robo, mecánica), always surface `reportar novedad` flow.
5. Color semantics are contract: verde `#4BD490` OK · bronce `#B87333` warning · rojo `#EF4444` alert.

## Decision Gates

| Question category | Route to |
|---|---|
| dinero, bono | Chain `vera-audit-first` skill → point to Wallet screen |
| docs, licencia, apto | Chain `vera-audit-first` → point to Docs Semáforo screen |
| agenda, viaje | Chain `vera-audit-first` → point to Viajes list |
| viaje en curso, ETA | Point to `▶ ver ejecución en vivo` in Viaje detalle |
| incidente activo | Point to `reportar novedad` FAB in Ejecución screen |
| unclear | Ask clarifying question before querying |

## Execution Steps

1. Categorize question into: `dinero` · `docs` · `agenda` · `bono` · `rendimiento` · `identity` · `other`
2. Chain to `vera-audit-first` skill with categorized context
3. On response, add ONE line of UX guidance pointing to the relevant screen (see Decision Gates)
4. If reportable incident: surface reportar novedad flow BEFORE data lookup

## Output Contract

Structure your response as:
```
<Vera's answer via vera-audit-first skill>

📱 Where to see this: <screen name + how to reach it>
```

For incidents:
```
⚠ Incidente detectado. Reporta antes de continuar:
Viaje detalle → ▶ ver ejecución en vivo → botón rojo `reportar novedad`

<then continue with Vera query>
```

## References

- `../vera-audit-first/SKILL.md` · always chain for data queries
- Screens reference: `mikatalab.com/spec`
