Scaffold a new pipeline step. Ask the user for:
(1) Step number (suggest the next available number with a gap).
(2) Script name and language (Stata or R).
(3) Brief description of what the step does.
(4) Input files.
(5) Expected output files.

Then:
(a) Create the script file in scripts/ with a standard header documenting Purpose, Inputs, Outputs, Dependencies.
(b) Add the step to the README pipeline table in the correct position.
(c) Add the step to run_all.sh in the correct position.
(d) Add the step to 00_run.do (commented out) in the correct position.
(e) If the step produces figures or tables, add entries to the README table/figure map.
Show the user everything before writing.
