# Changelog

## [1.0.0] - 2026-07-03

### Added
- Initial 4 Anthropic Skills for Mika Core:
  - `vera-audit-first` · query Vera with guardian verdict routing
  - `mikalogistics-operator-support` · operator UX + Vera chain
  - `capa4-autoevolution-review` · pending proposals by tier + rollback audit
  - `mos-rh-multi-ia-consult` · 4-6 IA voting with dissent tracking
- All skills refactored to LLM-first style (gentle-ai inspired):
  - Frontmatter with `name`, single-line quoted `description` (Trigger: ..., <=250 chars), `license`, `metadata.author`, `metadata.version`
  - Required section order: Activation Contract → Hard Rules → Decision Gates → Execution Steps → Output Contract → References
  - Body budget respected (300-500 tokens each)
  - Imperative language ("Load X · Check Y · Return Z")
- README with install instructions for Claude Desktop + Claude Code
- MIT LICENSE
- Validation script `tests/validate_skills.py` enforcing style guide
- GitHub Actions CI

### Attribution
Style guide inspired by [Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai) LLM-first skill format.

## [Unreleased]

### Planned
- `mika-skill-creator` · meta-skill to author new skills following the guide
- `mika-judgment-day` · adversarial review of Mika responses
- `mika-onboarding-vertical` · scaffold new tenant vertical
