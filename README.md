# mika-skills

**Anthropic Skills** for [Mika Core](https://mikatalab.com/spec) · LLM-first runtime instruction contracts, not human docs.

Skills are the application layer above [MCP](https://modelcontextprotocol.io) · complementary to [mika-vera-mcp-server](https://github.com/JorgeMataSaucedo/mika-vera-mcp-server).

## Skills

| Skill | Trigger | Chain |
|---|---|---|
| **vera-audit-first** | User asks operator data OR wants audit-first LLM example | MCP tools `vera_ask`, `vera_trace_summary` |
| **mikalogistics-operator-support** | Operator asks docs/pay/trips/bonuses/agenda | Chains `vera-audit-first` + UX guidance |
| **capa4-autoevolution-review** | User reviews pending proposals/commits/rollbacks | MCP tools `mika_autoevolution_*` |
| **mos-rh-multi-ia-consult** | Difficult HR decision needing multi-model consensus | Multi-IA parallel dispatch script |

## Style

All skills follow the LLM-first style guide inspired by [gentle-ai](https://github.com/Gentleman-Programming/gentle-ai):

- Body budget 180-450 tokens (700 max)
- Required order: Activation Contract → Hard Rules → Decision Gates → Execution Steps → Output Contract → References
- Imperative language ("Load X · Check Y · Return Z")
- Frontmatter with `license`, `author`, `version`, single-line quoted `description` starting with `"Trigger: ..."`

## Install

### Claude Code

```bash
git clone https://github.com/JorgeMataSaucedo/mika-skills ~/mika-skills
cp -r ~/mika-skills/*/ ~/.claude/skills/
```

### Claude Desktop

Copy skill directories to `~/Library/Application Support/Claude/skills/` (macOS) or `%APPDATA%\Claude\skills\` (Windows).

## Dependencies

Most skills chain with `mika-vera-mcp-server` for live data. Install:

```bash
git clone https://github.com/JorgeMataSaucedo/mika-vera-mcp-server
```

Configure the MCP server in your Claude client (see that repo's README).

## Canon

All skills respect (verbatim):

1. Zero cross-tenant memory · Vera isolated per vertical
2. Failure taxonomy visible · `mlTrace` anonymized public
3. Guardian semantic filters every LLM output pre-user
4. Silence over fiction · no invented data
5. Sábado cero código · canon salud
6. Corte 10pm sagrado · nightly boundary

## License

MIT · see [LICENSE](LICENSE)

## Author

**Miguel Mata** · [mikatalab.com](https://mikatalab.com) · Applied AI / Forward Deployed Engineer 2027

**Infraestructura: Mika · Mikata AI Lab 🎀**
