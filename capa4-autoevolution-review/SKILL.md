---
name: capa4-autoevolution-review
description: "Trigger: user reviews Mika Core Capa 4 pending proposals, recent commits, or rollbacks. Present by ApprovalTierCode with dissent visible; enforce human approval required."
license: MIT
metadata:
  author: Miguel Mata · Mikata AI Lab
  version: 1.0.0
---

# capa4-autoevolution-review

## Activation Contract

Load this skill when the user:
- Asks *"¿qué propuestas están pending?"* or similar
- Wants to inspect a specific `ProposalId`, `CommitId`, or rollback
- Audits Mika's self-modification loop
- Asks the diff between Capa 3 (agencia) and Capa 4 (autoevolución)

## Hard Rules

1. NEVER auto-approve. Every proposal requires explicit Mikata approval.
2. NEVER modify `IsProtected=1` memories. They are canon inmutable.
3. NEVER hide dissent. If Mika proposed vs previous rejection, surface the `ParentRejectedProposalId` link.
4. Auto-rollback threshold is `PostPct < 90%`. Report it verbatim; do not soften.
5. Skip runs when local day is Saturday (canon salud sagrada) or hour ≥ 22 (corte 10pm).

## Decision Gates

| ApprovalTierCode | Review recommendation |
|---|---|
| `TIER_LOW` (risk<30) | Quick review, simple notification, likely safe |
| `TIER_MEDIUM` (30-70) | Define KPI to watch post-apply, shadow observation plan |
| `TIER_HIGH` (>70) | Require side-by-side before/after; check 24h cooldown on same target |

| Commit state | Action |
|---|---|
| `VerifyStatusCode=PENDING` | Block any new apply on same target |
| `VerifyStatusCode=FAIL_ROLLBACK` | Show baseline vs post + `RollbackReasonText` |
| `IsProtected=1` | Note exempt from auto-rollback |

## Execution Steps

1. Call `mika_autoevolution_pending()` to list PROPOSED by tier
2. Present TIER_HIGH first, then MEDIUM, then LOW
3. For each: show `ProposalId · type · target · risk · rationale (200 chars) · ParentRejected if any · days pending`
4. Call `mika_autoevolution_commits(limit=10)` for recent history
5. Highlight any `FAIL_ROLLBACK` with reason + baseline delta

## Output Contract

Return structured markdown:
```
## Pending Proposals

### TIER_HIGH
- #<id> · <type> → <target> · risk <n>/100 · <n>d pending
  Rationale: <200 chars>
  Parent rejected: #<pid> · Reason: <100 chars>

### TIER_MEDIUM
...

### TIER_LOW
...

## Recent Commits (last 7d)
- #<cid> · <target> · baseline <n>% → post <n>% · <verify>
  <if FAIL_ROLLBACK: rollback reason>
```

## References

- `../vera-audit-first/SKILL.md` · chain when reviewing hallucination-driven proposals
- Live schema: tables `AutoevoluProposal` · `AutoevoluCommit`
