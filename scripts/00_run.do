* ==============================================================================
* 00_run.do — Master do-file
* Sets globals, runs all pipeline steps
* ==============================================================================

clear all
set more off
set maxvar 32767

* --- Detect user and set project root ---
if "`c(username)'" == "jaredblack" {
    global root "/Users/jaredblack/Library/CloudStorage/Dropbox/Research-Project-Flow"
}
* Add each collaborator:
* if "`c(username)'" == "coauthor" {
*     global root "/Users/coauthor/Dropbox/Research-Project-Flow"
* }

* --- Verify correct folder ---
capture confirm file "$root/pipeline.md"
if _rc != 0 {
    display as error "Cannot find pipeline.md — wrong folder?"
    exit 601
}

* --- Define globals ---
global data      "$root/data"
global raw       "$root/data/raw"
global processed "$root/data/processed"
global scripts   "$root/scripts"
global output    "$root/output"
global figures   "$root/output/figures"
global tables    "$root/output/tables"
global results   "$root/output/results"
global logs      "$root/output/logs"

* --- Load parameters ---
do "$scripts/params.do"

* --- Run pipeline steps ---
* Uncomment as you build:
* do "$scripts/01_import.do"
* do "$scripts/05_merge.do"
* do "$scripts/10_treatment.do"
