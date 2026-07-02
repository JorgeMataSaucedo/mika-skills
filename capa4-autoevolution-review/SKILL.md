---
name: capa4-autoevolution-review
description: Review Mika Core Capa 4 autoevolution proposals · Mika observes her own failures + proposes catalog updates · zero auto-merge · human approval required. Use when the user asks to review pending proposals, understand a specific commit's rollback, or audit the autoevolution loop. Chain with mika-vera-mcp-server for live data.
---

# capa4-autoevolution-review

You are helping the user review **Capa 4 autoevolución** proposals for Mika Core. Mika observes her own operational failures (mlTrace, guardian verdicts, latency, hallucinations) and proposes concrete updates to her own catalog · zero auto-merge · every change goes through human approval + verify against golden set.

## When to use this skill

- User asks *"¿qué propuestas están pending?"*
- User wants to see recent commits from autoevolución
- User inspects a specific ProposalId or CommitId
- User wants to audit the autoevolution loop end-to-end
- User asks about the diff between Capa 3 (agencia) and Capa 4 (autoevolución)

## Canon rules Capa 4 respects (verbatim)

1. **Nunca auto-merge** · every proposal requires Mikata's explicit approval via AgencyApproval workflow
2. **Rollback automático** if golden set post-apply < 90% baseline
3. **Zero cambios en IsProtected** memories (canon inmutable)
4. **Feedback loop honest** · Mika reads `rejection_reason` from previous rejections and doesn't repeat without new evidence
5. **Post-mortem log público** when rollback triggers
6. **Sábado auto-paused** · canon salud sagrada
7. **Corte 10pm respetado** · notifications posponed to next work day

## Tier system (v2 · post Sonnet 5 review)

`ApprovalTierCode` computed automatically from `RiskScoreInt`:

- **TIER_LOW** (risk < 30) · simple notification · approval normal
- **TIER_MEDIUM** (30-70) · shadow observation post-apply · approval + monitor
- **TIER_HIGH** (> 70) · approval explícito with expanded context · cooldown 24h

## Similarity check (v2 · fix Sonnet 5 review)

Before proposing a new change on a target with rejected history:
- Mika reads `vw_AutoevoluRejectedRecent` (last 30 days)
- If overlap with rejected: MUST include `parent_rejected_proposal_id` + justify what evidence is new
- If no overlap: explicit note in rationale

## Available MCP tools (from mika-vera-mcp-server)

- `mika_autoevolution_observe()` · resumen operacional last 24h
- `mika_autoevolution_pending()` · pending proposals by tier
- `mika_autoevolution_commits(limit=10)` · recent commits with verify status

## Review workflow

### Step 1 · List pending proposals
```
mika_autoevolution_pending()
```

Show by tier. Highlight TIER_HIGH first (they need cooldown + context).

### Step 2 · For each pending, show:
- ProposalId · type · target · risk · tier
- Rationale (first 200 chars)
- ParentRejectedProposalId if any (with reason for retry)
- Days pending

### Step 3 · Recommend action per tier

- **TIER_LOW** · likely safe · quick review
- **TIER_MEDIUM** · requires shadow observation plan · define KPI to watch post-apply
- **TIER_HIGH** · requires side-by-side before/after · check cooldown status (24h since last same-target apply)

### Step 4 · Check recent commits

```
mika_autoevolution_commits(limit=10)
```

Look for:
- `VerifyStatusCode = FAIL_ROLLBACK` (auto-rollback triggered)
- Commits where PostPct < BaselinePct
- IsProtected commits (exempt from auto-rollback)

### Step 5 · Explain rollback if any

If a recent commit rolled back:
- Show baseline vs post
- Show `RollbackReasonText`
- Suggest what evidence Mika needs next time (feedback loop honest)

## Diff Capa 3 vs Capa 4

| | Capa 3 · Agencia | Capa 4 · Autoevolución |
|---|---|---|
| Rol | Mika ejecuta con límites | Mika modifica sus propios límites |
| Trigger | User request | Nightly cron 23:45 (skipping sábado) |
| Approval | Via AgencyPolicy | Via AgencyApproval + tier gating |
| Learning | Read-only observation | Propose + apply after human approve |
| Rollback | Manual | Auto if post < 90% golden set |

## Reference

- Design draft: `mikatalab.com/blog/capa4-autoevolucion` (semana 3)
- Live schema: tables `AutoevoluProposal` · `AutoevoluCommit` · views `vw_AutoevoluPending` · `vw_AutoevoluTieredApprovals`
- Cron script: `autoevolution_nightly.py` @ 23:45 daily
- MCP server: `github.com/JorgeMataSaucedo/mika-vera-mcp-server`

**Infraestructura: Mika · Mikata AI Lab 🎀**
