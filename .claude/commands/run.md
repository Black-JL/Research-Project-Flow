Run a pipeline step. Ask which step if not specified. Accept --all to run full pipeline, --from <step> to run from a specific step forward.
Before running: (1) confirm input files exist, (2) confirm output paths match the README pipeline table, (3) check params.do for parameter values.
Execute using ./run_all.sh "<script_name>". Read the log. Summarize results. Flag any errors or warnings.
After running: identify downstream steps that may need re-running and tell the user.
