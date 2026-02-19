# Pipeline

**Project:** <!-- Your project title -->
**Last Updated:** <!-- Date -->

---

## Path Conventions

### Working Directory Structure

```
project-name/
├── data/           ← Validated data files
│   ├── raw/        ← Untouched source data (READ-ONLY)
│   └── processed/  ← Created by scripts
├── scripts/        ← Validated scripts (.do, .R, .py)
├── output/         ← ALL generated outputs
│   ├── logs/       ← Execution logs (from run_all.sh)
│   ├── figures/    ← Plots for manuscript
│   └── tables/     ← LaTeX tables, CSV summaries
├── manuscript/     ← LaTeX/Markdown manuscript
└── session_logs/   ← AI session documentation
```

### Script Path Rules

**Data input (Stata):**
```stata
cd "$data"
use "processed/analysis_file.dta"
```

**Output paths (Stata):**
```stata
graph export "$figures/plot.pdf", replace
esttab using "$tables/results.tex", replace
```

**LaTeX integration:**
```latex
\graphicspath{{../output/figures/}}
\input{../output/tables/table.tex}
```

---

## Pipeline Tree

```
PROJECT PIPELINE
================

[RAW DATA SOURCES] (data/raw/ — READ-ONLY)
├── Source 1
├── Source 2
└── Source 3

                    │
                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 1: DATA PREPARATION                                      │
└─────────────────────────────────────────────────────────────────┘
    │
    ├──► Step 01: Import & Clean
    │    INPUT:  data/raw/source_file.csv
    │    OUTPUT: data/processed/clean_data.dta
    │
    └──► Step 05: Merge & Collapse
         INPUT:  data/processed/clean_data.dta
         OUTPUT: data/processed/analysis_file.dta

┌─────────────────────────────────────────────────────────────────┐
│  PHASE 2: DIAGNOSTICS & PREPARATION                              │
└─────────────────────────────────────────────────────────────────┘
    │
    ├──► Step 10: Balance / Summary Statistics
    │    INPUT:  data/processed/analysis_file.dta
    │    OUTPUT: output/tables/balance_table.tex
    │
    └──► Step 15: Visualization
         INPUT:  data/processed/analysis_file.dta
         OUTPUT: output/figures/descriptive_plot.pdf

┌─────────────────────────────────────────────────────────────────┐
│  PHASE 3: ESTIMATION                                             │
└─────────────────────────────────────────────────────────────────┘
    │
    └──► Step 20: Main Estimation
         INPUT:  data/processed/analysis_file.dta
         OUTPUT: output/tables/main_results.tex
                 output/figures/event_study.pdf
                 output/results/estimates.ster

================================================================================
                            OUTPUT PRODUCTS
================================================================================

FIGURES (for manuscript)
└── output/figures/
    ├── descriptive_plot.pdf
    └── event_study.pdf

TABLES (for manuscript)
└── output/tables/
    ├── balance_table.tex
    └── main_results.tex

LOGS
└── output/logs/
    └── [All execution logs from run_all.sh]
```

---

## Script Status

| Step | Script | Language | Status | Notes |
|------|--------|----------|--------|-------|
<!-- | 01 | scripts/01_import.do | Stata | ✓ Done | Imports raw CSV, cleans IDs | -->
<!-- | 05 | scripts/05_merge.do | Stata | ✓ Done | Merges datasets on FIPS | -->
<!-- | 10 | scripts/10_balance.R | R | ✓ Done | Balance table, t-tests | -->
<!-- | 15 | scripts/15_visualize.R | R | ✓ Done | Descriptive figures | -->
<!-- | 20 | scripts/20_estimate.do | Stata | In progress | Main DiD estimation | -->

---

## Data Files

| File | Size | Purpose | Created by | Used by |
|------|------|---------|------------|---------|
<!-- | data/processed/clean_data.dta | 5 MB | Cleaned import | Step 01 | Step 05 | -->
<!-- | data/processed/analysis_file.dta | 12 MB | Analysis-ready | Step 05 | Steps 10, 15, 20 | -->

---

## Manuscript Figure Manifest

This table maps every figure in the manuscript back to its source script and input data. Use this to trace any figure upstream to its code, or to identify which figures need regeneration when a script or dataset changes.

| Manuscript ref | Filename | Source script | Step | Input data |
|---------------|----------|---------------|------|------------|
<!-- | Figure 1 | descriptive_plot.pdf | scripts/15_visualize.R | 15 | analysis_file.dta | -->
<!-- | Figure 2 | event_study.pdf | scripts/20_estimate.do | 20 | analysis_file.dta | -->
<!-- | Table 1 | balance_table.tex | scripts/10_balance.R | 10 | analysis_file.dta | -->
<!-- | Table 2 | main_results.tex | scripts/20_estimate.do | 20 | analysis_file.dta | -->

### Tracing Workflow

**Figure → Source (downstream to upstream):**
1. Find the `\includegraphics{filename}` in your manuscript
2. Look up the filename in this manifest to find the source script and step
3. Read the source script to find its input data file
4. Check the pipeline tree above to find what upstream step creates that data file

**Script change → Affected figures (upstream to downstream):**
1. Identify which step's script was changed
2. Look up that step in this manifest to find all figures it produces
3. Rerun the script using `./run_all.sh "script_name"`
4. Output goes to `output/figures/` or `output/tables/` which the manuscript picks up

---

## Notes

<!-- Add project-specific notes here -->
- All outputs go to `output/` — figures in `output/figures/`, tables in `output/tables/`
- The pipeline table in `README.md` must stay in sync with this document
- Use `/check` to verify consistency between pipeline.md, README, and actual files
