# AEA Manuscript & Publishing Style Guide
## Comprehensive Reference for AI-Assisted Editing

**Compiled:** 2026-02-07
**Primary sources:** AEA submission policies (aeaweb.org/journals/policies/submissions), AER editorial guidelines (aeaweb.org/journals/aer/about-aer), AEA sample references (aeaweb.org/journals/policies/sample-references), AEA Data and Code Availability Policy, and established conventions from published AER/AEJ papers.

**Note:** Web fetching was unavailable at compile time. This document is drawn from training knowledge of AEA policies current through early 2025. Before final submission, verify all rules against the live AEA website. Flag any discrepancies for the author.

---

## 1. MANUSCRIPT FORMATTING

### 1.1 Page Layout
- **Paper size:** US Letter (8.5 x 11 inches)
- **Margins:** 1 inch on all sides
- **Font:** 12-point, Times New Roman or equivalent serif font (Computer Modern in LaTeX is acceptable)
- **Spacing:** Double-spaced throughout, including abstract, text, footnotes, references, and appendices
- **Page numbers:** Bottom center of every page
- **Alignment:** Left-justified (ragged right) is standard; full justification is also acceptable

### 1.2 Length Guidelines
| Journal | Typical length (published) | Submission guidance |
|---------|---------------------------|-------------------|
| AER | ~15,000-20,000 words | No strict limit; paper should be as long as needed and no longer |
| AER: Insights | ~6,000 words (strict) | Roughly 10 pages of text; 4 exhibits max |
| AEJ: Applied | ~12,000-18,000 words | Similar to AER |
| AEJ: Economic Policy | ~10,000-15,000 words | Conciseness valued |
| AEJ: Macro | ~12,000-18,000 words | Similar to AER |
| AEJ: Micro | ~12,000-18,000 words | Similar to AER |
| JEL | Survey articles; longer | 15,000-20,000+ words |
| JEP | ~6,000-8,000 words | Accessible, shorter |

**Rule for the agent:** Count words excluding tables, figures, references, and appendices. Flag any paper exceeding 20,000 words of body text for AER, or 6,000 for AER: Insights.

### 1.3 LaTeX-Specific Configuration

```latex
\documentclass[12pt]{article}

\usepackage[margin=1in]{geometry}
\usepackage{setspace}
\doublespacing

\usepackage[T1]{fontenc}
\usepackage{mathptmx}          % Times Roman text + math
% OR leave as Computer Modern (LaTeX default) -- both acceptable

\usepackage{graphicx}
\usepackage{booktabs}           % Professional table rules
\usepackage{natbib}             % Author-year citations
\usepackage{amsmath,amssymb}
\usepackage{hyperref}
\usepackage{caption}            % Caption formatting control
\usepackage{subcaption}         % For panel figures
\usepackage{threeparttable}     % Table notes below tables
\usepackage{dcolumn}            % Decimal-aligned columns
\usepackage{rotating}           % Landscape tables if needed
\usepackage{appendix}

\bibliographystyle{aer}         % AER bibliography style
```

**Rule for the agent:** When editing the manuscript.tex preamble, ensure `booktabs`, `natbib`, `threeparttable`, and `dcolumn` are present. These are near-universal in AEA publications.

---

## 2. TITLE PAGE

### 2.1 Required Elements
1. **Title:** Descriptive but concise. Avoid "clever" titles that sacrifice clarity. Subtitles are acceptable with a colon separator.
2. **Author name(s):** Full first and last names.
3. **Affiliation(s):** University or institution for each author, on separate lines.
4. **Contact information:** Corresponding author's email address and mailing address.
5. **Acknowledgments:** In an unnumbered footnote attached to the title (use `\thanks{}` in LaTeX). Include:
   - Funding sources with grant numbers
   - Names of people who provided helpful comments
   - Seminar/conference audiences where paper was presented
   - Disclaimer that views are the authors' own (if relevant)
   - IRB approval statement if human subjects data
6. **JEL Classification codes:** Listed after the abstract (e.g., "JEL: D82, G14, L15")
7. **Keywords:** 3-6 keywords, listed after JEL codes

### 2.2 LaTeX Title Page Template

```latex
\title{Descriptive Paper Title\thanks{%
Author One: Department of Economics, University X, email@univ.edu.
Author Two: Department of Economics, University Y, email@univ.edu.
We thank [names] for helpful comments and seminar participants at [venues].
This research was supported by [funding source, grant number].
The authors declare no relevant financial interests.
All errors are our own.}}

\author{Author One and Author Two}
\date{}  % Leave blank for submission; do not print date

\maketitle

\begin{abstract}
\noindent [Abstract text -- no indentation on first line.]
\end{abstract}

\medskip
\noindent\textbf{JEL:} D82, G14, L15\\
\noindent\textbf{Keywords:} information asymmetry, market design, quality disclosure
\newpage
```

**Rule for the agent:** The title page must include JEL codes and keywords. If either is missing, flag it and suggest the author add them. The `\date{}` should be empty for submissions.

---

## 3. ABSTRACT

### 3.1 Requirements
- **Length:** 100-150 words (strict for AER). Some AEJ journals allow up to 200 words.
- **Content structure:** Should contain:
  1. The research question (1 sentence)
  2. What the paper does / methodology (1-2 sentences)
  3. Key data or setting (1 sentence)
  4. Main finding(s) (1-2 sentences)
  5. Implication or contribution (1 sentence, optional)
- **Style:** No citations, no footnotes, no acronyms (or define them), no mathematical notation if avoidable.
- **Tense:** Present tense for claims and findings ("We find that..."), past tense for what was done ("We estimate...").

### 3.2 Formatting
- No paragraph indentation on the first line
- Single paragraph (no line breaks within the abstract)
- Self-contained: a reader should understand the paper's contribution from the abstract alone

**Rule for the agent:** Count abstract words. If >150 for AER, flag it. If the abstract lacks a clear statement of findings, flag it. If citations or equations appear in the abstract, flag them for removal.

---

## 4. SECTION STRUCTURE FOR EMPIRICAL PAPERS

### 4.1 Standard Structure
The canonical structure for an empirical economics paper:

1. **Introduction** (3-7 pages)
   - Hook: Why should the reader care?
   - Research question, stated plainly
   - Brief summary of what you do (data, method, key result)
   - Contribution relative to literature (concise; not a full lit review)
   - Road map paragraph (optional; increasingly omitted in top journals)

2. **Institutional Background / Setting** (1-4 pages)
   - Only if the institutional context is critical to understanding the identification
   - Keep it tightly focused on what the reader needs

3. **Data** (2-5 pages)
   - Data sources and sample construction
   - Key variable definitions
   - Summary statistics table
   - Sample restrictions and their justification

4. **Empirical Strategy / Identification** (2-5 pages)
   - Estimating equation(s), clearly numbered
   - Identification assumption, stated in plain language
   - Threats to identification, acknowledged upfront
   - Connection between empirical strategy and the research question

5. **Results** (3-8 pages)
   - Main results first (the table that answers your research question)
   - Secondary results and mechanisms
   - Heterogeneity analysis
   - Do not bury the lead

6. **Robustness Checks** (1-4 pages)
   - Can be a subsection of Results or a standalone section
   - Placebo tests, alternative specifications, different samples
   - Sensitivity to functional form, bandwidth, controls

7. **Conclusion** (1-2 pages)
   - Restate main finding(s)
   - Discuss implications
   - Acknowledge limitations honestly
   - Do NOT introduce new results or arguments
   - Keep short -- editors and referees notice bloated conclusions

### 4.2 Variations by Paper Type
- **RCT papers:** Add a "Design" or "Experimental Design" section between Background and Data. Include a CONSORT-style flow diagram. Pre-registration details in a footnote or appendix.
- **Structural papers:** Add a "Model" section before "Estimation." The empirical section becomes "Estimation" and "Identification" may be embedded in the model section.
- **RDD papers:** Empirical Strategy should include density tests, bandwidth sensitivity, and graphical evidence prominently.
- **Theory papers:** Replace empirical sections with "Model," "Analysis," "Equilibrium Characterization," etc.

**Rule for the agent:** If sections are missing or oddly ordered relative to the standard structure, flag it. The Introduction must contain a clear statement of the contribution. The Conclusion must not introduce new evidence.

---

## 5. TABLES

### 5.1 General Principles (AEA Standard)
- Tables should be **self-contained**: a reader should understand the table without reading the text.
- Every table needs:
  - A **numbered title** (e.g., "Table 1--Effect of Treatment on Outcome")
  - **Column headers** that are clear and labeled
  - **Row labels** that are descriptive (not variable codes)
  - **Notes** below the table explaining variables, sample, and statistical details
  - **Source** if data are not from the paper's main dataset

### 5.2 Formatting Rules
- Use `booktabs` rules: `\toprule`, `\midrule`, `\bottomrule`. NO vertical lines. NO `\hline`.
- Decimal-align numeric columns (use `dcolumn` package or `siunitx`).
- Use consistent decimal places within each column (typically 2-3 for coefficients, 3 for standard errors).
- Standard errors in parentheses below coefficients. NOT brackets.
- Significance stars: `* p<0.10, ** p<0.05, *** p<0.01` (this is the AEA convention).
  - Define stars in a table note, every time.
  - Some editors prefer p<0.05 and p<0.01 only. Follow journal norms.
- Report the number of observations (N) for each specification.
- Report R-squared or pseudo R-squared where appropriate.
- Report the mean of the dependent variable when it aids interpretation.
- Cluster-robust standard errors: state the clustering level in the table note.

### 5.3 Summary Statistics Table
Required elements:
| Variable | Mean | Std. Dev. | Min | Max | N |
|----------|------|-----------|-----|-----|---|

- Use human-readable variable names, not Stata/R variable codes.
- Group variables logically (outcomes, then treatments, then controls).
- Consider adding the median or the 25th/75th percentile for skewed variables.

### 5.4 Regression Table Best Practices

```
Table 3--Effect of Minimum Wage on Employment

                        (1)         (2)         (3)         (4)
                        OLS         OLS         IV          IV
--------------------------------------------------------------
Minimum wage           -0.032**    -0.028**    -0.054**    -0.048*
                       (0.014)     (0.013)     (0.025)     (0.026)

Controls                 No          Yes         No          Yes
State FE                 Yes         Yes         Yes         Yes
Year FE                  Yes         Yes         Yes         Yes
--------------------------------------------------------------
Observations           15,230      15,230      15,230      15,230
R-squared               0.42        0.47         --          --
First-stage F-stat       --          --        24.6        23.1
Mean dep. var.          8.32        8.32        8.32        8.32
--------------------------------------------------------------
Notes: The dependent variable is log employment. Standard errors
clustered at the state level in parentheses. * p<0.10, ** p<0.05,
*** p<0.01.
```

**Rules for the agent:**
- Flag tables with vertical lines or `\hline` instead of booktabs rules.
- Flag standard errors in brackets instead of parentheses.
- Flag missing N, R-squared, or significance star definitions.
- Flag Stata/R variable names (e.g., `ln_emp`) instead of human-readable labels.
- Flag inconsistent decimal places within a column.
- Ensure the table note defines what is in parentheses.
- Tables should build progressively: column (1) simplest, adding controls and fixed effects.

### 5.5 LaTeX Table Template

```latex
\begin{table}[htbp]
\centering
\begin{threeparttable}
\caption{Effect of Treatment on Outcome}
\label{tab:main_results}
\begin{tabular}{l D{.}{.}{2.3} D{.}{.}{2.3} D{.}{.}{2.3}}
\toprule
                    & \multicolumn{1}{c}{(1)} & \multicolumn{1}{c}{(2)} & \multicolumn{1}{c}{(3)} \\
                    & \multicolumn{1}{c}{OLS} & \multicolumn{1}{c}{OLS} & \multicolumn{1}{c}{IV}  \\
\midrule
Treatment           & -0.032^{**}  & -0.028^{**}  & -0.054^{**}  \\
                    & (0.014)      & (0.013)      & (0.025)      \\[6pt]
Controls            & \multicolumn{1}{c}{No}  & \multicolumn{1}{c}{Yes} & \multicolumn{1}{c}{Yes} \\
State FE            & \multicolumn{1}{c}{Yes} & \multicolumn{1}{c}{Yes} & \multicolumn{1}{c}{Yes} \\
Year FE             & \multicolumn{1}{c}{Yes} & \multicolumn{1}{c}{Yes} & \multicolumn{1}{c}{Yes} \\
\midrule
Observations        & \multicolumn{1}{c}{15,230} & \multicolumn{1}{c}{15,230} & \multicolumn{1}{c}{15,230} \\
R^2                 & 0.42         & 0.47         &              \\
Mean dep.\ var.     & 8.32         & 8.32         & 8.32         \\
\bottomrule
\end{tabular}
\begin{tablenotes}[flushleft]
\small
\item \textit{Notes:} The dependent variable is log employment.
Standard errors clustered at the state level in parentheses.
$^{*}$ $p<0.10$, $^{**}$ $p<0.05$, $^{***}$ $p<0.01$.
\end{tablenotes}
\end{threeparttable}
\end{table}
```

---

## 6. FIGURES

### 6.1 General Requirements
- **Resolution:** At least 300 dpi for raster images; vector formats (PDF, EPS) strongly preferred.
- **File format:** PDF for LaTeX; EPS also accepted. Avoid PNG/JPG for line graphs.
- **Color:** Use colorblind-friendly palettes. Figures must be interpretable in grayscale (many readers print in B&W).
- **Size:** Design for the final printed column width (~5.5 inches for single column, ~3.3 inches for two-column).
- **Font in figures:** Should match or complement the body text font. Minimum 8pt for axis labels.

### 6.2 Figure Components
Every figure needs:
1. **Number and title** (e.g., "Figure 1. Effect of Treatment Over Time")
   - AEA uses a period after the number: "Figure 1." not "Figure 1:"
   - Title is descriptive: tells the reader what to see
2. **Axis labels** with units (e.g., "Employment (thousands)" not just "Employment")
3. **Legend** if multiple series, positioned to minimize whitespace
4. **Notes** below the figure: data source, sample, what the shaded areas or dashed lines represent
5. **Confidence intervals** shown as shaded bands or capped whiskers for regression plots

### 6.3 Common Figure Types in Empirical Economics
- **Event study / dynamic treatment effects:** Plot coefficients with 95% CI. Reference period = 0 with dashed horizontal line. Pre-trends visible. Time on x-axis, effect size on y-axis.
- **RDD plots:** Binned scatter plot with fitted polynomial on each side of cutoff. Vertical dashed line at cutoff.
- **Binned scatter plots:** Use ~20 bins (Chetty et al. convention). Show the regression line. Note the number of bins and residualization in notes.
- **Distribution plots:** Histograms or kernel densities. State bandwidth if kernel.
- **Maps:** Include scale bar, legend, source.

### 6.4 LaTeX Figure Template

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=\textwidth]{fig1_event_study.pdf}
\caption{Dynamic Treatment Effects on Employment}
\label{fig:event_study}
\begin{minipage}{\textwidth}
\small
\textit{Notes:} This figure plots estimated coefficients $\beta_\tau$
from equation (2) with 95 percent confidence intervals. The omitted
period is $\tau = -1$. The dashed horizontal line marks zero. Standard
errors are clustered at the state level. $N = 15{,}230$.
\end{minipage}
\end{figure}
```

**Rules for the agent:**
- Flag figures without notes or axis labels.
- Flag raster image formats (PNG, JPG, BMP) -- suggest PDF.
- Flag event study plots missing a reference period line or confidence intervals.
- Ensure figure titles use "Figure N." (period, not colon).

---

## 7. CITATIONS AND REFERENCES (AEA STYLE)

### 7.1 In-Text Citations
AEA uses **author-year** style (via `natbib`):

| Citation type | LaTeX command | Output |
|--------------|---------------|--------|
| Parenthetical | `\citep{angrist1999}` | (Angrist and Krueger 1999) |
| Textual | `\citet{angrist1999}` | Angrist and Krueger (1999) |
| Multiple | `\citep{angrist1999, card1994}` | (Angrist and Krueger 1999; Card 1994) |
| With page | `\citep[p.~42]{angrist1999}` | (Angrist and Krueger 1999, p. 42) |
| Possessive | `\citeauthor{angrist1999}'s (\citeyear{angrist1999})` | Angrist and Krueger's (1999) |

**Key rules:**
- Two authors: always spell out both names ("Angrist and Krueger 1999").
- Three or more authors: use "et al." from the first citation ("Chetty et al. 2014").
- No comma between author and year: "(Smith 2020)" not "(Smith, 2020)".
- Semicolons separate multiple citations: "(Smith 2020; Jones 2021)".
- Alphabetical order within parenthetical groups, unless chronological order is meaningful.

### 7.2 Reference List Formatting

The reference list is titled "REFERENCES" (all caps, centered). Entries are:
- Hanging indent (first line flush left, subsequent lines indented)
- Single-spaced within entries, double-spaced between entries (in final publication; double-space everything for submission)
- Alphabetical by first author's last name
- Chronological for multiple works by the same author(s)
- Use "a", "b", "c" suffixes for same-author, same-year works

### 7.3 Sample Reference Formats

**Journal article:**
```
Acemoglu, Daron, and James A. Robinson. 2001. "A Theory of Political
    Transitions." American Economic Review, 91 (4): 938-963.
```

**Journal article with DOI (increasingly required):**
```
Autor, David H., Lawrence F. Katz, and Melissa S. Kearney. 2008.
    "Trends in US Wage Inequality: Revising the Revisionists."
    Review of Economics and Statistics, 90 (2): 300-323.
    https://doi.org/10.1162/rest.90.2.300.
```

**Book:**
```
Angrist, Joshua D., and Jorn-Steffen Pischke. 2009. Mostly Harmless
    Econometrics: An Empiricist's Companion. Princeton, NJ:
    Princeton University Press.
```

**Chapter in edited volume:**
```
Heckman, James J. 2001. "Micro Data, Heterogeneity, and the
    Evaluation of Public Policy: Nobel Lecture." Journal of Political
    Economy, 109 (4): 673-748.
```

**Edited volume:**
```
Aghion, Philippe, and Steven N. Durlauf, eds. 2005. Handbook of
    Economic Growth, Vol. 1A. Amsterdam: Elsevier.
```

**Working paper / NBER:**
```
Chetty, Raj, John N. Friedman, and Jonah E. Rockoff. 2013. "Measuring
    the Impacts of Teachers II: Teacher Value-Added and Student
    Outcomes in Adulthood." NBER Working Paper 19424.
```

**Government/institutional report:**
```
US Census Bureau. 2020. "Current Population Survey, Annual Social
    and Economic Supplement." Washington, DC: US Census Bureau.
```

**Website / online resource:**
```
Bureau of Labor Statistics. 2023. "Consumer Price Index."
    https://www.bls.gov/cpi/ (accessed March 15, 2023).
```

**Forthcoming:**
```
Smith, John. Forthcoming. "Title of Article." American Economic Review.
```

**Dissertation:**
```
Doe, Jane. 2019. "Title of Dissertation." PhD diss., Harvard University.
```

### 7.4 Key Reference Formatting Rules
1. Author names: Last, First Middle Initial. Use full first names (not initials alone).
2. Use "and" (not "&") before the last author.
3. Article titles in quotation marks; book/journal titles in italics.
4. Journal name followed by a **comma**, then volume number **(bold or plain both seen; AER house style uses plain)**, issue number in parentheses, colon, page range.
5. Volume(Issue): Pages format: `91 (4): 938-963.` -- note the space before parenthesis and after colon.
6. Use en-dash for page ranges: `938-963` (or `938--963` in LaTeX).
7. End every reference with a period.
8. Capitalize all major words in titles (AEA uses title case for article titles).
9. Publisher location: City, State abbreviation (for US) or City, Country.
10. URLs: include for online-only sources; include access date.

**Rule for the agent:** Flag references that use initials instead of full first names, use "&" instead of "and", lack quotation marks around article titles, or have inconsistent formatting. Ensure the `.bib` file produces output compatible with these rules when used with `\bibliographystyle{aer}`.

---

## 8. DATA AND CODE AVAILABILITY POLICY

### 8.1 AEA Data and Code Availability Policy (Mandatory since 2019)
This is a **condition of publication**, not optional. Every accepted paper must provide:

1. **README file:** A master README (in PDF) that describes:
   - Data sources and how to obtain them
   - Computational requirements (software, hardware, runtime)
   - Instructions for replication from raw data to final tables/figures
   - File structure of the replication package

2. **Data:** All data used in the analysis must be provided unless legally restricted. For restricted data:
   - Describe the data and access procedures in detail
   - Provide all code that would run on the data
   - Provide simulated/synthetic data if possible

3. **Code:** All code for:
   - Data cleaning and preparation
   - All analyses (main and appendix)
   - Every table and figure in the paper

4. **Deposit location:** The AEA Data and Code Repository on openICPSR.

### 8.2 What to Prepare During Writing
- Maintain a clear pipeline from raw data to outputs (this project already has `pipeline.md`).
- Write code that runs end-to-end from a master script (this project has `run_all.sh`).
- Name output files to match manuscript references (this project has `table_figure_map.md`).
- Log software versions and package dependencies.
- Include a data citation for every dataset used.

### 8.3 Data Citations
Data should be cited in the reference list like any other source:

```
Chetty, Raj, and Nathaniel Hendren. 2018. "Replication Data for:
    The Impacts of Neighborhoods on Intergenerational Mobility."
    American Economic Association [publisher], Inter-university
    Consortium for Political and Social Research [distributor].
    https://doi.org/10.3886/E12345V1.
```

**Rule for the agent:** When a dataset is mentioned in the text, verify it has a formal citation in the references. Flag datasets that lack citations. Remind authors to prepare the replication package alongside the manuscript, not after acceptance.

---

## 9. STYLE GUIDE: PROSE CONVENTIONS

### 9.1 Numbers
- Spell out numbers one through nine in text; use numerals for 10 and above.
- Always use numerals with units: "5 percent," "3 years," "$4 million."
- Use numerals for all numbers in a sentence if any exceed nine: "We use 3 datasets with 12, 8, and 15 variables."
- Use commas in numbers >= 1,000: "15,230 observations."
- In LaTeX, use `15{,}230` or `\numprint{15230}` for proper spacing.
- Percentages: "5 percent" in text (spell out "percent"), "5%" in tables and figures.
- Dollar amounts: "$4.2 million" (not "$4,200,000" unless precision matters).

### 9.2 Punctuation
- **Oxford comma:** YES. AEA uses the serial/Oxford comma. "Wages, employment, and hours" not "wages, employment and hours."
- **Em-dash:** Use sparingly. In LaTeX: `---` (no spaces around it). "The result---consistent with theory---suggests..."
- **En-dash:** For number ranges and compound adjectives: "1990--2020," "difference-in-differences."
- **Quotation marks:** Double quotes for direct quotations and article titles. Single quotes for terms used in a special sense (e.g., 'treatment' in a non-medical context). AEA generally uses double quotes.
- **Periods with abbreviations:** "U.S." (with periods) as adjective; "the United States" (spelled out) as noun. "e.g.," and "i.e.," always followed by a comma.

### 9.3 Abbreviations and Acronyms
- Define on first use: "instrumental variables (IV)" then "IV" thereafter.
- Common abbreviations that need no definition in economics: GDP, OLS, IV, GNP, CPI, US (as adjective).
- Avoid acronym overload. If an acronym is used fewer than ~5 times, just spell it out each time.
- Latin abbreviations: use "e.g.," "i.e.," "et al.," "cf." -- always with periods.
- "et al." has a period after "al" but not after "et."

### 9.4 Capitalization
- Section headings: Title Case ("Empirical Strategy") or Sentence case ("Empirical strategy") -- be consistent. AER uses Roman numerals with Title Case (I. Introduction, II. Data).
- "Table 1" and "Figure 2" are capitalized when referring to specific items.
- "equation (3)" is lowercase with the number in parentheses.
- "Section III" is capitalized.
- Theory-specific terms: capitalize proper nouns only ("Nash equilibrium," not "Nash Equilibrium"; "Bayesian" is capitalized because it derives from Bayes).

### 9.5 Mathematical Notation
- Italicize variables: $x$, $\beta$, $Y_{it}$.
- Vectors and matrices in bold: $\mathbf{X}$, $\boldsymbol{\beta}$.
- Operators in Roman (upright): $\log$, $\exp$, $\max$, $\Pr$, $\mathbb{E}$ -- use `\log`, `\exp`, `\max`, `\Pr`, `\mathbb{E}`.
- Number all equations that are referenced in the text. Unreferenced display equations need not be numbered.
- Use `align` or `equation` environments, not `eqnarray` (deprecated).
- Define every symbol when it first appears.
- Subscripts: $i$ for individuals, $t$ for time, $j$ for firms/groups, $s$ for states/sectors (common conventions).

### 9.6 Commonly Confused Terms in Economics
- "effect" (noun) vs. "affect" (verb)
- "causal" vs. "correlational" -- be precise
- "significant" -- always clarify: statistically significant or economically significant
- "We regress Y on X" (not "of X" or "against X" -- though "against" is sometimes used)
- "standard deviation" (of a variable) vs. "standard error" (of an estimate)
- "data" is plural in formal economics writing: "the data are" not "the data is"
- "robust" standard errors, not "Robust" (no capital unless starting a sentence)
- "fixed effects" (noun, adjective) -- lowercase, two words
- "difference-in-differences" (hyphenated, lowercase)
- "regression discontinuity" (two words, no hyphen when used as a noun)
- "instrumental variable" (singular) or "instrumental variables" (plural); "IV" for short
- "percent" not "per cent" in American English
- "toward" not "towards" (American English preference)

---

## 10. FOOTNOTES AND ENDNOTES

### 10.1 AEA Policy
- AER and AEJ journals use **footnotes** (bottom of page), not endnotes.
- Footnotes should be **substantive but brief**. If a footnote grows beyond ~3-4 sentences, consider moving it to an appendix or incorporating it into the text.
- Use footnotes for:
  - Technical details that interrupt the narrative flow
  - Caveats or qualifications
  - Brief references to related literature
  - Data source details
- Do NOT use footnotes for:
  - Core arguments (put them in the text)
  - Long methodological discussions (put them in an appendix)
  - Citations alone (use in-text citations instead)
- Number footnotes consecutively throughout the paper.
- In LaTeX, `\footnote{Text.}` places the marker after punctuation: `word.\footnote{...}` is correct.

---

## 11. APPENDICES

### 11.1 What Goes in the Appendix vs. Main Text
**Main text should contain:**
- Core argument, identification, main results
- Key robustness checks that a skeptical reader needs to see
- Essential summary statistics
- The minimum a reader needs to evaluate your contribution

**Online appendix should contain:**
- Additional robustness checks (alternative specifications, subsamples, bandwidths)
- Detailed variable definitions
- Extended summary statistics
- Proofs of theoretical propositions (unless the proof IS the contribution)
- Survey instruments, additional institutional details
- First-stage results for IV (unless first stage is a key contribution)
- Additional figures that supplement the narrative
- Sensitivity analyses, leave-one-out tests, etc.

### 11.2 Formatting
- Label appendix sections as A, B, C (e.g., "Appendix A: Variable Definitions")
- Tables numbered A1, A2, ...; Figures numbered A1, A2, ...
- The appendix should be self-contained with its own references if submitted as a separate document
- For AER: the online appendix is hosted on the AEA website alongside the paper
- Reference appendix content from the main text: "See Appendix Table A3 for robustness."

### 11.3 LaTeX Appendix Setup

```latex
\clearpage
\appendix
\renewcommand{\thetable}{A\arabic{table}}
\renewcommand{\thefigure}{A\arabic{figure}}
\setcounter{table}{0}
\setcounter{figure}{0}

\section{Additional Results}
\label{app:additional}
```

---

## 12. COMMON REJECTION REASONS RELATED TO PRESENTATION

### 12.1 Formatting/Presentation Red Flags
Based on published editorial reports and referee guidance:

1. **Paper is too long.** Ruthlessly cut. If a section does not advance the core argument, move it to the appendix.
2. **Introduction does not state the contribution clearly.** The reader should know the main finding by page 2-3.
3. **Tables are unreadable.** Tiny font, too many columns, no notes, Stata output pasted directly.
4. **Figures are low resolution or uninterpretable.** Missing axis labels, no legend, wrong scale.
5. **Literature review is a laundry list.** Organize by contribution, not by author.
6. **Identification is buried.** The estimating equation and identification assumption should be prominent.
7. **Abstract is vague.** "We study the effect of X on Y" without stating the finding.
8. **Inconsistent notation.** Switching between $\beta$ and $b$ for the same parameter.
9. **Missing standard errors or confidence intervals.** Every estimated quantity needs a measure of uncertainty.
10. **No discussion of economic significance.** Statistical significance alone is insufficient.
11. **Sloppy references.** Missing years, inconsistent formatting, "et al" in the reference list (it belongs only in citations).
12. **Appendix overload with thin main text.** The main paper must stand alone.

**Rule for the agent:** When reviewing a draft, check every item on this list. Flag violations with specific suggestions.

---

## 13. PRESENTING REGRESSION RESULTS

### 13.1 Coefficient Reporting
- Report coefficients with enough decimal places to convey precision, but not so many that the table is cluttered. Typically 2-4 significant digits.
- Standard errors in parentheses directly below the coefficient.
- State the type of standard errors: robust, clustered (and at what level), bootstrapped, etc.
- Use asterisks for significance: *, **, *** at conventional levels.
- Always report the dependent variable clearly (in the table title or column header).

### 13.2 Economic Significance
- Discuss the magnitude: "A one-standard-deviation increase in X is associated with a Y-unit change in the outcome, which represents Z percent of the mean."
- Back-of-the-envelope calculations help the reader grasp the importance.
- Compare effect sizes to other studies or policy-relevant benchmarks.

### 13.3 Building a Regression Table
- Column (1): Simplest specification (bivariate or with minimal controls)
- Column (2): Add demographic/standard controls
- Column (3): Add fixed effects
- Column (4): Preferred specification (clearly indicated in text)
- Column (5+): Alternative specifications, robustness
- This progressive structure lets the reader see how sensitive results are to specification choices.

### 13.4 Summary Statistics Best Practices
- Present before any regression results.
- Include all variables that appear in regressions.
- Consider separate panels for different subgroups (treatment vs. control).
- Balance tables for RCTs or quasi-experimental designs: treatment mean, control mean, difference, p-value.

### 13.5 Robustness Check Presentation
- Organize by type of concern: alternative samples, alternative measures, alternative specifications, placebo tests, falsification tests.
- A single "robustness table" with each column representing a different check is efficient.
- The preferred specification should appear as a benchmark column for easy comparison.
- Do not just show that results are robust -- explain what threat each check addresses.

---

## 14. AER-SPECIFIC NOTES

### 14.1 About AER
- The American Economic Review is the flagship journal of the AEA, published since 1911.
- Publishes original research across all fields of economics.
- Acceptance rate: approximately 6-8%.
- Typical timeline: 3-6 months for first decision.
- Submissions are handled through the AEA's editorial management system.

### 14.2 AER: Insights
- Shorter papers (roughly 6,000 words, ~10 published pages).
- Maximum of 4 exhibits (tables + figures combined).
- Must make a clear, concise contribution that does not require the length of a full AER paper.
- Faster review process.

### 14.3 AER: Papers and Proceedings (AER P&P)
- Published in May issue, based on AEA Annual Meeting sessions.
- By invitation only (not open for unsolicited submissions).
- Very short: ~2,500 words, 7 pages max in published form.
- No formal refereeing; edited for clarity.

---

## 15. CHECKLIST FOR MANUSCRIPT REVIEW

Use this checklist when performing a final review before submission:

### Title Page
- [ ] Title is descriptive and concise
- [ ] All author names and affiliations present
- [ ] Contact email for corresponding author
- [ ] Acknowledgments footnote with funding, thanks, disclaimers
- [ ] JEL codes listed
- [ ] Keywords listed
- [ ] Date field is empty (for blind review)

### Abstract
- [ ] 100-150 words (AER) / up to 200 words (AEJ)
- [ ] States the research question
- [ ] States the main finding with specificity
- [ ] No citations, equations, or undefined acronyms
- [ ] Single paragraph

### Body Text
- [ ] Double-spaced, 12pt font, 1-inch margins
- [ ] Sections logically ordered
- [ ] Introduction states contribution by page 2-3
- [ ] All variables defined before use
- [ ] All equations numbered (if referenced)
- [ ] Notation consistent throughout
- [ ] "Data are" (plural)
- [ ] Oxford comma used consistently
- [ ] Numbers follow style rules (spell out 1-9, numerals 10+)
- [ ] "percent" spelled out in text; "%" in tables
- [ ] US/American English spelling throughout
- [ ] No first-person hedging ("We believe" -- state it directly)

### Tables
- [ ] Booktabs rules only (no vertical lines, no \hline)
- [ ] Self-contained: title, headers, notes
- [ ] Human-readable variable names
- [ ] Standard errors in parentheses
- [ ] Significance stars defined in notes
- [ ] N reported for every specification
- [ ] Decimal places consistent within columns
- [ ] Mean of dependent variable reported (if helpful)
- [ ] Source noted for external data

### Figures
- [ ] Vector format (PDF/EPS preferred)
- [ ] High resolution (300+ dpi if raster)
- [ ] Axis labels with units
- [ ] Legends where needed
- [ ] Confidence intervals shown
- [ ] Colorblind-friendly palette
- [ ] Interpretable in grayscale
- [ ] Notes below figure

### References
- [ ] AER author-year style
- [ ] Full first names (not initials)
- [ ] "and" not "&"
- [ ] Article titles in quotes, title case
- [ ] Journal names in italics
- [ ] Volume (Issue): Pages format
- [ ] Every citation has a reference entry and vice versa
- [ ] Data sources cited in reference list
- [ ] URLs include access dates
- [ ] Alphabetical order

### Appendix
- [ ] Tables/figures numbered A1, A2, etc.
- [ ] Referenced from main text
- [ ] Does not contain results essential to the core argument
- [ ] Formatted consistently with main paper

### Data and Code
- [ ] Replication package prepared (or in progress)
- [ ] README describes full pipeline
- [ ] All data sources documented
- [ ] Code runs end-to-end from master script
- [ ] All datasets cited in references

---

## 16. QUICK REFERENCE: COMMON LATEX COMMANDS FOR AEA PAPERS

| Task | LaTeX | Notes |
|------|-------|-------|
| Parenthetical cite | `\citep{key}` | (Author Year) |
| Textual cite | `\citet{key}` | Author (Year) |
| Author only | `\citeauthor{key}` | Author |
| Year only | `\citeyear{key}` | Year |
| Thousands separator | `15{,}230` | Proper kerning |
| Percent | `5~percent` or `5\%` | Text vs. tables |
| Significance stars | `$^{***}$` | In table cells |
| Table notes | `\begin{tablenotes}` | With threeparttable |
| Decimal align | `D{.}{.}{2.3}` | With dcolumn |
| Cross-reference | `Table~\ref{tab:main}` | Non-breaking space with ~ |
| Equation ref | `equation~(\ref{eq:main})` | Parentheses around number |
| Em-dash | `---` | No surrounding spaces |
| En-dash | `--` | For ranges: 1990--2020 |
| Non-breaking space | `~` | Before \ref, \citep, units |
| Ellipsis | `\ldots` | Not three periods |

---

## 17. SOURCE URLS FOR VERIFICATION

Before final submission, verify current rules at these URLs:
- AEA Submission Policies: https://www.aeaweb.org/journals/policies/submissions
- AER About Page: https://www.aeaweb.org/journals/aer/about-aer
- AEA Sample References: https://www.aeaweb.org/journals/policies/sample-references
- AEA Data and Code Policy: https://www.aeaweb.org/journals/data/data-code-policy
- AEA LaTeX Templates: https://www.aeaweb.org/journals/policies/templates
- AEA Accepted Articles Formatting: https://www.aeaweb.org/journals/policies/accepted-articles
- AER Style Guide (for copyediting): provided to authors upon acceptance

---

*This document should be updated whenever AEA policies change. The agent should flag any manuscript element that deviates from these rules and suggest the specific correction with reference to the relevant section of this guide.*
