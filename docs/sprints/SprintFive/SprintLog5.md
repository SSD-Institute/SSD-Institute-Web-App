# Sprint [5] Technical Log

## 1. Planning & Assignments

* **Sprint Dates:** March 22, 2026 – April 5, 2026  
* **Team Name:** JAST | **Members Present:** @Thommond, @arpringle, @stukru42, @JustinMaga26  

* **Sprint Goals:**  
  - Implement Collaborative Veto (county-level) visualization  
  - Prepare and integrate Wyoming county GeoJSON + dataset  
  - Add testing and QA validation for visualization  
  - Improve accessibility features and finalize README updates  

| Task Description | Assigned Owner | Priority | Status |
| :--- | :--- | :--- | :--- |
| R&D: Obtain WY county boundaries and state boundaries | @Thommond | High | Completed (Issue #101) |
| Prepare WY county GeoJSON | @Thommond | High | Completed (Issue #70) |
| GeoJSON clean + merge county-level data | @Thommond | High | Completed (Issue #103) |
| Prepare sample veto dataset (county level) | @Thommond | High | Completed (Issue #102) |
| Implement Collaborative Veto visualization (Plotly) | @arpringle | High | Completed (Issue #71 / PR #163) |
| Write explanation and supporting details | @Thommond | Medium | Completed (Issue #73 / PR #159) |
| Add test for WY county visualization | @stukru42 | High | Completed (Issue #104) |
| QA Collaborative Veto feature | @Thommond | High | Completed (Issue #150 / PR #164) |
| Perform accessibility check | @stukru42 | Medium | Completed (Issue #115 / PR #160) |
| Update README with Sprint 4 + QA updates | @Thommond | Medium | Completed (PR #164) |

---

## 2. Progress & Blockers

* **Completed Work:**
  - Successfully implemented a county-level Collaborative Veto visualization using Plotly with Wyoming GeoJSON.
  - Built and integrated a structured dataset using FIPS codes aligned with county boundaries.
  - Completed GeoJSON preprocessing, including filtering and formatting for compatibility with Plotly.
  - Developed and validated visualization switching and rendering behavior.
  - Added automated and manual testing for the county visualization module.
  - Conducted full QA pass with validation across environments.
  - Implemented accessibility improvements (high contrast considerations, scalable UI elements).
  - Updated README with Sprint 4 deliverables and QA notes.
  - Maintained consistent workflow discipline with PR approvals and merge validation.

* **Incomplete Tasks:**
  - None (all Sprint 5 scoped issues were completed and closed)

* **Known Issues (Post-QA Findings):**
  - Selecting specific filters (“Approve” / “Veto”) causes state boundary layer to disappear in visualization.
  - Minor text inconsistency in explanation template (“The following” vs. “Below”).

* **Resolution Plan:**
  - Debug layer rendering order and GeoJSON overlay behavior in next sprint.
  - Standardize explanatory text across templates during content refinement phase.

---

## 3. System Test Report

| Test Case | Type | Result | Evidence/PR # |
| :--- | :--- | :--- | :--- |
| Wyoming county GeoJSON loads correctly | Manual (Chrome 121, Firefox 122, Windows 10) | Passed | Issue #70 / #101 |
| County-level data correctly maps to FIPS codes | Integration | Passed | Issue #103 |
| Collaborative Veto visualization renders (default view) | Manual (Chrome 121, Firefox 122, Windows 10) | Passed | PR #163 |
| Visualization switching between scenarios | Manual | Passed | PR #163 |
| Approve/Veto toggle interaction | Manual | Partial (boundary issue) | PR #163 |
| Dataset integrity validation (scenario structure) | Unit | Passed | Issue #102 |
| Visualization test script execution | Automated | Passed | Issue #104 |
| Accessibility feature rendering (contrast/readability) | Manual | Passed | PR #160 |
| QA validation across full feature | Manual | Passed | PR #164 |

---

## 4. Bug Tracking

* **Bug Description 1:**  
  State boundary layer disappears when selecting specific filters (“Approve” / “Veto”) in visualization.  
  - **Severity:** Medium  
  - **Fix Status:** Open (identified, scheduled for next sprint)

* **Bug Description 2:**  
  Minor wording inconsistency in explanation text (“The following” instead of “Below”).  
  - **Severity:** Low  
  - **Fix Status:** Open (content correction planned)

---

## 5. QA Evidence & Validation

- QA documentation location:  
  `/docs/QA/QA.md`

### Supporting Artifacts
- Visualization rendering screenshots  
- Button mapping fix validation  
- Accessibility updates

### QA Owner
- @JustinMaga26  

---

## 6. Workflow & PR Observations

### Strengths
- Achieved Sprint MVP, techincal specifications and collaberation
- Workload collaberation is split

### Areas for Improvement
- Formal reviews and notating Sprints along with closing issues with PRs 

### Next Sprint Actions
- More rigirous QA and timing process to catch bugs quicker in the process a half
way point in the sprint to check for minor errs instead of one QA.
---

## 7. Notes / Evidence

- PR #163: Implementation of Collaborative Veto visualization using Wyoming county GeoJSON  
- PR #159: Dataset creation, explanations, and structural integration  
- PR #164: QA validation and README updates  
- PR #160: Accessibility improvements and UI enhancements  
- Issue #104: Visualization testing implementation  
- Issue #150: QA completion and verification  

All Sprint 5 issues were successfully moved to **Done** in the SSD Workflow and closed with linked PRs and validation evidence.

---

## 8. Sprint Summary

Sprint 5 successfully delivered a fully functional **county-level Collaborative Veto system**, extending the project from national and state-level simulations to localized governance modeling. The integration of GeoJSON data with Plotly demonstrates strong modular design and geospatial handling capability. Testing coverage improved with both automated and manual validation, and accessibility considerations were introduced into the UI.

Primary areas for improvement moving forward include:
- Visualization edge-case handling (layer rendering bugs)
- Continued refinement of UI/UX consistency
- Maintaining strong PR review discipline and test evidence visibility

Overall, Sprint 5 represents a successful expansion in both **technical complexity** and **feature completeness**.