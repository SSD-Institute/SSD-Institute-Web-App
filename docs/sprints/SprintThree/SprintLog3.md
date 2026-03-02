# Sprint 3 Technical Log

## 1. Planning & Assignments

**Sprint Dates:** Feb 16, 2026 – March 1, 2026
**Team Name:** JAST
**Members Present (Planning & Review):** @Thommond, @arpringle, @stukru42, @JustinMaga26

### Sprint Goal

Deliver the core Multiple-Choice (Approval) Voting Plotly visualization for MVP:

* Historical dataset R&D
* Data cleaning & normalization
* Modular Plotly bar chart implementation
* QA & usability validation
* Documentation of data provenance

This sprint fulfills:

* **US Citizen 2 – Bar Chart Visualization**
* **US Developer 2 – Modularity**
* **US Developer 5 – Testing**

---

### Planned Tasks vs Ownership (Per GitHub Issues)

| Issue # | Task Description                                                       | Assigned Owner | Priority | Status    |
| ------- | ---------------------------------------------------------------------- | -------------- | -------- | --------- |
| #93     | R&D: Find or create sample multi-choice dataset                        | @Thommond      | High     | Completed |
| #94     | Prep & clean dataset for visualization                                 | @Thommond      | High     | Completed |
| #95     | Write Plotly-specific data functions (normalize, sort, validate, test) | @arpringle @stukru42      | High     | Completed |
| #64     | Build Plotly bar chart module                                          | @arpringle      | High     | Completed |
| #66     | Write governance explanation for visualization                         | @Thommond      | High     | Completed |
| #96     | Add automated test for MC voting visualization                         | @stukru42      | High     | Completed |
| #65     | QA + usability test (GitHub + production review)                       | @JustinMaga26  | High     | Completed |

All Sprint 3 issues were moved to Done or Ready and merged via PR #142 and PR #143.

No tasks carried over.

---

## 2. Progress & Accountability

### Completed Work

* Created historically grounded approval voting dataset (U.S. election case study).
* Cleaned and validated dataset prior to visualization.
* Implemented normalization and sorting functions for modular reuse.
* Built independent Plotly bar chart module (no cross-module dependencies).
* Added automated testing scaffolding for visualization module (#96).
* Conducted QA and usability review across GitHub workflow and production site (#65).
* Added source documentation file detailing data provenance.
* Consolidated implementation into PR #143 after peer review.
* Maintained branch discipline (`feature/* → develop`).

### Incomplete Tasks

None.

### Blockers

None.

No dependency conflicts, merge conflicts, or environment failures.

---

## 3. System Test Report

All tests executed prior to merge into `main`

| Test Case                                                           | Type        | Result | Environment                           | Evidence  |
| ------------------------------------------------------------------- | ----------- | ------ | ------------------------------------- | --------- |
| Dataset loads correctly into module                                 | Unit        | Passed | Python 3.11 (local)                   | PR #143   |
| Normalize function returns expected values                          | Unit        | Passed | Python 3.11 (local)                   | PR #143   |
| Sorting maintains data integrity                                    | Unit        | Passed | Python 3.11 (local)                   | PR #143   |
| Plotly chart renders without JS errors                              | Integration | Passed | Chrome 121 / Firefox 122 (Windows 10) | PR #143   |
| Visualization loads < 3 seconds                                     | Manual      | Passed | Localhost + Production                | PR #143   |
| Modular independence verified                                       | Integration | Passed | Develop branch build                  | PR #143   |
| Automated test scaffold executes without failure                    | Unit        | Passed | Flask test client                     | Issue #96 |
| QA + usability pass (UI clarity, readability, navigation stability) | Manual      | Passed | Production Site Review                | Issue #65 |

Manual tests explicitly executed in:

* Chrome 121
* Firefox 122
* Windows 10 environment

Peer review comments addressed prior to merge.

---

## 4. Bug Tracking

| Severity | Description                      | Status | Fix PR |
| -------- | -------------------------------- | ------ | ------ |
| N/A      | No high-severity bugs discovered | N/A    | N/A    |

No regressions introduced.
No UI crashes observed.
No performance degradation.

---

## 5. Workflow Integrity

Branching Strategy (Confirmed):

* `main` → production
* `develop` → integration
* `feature/*` → isolated development

Sprint 3 Workflow Strengths:

* Clear issue ownership
* Active peer review before merge
* QA independent from implementation
* Commit messages followed `feat:` / `fix:` conventions
* Project Board updated in real time

Improvement Opportunity:
PR #143 consolidated multiple issues. While efficient, smaller PRs may improve review traceability in future sprints.

---

## 6. Retrospective

### What Went Well

* Clean modular Plotly implementation.
* Dataset R&D completed early, preventing downstream delays.
* Automated testing introduced for visualization module.
* QA performed independently of implementation.
* No blockers; sprint completed fully on schedule.

### Areas for Improvement

* Break large PRs into smaller units for clearer review history.
* Improve font scaling consistency (noted in prior sprint feedback).

### Lessons Learned

* Explicit validation functions reduce future regression risk.
* Documentation of simulated vs. historical data protects academic integrity.
* Integrating testing during development (not after) improves reliability.

---

## 7. Actionable Goals for Sprint 4

1. Expand automated test coverage (Owner: @stukru42)
2. Improve UI typography scaling and accessibility (Owner: @arpringle)
3. Add additional historical voting case examples (Owner: @Thommond)
4. Update CI/CL or Python Anywhere to run mcv_viz.py file (Owner: @Thommond)
5. Set up pytest on the actual Github Repo README.md status (Owner: @Thommond)

Assigned in GitHub Project Board.

