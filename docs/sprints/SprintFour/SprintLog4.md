# Sprint [4] Technical Log

## 1. Planning & Assignments

* **Sprint Dates:** March 2, 2026 – March 22, 2026  
* **Team Name:** JAST  
* **Members Present:** @Thommond, @arpringle, @stukru42, @JustinMaga26  

### Sprint Goals
- Implement Supreme Court Check (SCV) visualization system  
- Create state-level dataset and GeoJSON integration  
- Add automated testing and CI/CD support  
- Complete QA validation with documented evidence  

| Task Description | Assigned Owner | Priority | Status |
| :--- | :--- | :--- | :--- |
| R&D: State-by-State SC veto dataset (#97) | @Thommond | High | Completed |
| Retrieve & prepare US States GeoJSON (#98) | @Thommond | High | Completed |
| Join SC veto dataset with GeoJSON (#99) | @Thommond | High | Completed |
| Create choropleth visualization (Plotly) | @stukru42 | High | Completed |
| Write explanations + source citations (#69) | @Thommond | Medium | Completed |
| Add automated tests for SC veto visualization (#100) | @stukru42 | High | Completed |
| QA Supreme Court Check + evidence (#149) | @JustinMaga26 | High | Completed |
| Implement CI/CD testing workflow (GitHub Actions) | @stukru42 | Medium | Completed |

---

## 2. Progress & Blockers

### Completed Work
- Developed full **state-level Supreme Court Check dataset**, including legislative weighting and modeled ballot-measure override scenarios  
- Integrated **GeoJSON state boundaries** with dataset  
- Built **Plotly choropleth map** showing:
  - Override states  
  - Non-override states  
  - Conditional/ballot-trigger states  
- Implemented **automated testing** for visualization logic  
- Added **GitHub Actions CI/CD workflow**  
- Completed **formal QA pass** with screenshots and documentation  
- Finalized **case explanations and source citations**  

### Incomplete Tasks
- None  

### Blockers Encountered
- No technical blockers  
- Minor PR workflow friction due to missing formal review submission  

### Resolution Plan (Process Improvements)
- Continue to Require at least **1 reviewer approval before merge**  
- Require **CI checks to pass before merge**  
- Keep the Improvement of **PR granularity** (smaller, more traceable changes)  

---

## 3. System Test Report

| Test Case | Type | Result | Evidence/PR # |
| :--- | :--- | :--- | :--- |
| SCV dataset loads and validates correctly | Unit | Passed | Issue #97 |
| GeoJSON successfully merges with dataset | Integration | Passed | Issue #99 |
| Choropleth renders with correct state coloring | Manual (Chrome 121, Windows 10) | Passed | SCV PR + QA screenshots |
| Choropleth hover displays correct metadata | Manual (Firefox 122, Windows 10) | Passed | QA.md |
| Override threshold (26 states) computed correctly | Unit | Passed | Issue #100 |
| Visualization script runs without errors | Integration | Passed | GitHub Actions logs |
| SCV page loads correctly in UI | Manual (Chrome 121) | Passed | QA screenshots |
| Button mapping consistency across visualizations | Manual | Passed | QA IMG evidence |

---

## 4. Bug Tracking

| Bug Description | Severity | Fix Status |
| :--- | :--- | :--- |
| Visualization button mapping mismatch | Medium | Fixed |
| “Last Updated” GitHub API date inconsistency | Low | Fixed |
| PR merge blocked due to missing review submission | Low | Resolved |

### Notes
- No critical bugs identified  
- Minor issues were documented and resolved with evidence  
- Improved transparency compared to prior sprints  

---

## 5. QA Evidence & Validation

- QA documentation location:  
  `/docs/QA/QA.md`

### Supporting Artifacts
- Visualization rendering screenshots  
- Button mapping fix validation  
- Last-updated timestamp fix verification  

### QA Owner
- @JustinMaga26  

---

## 6. Workflow & PR Observations

### Strengths
- Strong issue-to-PR traceability  
- Clean integration into main branch  
- CI/CD integration improves SDLC maturity  

### Areas for Improvement
- Some PRs merged without formal reviewer approval  
- Large PRs reduced review traceability  
- Contribution distribution remains uneven (noted in retrospective)  

### Next Sprint Actions
- Require **≥1 reviewer approval per PR**  
- Enforce **CI checks before merge**  
- Break PRs into **smaller, testable units**  

---

## 7. Summary

Sprint 4 delivered a complete **Supreme Court Check visualization system**, including dataset creation, geospatial integration, automated testing, and QA validation.  

Compared to Sprint 3:
- **Testing rigor improved**
- **Documentation quality improved**
- **CI/CD introduced**

Remaining gaps are primarily **process-related**, not technical. The system is stable, modular, and ready for further extension.