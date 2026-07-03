"""Validation script for SKILL.md files.

Enforces LLM-first style guide:
- Frontmatter with name, description (single-line, starts with 'Trigger:', <=250 chars), license, metadata
- Required body sections in order: Activation Contract, Hard Rules, Decision Gates, Execution Steps, Output Contract, References
- Body budget: warn >700 chars in Markdown, hard fail >2000 (proxy for tokens)

Usage:
  python tests/validate_skills.py

Exit code 0 if all pass, 1 if any fail.
"""
import sys
import re
from pathlib import Path


REQUIRED_SECTIONS = [
    "## Activation Contract",
    "## Hard Rules",
    "## Decision Gates",
    "## Execution Steps",
    "## Output Contract",
    "## References",
]
DESCRIPTION_MAX = 250
BODY_WARN_TOKENS = 700
BODY_HARD_CAP = 2000  # rough char cap; adjust if we integrate tiktoken


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        return None, text
    fm_raw, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_raw.split("\n"):
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, body


def validate_skill(skill_path):
    errors = []
    warnings = []

    text = skill_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    if fm is None:
        errors.append("missing frontmatter (---...---)")
        return errors, warnings

    # Frontmatter checks
    for key in ("name", "description", "license"):
        if key not in fm:
            errors.append(f"frontmatter missing '{key}'")

    desc = fm.get("description", "")
    if desc:
        if len(desc) > DESCRIPTION_MAX:
            errors.append(f"description too long ({len(desc)} > {DESCRIPTION_MAX})")
        if not desc.lower().startswith("trigger:"):
            warnings.append("description should start with 'Trigger: ...'")
        if "\n" in desc:
            errors.append("description must be single physical line")

    # Section order
    positions = []
    for section in REQUIRED_SECTIONS:
        idx = body.find(section)
        if idx == -1:
            errors.append(f"missing required section '{section}'")
        else:
            positions.append((idx, section))

    positions.sort()
    ordered_names = [n for _, n in positions]
    if ordered_names != [s for s in REQUIRED_SECTIONS if s in ordered_names]:
        errors.append(f"sections out of order: got {ordered_names}")

    # Body budget (rough char count)
    body_chars = len(body)
    if body_chars > BODY_HARD_CAP:
        errors.append(f"body too long ({body_chars} > {BODY_HARD_CAP} chars, hard cap)")
    elif body_chars > BODY_WARN_TOKENS * 4:  # rough: 1 token ≈ 4 chars
        warnings.append(f"body approaching cap ({body_chars} chars, warn >{BODY_WARN_TOKENS*4})")

    return errors, warnings


def main():
    root = Path(__file__).parent.parent
    skill_files = sorted(root.glob("*/SKILL.md"))

    if not skill_files:
        print("No SKILL.md files found")
        return 1

    total_errors = 0
    for skill in skill_files:
        errors, warnings = validate_skill(skill)
        rel = skill.relative_to(root)
        if errors:
            print(f"✗ {rel}")
            for e in errors:
                print(f"    ERROR: {e}")
            total_errors += len(errors)
        elif warnings:
            print(f"⚠ {rel}")
            for w in warnings:
                print(f"    WARN: {w}")
        else:
            print(f"✓ {rel}")

    print(f"\n{len(skill_files)} skills · {total_errors} errors")
    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
