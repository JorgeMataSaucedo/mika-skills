# mika-skills

**Anthropic Skills** for [Mika Core](https://mikatalab.com/spec) · progressive-disclosure expertise packages that Claude loads on-demand.

Skills are the application layer above [MCP](https://modelcontextprotocol.io) · complementary to [mika-vera-mcp-server](https://github.com/JorgeMataSaucedo/mika-vera-mcp-server).

## The 4 Skills

| Skill | Trigger | Purpose |
|---|---|---|
| **vera-audit-first** | User asks operator data OR wants audit-first LLM example | Query Vera with full trace visibility |
| **mikalogistics-operator-support** | Operator asks about docs, pay, trips, bonuses | Contextual operator support + UX guidance |
| **capa4-autoevolution-review** | User asks about pending proposals, commits, rollbacks | Review Mika's self-modification loop |
| **mos-rh-multi-ia-consult** | Difficult HR decision needing multi-model consensus | Orchestrate 4-6 IAs vote with dissent tracking |

## Install

### Claude Code

```bash
# Clone this repo somewhere accessible
git clone https://github.com/JorgeMataSaucedo/mika-skills ~/mika-skills

# Copy skills to Claude's skills directory
cp -r ~/mika-skills/* ~/.claude/skills/
```

### Claude Desktop

Skills are loaded from `~/Library/Application Support/Claude/skills/` (macOS) or `%APPDATA%\Claude\skills\` (Windows).

## Dependencies

Most skills chain with `mika-vera-mcp-server` for live data. Install it:

```bash
git clone https://github.com/JorgeMataSaucedo/mika-vera-mcp-server
```

And configure Claude Desktop/Code to load the MCP server (see that repo's README).

## Canon

All skills respect:

1. **Zero cross-tenant memory** · Vera is isolated per vertical
2. **Failure taxonomy visible** · `mlTrace` anonymized public
3. **Guardian semantic** filters every LLM output
4. **Silencio honesto antes que ficción cómoda** · no invented data
5. **Sábado: cero código** · canon salud (Mikata rule)
6. **Corte 10pm sagrado** · nightly boundary

## Portfolio Mikata AI Lab 2027

Applying to Applied AI · Forward Deployed Engineer roles for Q1 2027.

- **Public repos**: `mika-vera-mcp-server` · `mika-skills` · `mikatalab-blog`
- **Live spec**: [mikatalab.com/spec](https://mikatalab.com/spec)
- **Autoría**: Miguel Mata · [mikatalab.com](https://mikatalab.com)

**Infraestructura: Mika · Mikata AI Lab 🎀**
