Run a full project integrity check. Two phases:

Phase 1 — Pipeline integrity:
(1) Every script listed in README pipeline table exists.
(2) Every input data file listed exists.
(3) No scripts or data files sitting in wrong directories.
(4) Output directories exist.
(5) params.do values match README parameters table.

Phase 2 — Manuscript audit:
(1) Every entry in README table/figure map has an existing output file and source script.
(2) Every \includegraphics and \input in manuscript.tex resolves to an existing file.
(3) Find any output files not referenced in the manuscript (orphans).
(4) Find any manuscript references not in the table/figure map (undocumented).

Report all findings. Do not fix anything without user approval.
