# Sprint [6] Technical Log

## 1. Planning & Assignments

* **Sprint Dates:** March 17, 2026 – March 31, 2026  
* **Team Name:** JAST | **Members Present:** @Thommond, @arpringle, @stukru42, @JustinMaga26  

* **Sprint Goals:**  
  - Deploy application to production (PythonAnywhere)  
  - Implement CI pipeline and deployment workflow  
  - Configure HTTPS/SSL and validate secure access  
  - Perform final QA testing (pre- and post-deployment)  
  - Document system architecture and user guidance  

| Task Description | Assigned Owner | Priority | Status |
| :--- | :--- | :--- | :--- |
| Deploy application to PythonAnywhere | @Thommond | High | Completed (Issue #80) |
| Create CI pipeline and deployment scaffold | @Thommond | High | Completed (Issue #120) |
| SSL setup and final bug fixes | @Thommond | High | Completed (Issue #81) |
| Perform HTTPS/SSL validation test | @arpringle | High | Completed (Issue #114 / PR #170) |
| QA testing before and after deployment | @JustinMaga26 | High | Completed (Issue #82 / PR #170) |
| Fix Collaborative Veto visualization issues | @arpringle | High | Completed (PR #169) |
| Document final architecture diagram | @stukru42 | Medium | Completed (Issue #116 / PR #168) |
| Draft user manual | @JustinMaga26 | Medium | Completed (PR #167) |

---

## 2. Progress & Blockers

* **Completed Work:**
  - Successfully deployed the Flask application to PythonAnywhere with a functional production environment.
  - Implemented CI pipeline and deployment scaffold to support consistent builds and updates.
  - Configured HTTPS/SSL for secure access to the deployed application.
  - Conducted validation testing confirming SSL certificate functionality and secure connections.
  - Performed full QA testing both before and after deployment to ensure production stability.
  - Resolved prior Sprint 5 visualization issue involving incorrect Collaborative Veto map rendering.
  - Created and finalized system architecture documentation for project handoff clarity.
  - Drafted initial user manual to support usability and onboarding.
  - Maintained strong PR discipline with approvals and traceability across all merged work.

* **Incomplete Tasks:**  
  - None (all Sprint 6 scoped issues completed)

* **Known Issues:**
  - No critical system-level bugs identified post-deployment.
  - Minor improvements may be required in documentation clarity and UI polish (non-blocking).

* **Resolution Plan:**
  - Continue refining documentation and UI consistency if additional iterations occur.
  - Monitor deployed environment for runtime or availability issues.

---

## 3. System Test Report

| Test Case | Type | Result | Evidence/PR # |
| :--- | :--- | :--- | :--- |
| Application deployment to PythonAnywhere | Manual | Passed | Issue #80 |
| CI pipeline execution and deployment flow | Integration | Passed | Issue #120 |
| HTTPS/SSL certificate validation | Manual (Chrome 121, Firefox 122, Windows 10) | Passed | PR #170 |
| Pre-deployment QA validation | Manual | Passed | Issue #82 |
| Post-deployment QA validation | Manual | Passed | PR #170 |
| Collaborative Veto visualization rendering fix | Manual | Passed | PR #169 |
| Architecture documentation completeness | Review | Passed | PR #168 |
| User manual draft validation | Review | Passed | PR #167 |

---

## 4. Bug Tracking

* **Bug Description 1:**  
  Collaborative Veto visualization mapping inconsistency from Sprint 5.  
  - **Severity:** Medium  
  - **Fix Status:** Resolved (PR #169)

* **Bug Description 2:**  
  Minor UI/wording inconsistencies carried from prior sprint.  
  - **Severity:** Low  
  - **Fix Status:** Deferred / Non-blocking

---

## Notes / Evidence

- PR #170: SSL validation testing and QA verification (Issues #114, #82)  
- PR #169: Collaborative Veto visualization fix  
- PR #168: Final architecture documentation  
- PR #167: User manual draft  
- Issue #80: Deployment to PythonAnywhere  
- Issue #120: CI pipeline and deployment scaffold  
- Issue #81: SSL setup and final bug fixes  

All Sprint 6 issues were successfully moved to **Done** and validated through PR approvals and testing evidence.

---

## Sprint Summary

Sprint 6 finalized the project by successfully transitioning from development to a **production-ready deployment**. The application is now securely hosted with HTTPS enabled, supported by a CI-enabled workflow and validated through comprehensive QA testing. Key improvements included resolving outstanding visualization issues, formalizing system architecture documentation, and producing user-facing documentation.

This sprint demonstrates full lifecycle completion, including:
- Deployment
- Security configuration
- Testing rigor
- Documentation readiness

Remaining work is limited to minor refinements, with the system meeting expectations for delivery and handoff.
