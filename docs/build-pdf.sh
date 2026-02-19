#!/bin/bash
# build-pdf.sh — Compile the guide into a single bookmarked PDF
#
# Requires: pandoc, a LaTeX distribution (texlive)
# Called by the GitHub Actions workflow; can also be run locally.
#
# Usage: ./build-pdf.sh
# Output: guide.pdf in the docs/ directory

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Chapter order (matches nav_order in front matter)
CHAPTERS=(
  "index.md"
  "getting-started/why-ai-research.md"
  "getting-started/tools-setup.md"
  "the-flow/project-structure.md"
  "the-flow/your-first-session.md"
  "the-flow/ai-assisted-workflow.md"
  "the-flow/writing-with-ai.md"
  "reference/commands-cheatsheet.md"
  "reference/faq.md"
)

COMBINED="/tmp/guide-combined.md"
> "$COMBINED"

for chapter in "${CHAPTERS[@]}"; do
  if [[ ! -f "$chapter" ]]; then
    echo "Warning: $chapter not found, skipping" >&2
    continue
  fi

  # Strip YAML front matter (everything between first --- and second ---)
  # Then clean Jekyll-specific syntax
  awk '
    BEGIN { in_front=0; front_done=0 }
    /^---$/ && !front_done {
      in_front = !in_front
      if (!in_front) front_done = 1
      next
    }
    front_done { print }
  ' "$chapter" \
    | sed 's/{: \.fs-[0-9]* }//g' \
    | sed 's/{: \.fw-[0-9]* }//g' \
    | sed 's/{: \.tip }/> **Tip**/g' \
    | sed 's/{: \.note }/> **Note**/g' \
    | sed 's/{: \.important }/> **Important**/g' \
    | sed 's/{: \.warning }/> **Warning**/g' \
    | sed 's/{%[^%]*%}//g' \
    >> "$COMBINED"

  # Add a page break between chapters
  printf '\n\\newpage\n\n' >> "$COMBINED"
done

# Build PDF with pandoc
pandoc "$COMBINED" \
  -o guide.pdf \
  --pdf-engine=xelatex \
  --toc \
  --toc-depth=2 \
  -V documentclass=report \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V urlcolor=blue \
  -V toccolor=black \
  --metadata title="An AI-Assisted Research Flow" \
  --metadata subtitle="A practical guide for empirical researchers" \
  --metadata author="Dr. Jared L. Black" \
  --metadata date="$(date +%B\ %Y)"

echo "Built: $SCRIPT_DIR/guide.pdf"
