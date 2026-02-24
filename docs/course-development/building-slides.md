---
title: Building Slides
layout: default
parent: Course Development
nav_order: 3
---

# Building Slides

Slide creation follows the same pattern as any other task in the workflow: describe what you want in plain English, and the AI executes it within the conventions defined in the instruction file.

## The prompt

Be specific. A good slide-creation prompt tells the AI what content to use, what template to follow, and what quality bar to meet:

> *"Create slides for lesson 10 using the source materials in resources/ and the conventions in the instruction file. Follow the two-column template from lesson 04. Compile, fix any overflow errors, and iterate until the PDF is clean."*

The AI produces slides with consistent styling, diagrams, and speaker notes — all following whatever conventions the instruction file specifies.

## Source material as context

Before building slides, populate the lesson's `resources/` folder with the material you want to teach from (see [Source Material Library](#source-material-library) below). The AI reads these files as context, which means it has your actual references — not generic knowledge — when constructing slides.

## The presentation format

A common setup: slides on the left, speaker notes on the right. The presenter sees notes and upcoming slides on one screen while students see clean slides on another. Tools like **PyImpress** handle this dual-screen presentation. Templates for different presentation styles are easy to create — each instructor can have their own.

## Compilation

If slides are built in LaTeX Beamer, Marp, or any other compile-to-PDF system, the AI handles compilation and iterates on errors automatically. You can also use `make` targets for one-command builds:

```bash
make lesson-04          # slides
make lesson-04-notes    # slides with speaker notes
```

Or simply ask: *"Compile and open lesson 04."*

---

# Source Material Library

This works like a reference manager integrated into the build process. When you find an article, paper, video, or webpage you want to use for a lesson, it goes into that lesson's `resources/` folder as a markdown summary. When building slides, the AI reads these files and has all that context available.

## Pipelines for getting material in

**Web research:** Give the AI a specific, detailed prompt — the way you'd search Google Scholar after you already know the landscape. Tell it what you have, what quality you're looking for, and where to look.

> *"I already have Smith et al. (2024) and the framework from the tutorial. Find additional peer-reviewed sources on this topic — check the top journals in the field. Add anything good to references.bib."*

**PDFs and articles:** Ask the AI to summarize a PDF or web article into `resources/`. The AI figures out which tools to use — you don't need to know the specific conversion utilities.

**Video and audio:** Transcription skills extract audio from video and transcribe it locally using tools like Whisper. The resulting markdown transcript becomes source material the AI can reference when building slides. No data leaves your machine.

{: .tip }
> You don't need to know all the specific tools for these conversions. If there's a capability you need, the AI can figure out what's required and do it. The point is: you describe what you want, and it finds a path.

## Bibliography

Each lesson maintains a bibliography file. The AI adds entries automatically when creating slides or processing sources. You can also ask directly:

> *"Add this paper to references.bib: [paste citation or URL]"*
