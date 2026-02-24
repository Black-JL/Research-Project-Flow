#!/bin/bash
# build-pdf.sh — Compile the guide into a single bookmarked PDF
#
# Requires: pandoc, a LaTeX distribution (texlive), Eisvogel template
# Called by the GitHub Actions workflow; can also be run locally.
#
# Usage: ./build-pdf.sh
# Output: guide.pdf in the docs/ directory

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# --- Install Eisvogel template if not present ---
TEMPLATE_DIR="$HOME/.pandoc/templates"
if [[ ! -f "$TEMPLATE_DIR/eisvogel.latex" ]]; then
  echo "Installing Eisvogel template..."
  mkdir -p "$TEMPLATE_DIR"
  curl -sL "https://github.com/Wandmalfarbe/pandoc-latex-template/releases/download/v3.4.0/Eisvogel-3.4.0.zip" \
    -o /tmp/eisvogel.zip
  unzip -o /tmp/eisvogel.zip -d /tmp/eisvogel
  cp /tmp/eisvogel/eisvogel.latex "$TEMPLATE_DIR/"
  rm -rf /tmp/eisvogel /tmp/eisvogel.zip
fi

# Chapter order (matches site navigation hierarchy)
CHAPTERS=(
  "index.md"
  "getting-started/why-ai-research.md"
  "getting-started/tools-setup.md"
  "the-flow/project-structure.md"
  "the-flow/your-first-session.md"
  "the-flow/ai-assisted-workflow.md"
  "the-flow/writing-with-ai.md"
  "course-development/why-this-is-different.md"
  "course-development/the-instruction-file.md"
  "course-development/building-slides.md"
  "course-development/collaboration-and-handoff.md"
  "reference/commands-cheatsheet.md"
  "reference/faq.md"
)

COMBINED="/tmp/guide-combined.md"

# Write Eisvogel YAML frontmatter
cat > "$COMBINED" << 'FRONTMATTER'
---
title: "An AI-Assisted Research Flow"
subtitle: "A practical guide for empirical researchers and course developers"
author: "Dr. Jared L. Black"
titlepage: true
titlepage-color: "154734"
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "FFB81C"
titlepage-rule-height: 4
toc: true
toc-depth: 2
toc-own-page: true
fontsize: 10pt
linestretch: 1.05
geometry: "margin=0.85in"
colorlinks: true
linkcolor: "teal"
urlcolor: "teal"
toccolor: "black"
header-includes:
  - \usepackage{titlesec}
  - \titleformat{\section}{\Large\bfseries\color[HTML]{154734}}{}{0em}{}
  - \titleformat{\subsection}{\large\bfseries\color[HTML]{154734}}{}{0em}{}
  - \titleformat{\subsubsection}{\normalsize\bfseries\color[HTML]{154734}}{}{0em}{}
  - \titlespacing*{\section}{0pt}{1.2em}{0.4em}
  - \titlespacing*{\subsection}{0pt}{0.8em}{0.3em}
  - \titlespacing*{\subsubsection}{0pt}{0.6em}{0.2em}
  - \setlength{\parskip}{0.3em}
  - \setlength{\parindent}{0em}
  - \usepackage{enumitem}
  - \setlist{nosep, leftmargin=1.5em}
---
FRONTMATTER

for chapter in "${CHAPTERS[@]}"; do
  if [[ ! -f "$chapter" ]]; then
    echo "Warning: $chapter not found, skipping" >&2
    continue
  fi

  # Strip YAML front matter (everything between first --- and second ---)
  # Then clean Jekyll-specific syntax and HTML image tags
  awk '
    BEGIN { in_front=0; front_done=0 }
    /^---$/ && !front_done {
      in_front = !in_front
      if (!in_front) front_done = 1
      next
    }
    front_done { print }
  ' "$chapter" \
    | sed 's/{: \.fs-[0-9]*[^}]*}//g' \
    | sed 's/{: \.fw-[0-9]*[^}]*}//g' \
    | sed 's/{: \.btn[^}]*}//g' \
    | sed 's/{: \.tip }/> **Tip**/g' \
    | sed 's/{: \.note }/> **Note**/g' \
    | sed 's/{: \.important }/> **Important**/g' \
    | sed 's/{: \.warning }/> **Warning**/g' \
    | sed 's/{%[^%]*%}//g' \
    | sed '/<img[^>]*>/d' \
    | sed '/^\[Download as PDF\]/d' \
    >> "$COMBINED"

  # Add a page break between chapters
  printf '\n\\newpage\n\n' >> "$COMBINED"
done

# Build PDF with pandoc + Eisvogel
pandoc "$COMBINED" \
  -o guide.pdf \
  --template eisvogel \
  --pdf-engine=xelatex \
  --listings \
  --metadata date="$(date +%B\ %Y)"

echo "Built: $SCRIPT_DIR/guide.pdf"
