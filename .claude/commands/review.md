Adversarial review of a change to estimation or sample-construction logic, before it is accepted. Be skeptical and goal-backward: assume the change is wrong until shown otherwise. This is Layer 2 of dual-layer validation and operationalizes the "break the glass" rule.

**Trigger.** Run this whenever a script's *specification* changes — anything that alters what data enters the estimator. Cosmetic changes (paths, formatting, variable renaming, output aesthetics, logging) do not need review.

Procedure:

1. **Identify the change.** Diff the new logic against the prior version (`git diff`, or the prior lettered script — e.g. `10_estimate.do` vs `10a_estimate.do`). State exactly what changed in terms of *what data enters the estimator*.

2. **Review against each dimension.** For each, ask: "Does this change what is identified?" and "Is this what `params.do` / the README / the analysis plan intends?"
   - Sample restrictions (`keep if` / `drop if` / panel requirements)
   - Outcome variable definition
   - Exposure / treatment variable definition
   - Covariate set and functional form
   - Standard errors / clustering / inference method
   - Strata / fixed effects
   - Time origin (incl. survival origin)
   - Weights
   - Donor pool / control group
   - Treatment dates

3. **Check the Inline Audit Trail.** Every restriction the change touches must carry INTENT / REASONING / ASSUMES comments. Flag any that don't.

4. **Check validation.** The relevant checkpoint asserts (CP1–CP4) still hold and still cover the changed logic.

5. **Verdict per dimension — PASSED / WARNING / BLOCKER:**
   - **BLOCKER** — the change silently alters identification, contradicts `params.do`/README, or drops a sample restriction whose purpose is unclear. Stop.
   - **WARNING** — defensible but consequential; the user should confirm intent.
   - **PASSED** — cosmetic, or clearly intended and documented.

6. **Report** a table of dimension × verdict with one line of reasoning each. Do **not** accept or apply the change while any BLOCKER stands — escalate to the user. Never change the specification without flagging it and getting approval.
