# SSD-Institute-Web-App
The Scientific Self-Determination (SSD) Project is a civic education platform designed to empower the general public and non-profit organizations by simulating alternative governance models through an interactive Flask web application. The application uses data visualizations to demystify complex concepts like collaborative vetoes and multi-choice voting, helping citizens understand how local empowerment and direct participation can shift political decision-making. By providing these clear, visual tools, the project aims to foster informed consent in government and inspire discussions regarding more adaptable, representative democratic systems.

## Founding Documentation

The following links are a table of contents to our founding documentation 

* [Project Charter](docs/Founding/ProjectCharter.md)
* [Project Scope](docs/Founding/scopedoc.md)
* [FAQ Doc](docs/Mission/FAQSSD.md)
* [Governace Concepts](docs/Mission/GovernaceConcepts.md)
* [User Stories](docs/Founding/UserStories.md)
* [Topology Diagram](docs/Founding/IMG/toplogyDiagram.png)
* [ERD Diagram](docs/Founding/ERD/erdandtext.md)
* [DFD Level 0](docs/Founding/DFD/DFD0AndBriefText.md)
* [DFD Level 1](docs/Founding/DFD/DFD1AndBriefText.md)
* [DFD Level 2](docs/Founding/DFD/DFD2AndBriefText.md)
* [Screen Sequence](docs/Founding/ScreenSequenceIMG/ScreenSequence.md)
* [Project Plan](docs/Founding/ProjectPlan/ProjectPlan.md)
* [Database Script](docs/Founding/DBScript.sql)

## Our Progress
* [Meeting Minutes](docs/Meeting_Minutes/)
* [RACI Matrix](docs/Founding/RACIMatrix.md)

## Development Workflow

Branching Strategy:

* `main` → production
* `develop` → integration
* `feature/*` → isolated development

## Sprint Release

### Sprint 1
 * **New Features** 
    - **Application & Deployment**
      - Established the initial Flask project scaffold. 
      - Deployed the app on PythonAnywhere:
      - Configured CName and DNS for **www.ssdinstitute.net**
      - Set up a virtual environment and installed core dependencies (Flask, Gunicorn, etc.)
      - Implemented a GitHub Actions CI/CD pipeline with automated deployment triggered via curl-based API updates.

    * **Frontend & Templates**
      - Created base Jinja2 templates for the Home and Contact pages.
      - Added “Concept Definition” templates for:
      - Collaborative Veto  
      - Minimum Space  
      - Multiple-Choice Voting  
      - Supreme Court Check  

    * **Data Architecture**
      - Added a structured `data` directory within the Flask app.
      - Created subfolders for raw, processed, and sample data to support future visualizations.


* **Test Credentials** - Currently, we do not have test credentials available for site access. This item is planned for a future sprint.

### Sprint 2
* **New Features** 
  *  **Core Web Infrastructure**
     - Deployed Flask scaffolding and launched the production site at **ssdinstitute.net**.
     - Built a modular **base.html** template system for consistent layout and reduced duplication.
     - Implemented production-ready routing in **application.py** for all core concept pages.

  *  **Concept Pages (Research + UI Integration)**
     - **Collaborative Veto:** Added UI backed by Concurrent Majority theory and federalism data (Census of Governments, CRS).
     - **Supreme Court Check:** Integrated research on the Virginia/Kentucky Resolutions and judicial structure.
     - **Multiple Choice Voting:** Documented alternative voting systems using Maine/NYC rules and approval voting standards.
     - **Minimum Space Concept:** Applied Georgist land theory and GIS datasets (USGS/USDA) to spatial allocation formulas.

  *  **Repository & Project Management** 
     - Refactored the repo structure, removing duplicates and organizing documentation under **docs/**.
     - Linked commits and PRs to a centralized project board for transparent issue tracking.

* **Test Credentials** - Currently, we do not have test credentials available for site access. This item is planned for a future sprint.

### Sprint 3
* **New Features** - Multiple-Choice Voting (MCV) allows users to explore a voting system where electors can support multiple candidates simultaneously, rather than being restricted to a single choice. This prevents "spoiler effects" and more accurately reflects the broad preferences of a community.
   - **What the User Sees**: Interactive bar charts (grouped by voting method) showing the total votes for each candidate. The ability to toggle between different historical election simulations (e.g., 1824, 1992, and 2000).
   - **How Data is Generated:**: The system utilizes official Federal Election Commission (FEC) and National Archives data for actual plurality results.
     Simulation Modeling: Approval Voting totals are modeled based on political science literature (e.g., Brams & Fishburn) to estimate cross-candidate support.
     Visualization Pipeline: A Python script (mcv_viz_prod.py) processes this data using Pandas and Plotly Express to generate standalone HTML visualization files.
   -  **How to Extend It (Data Workflow)**: 
         + Step 1: Raw Data Storage: New election data must first be added to the raw data file (data/raw/). At this   stage, the data is stored but not yet visible on the website.
         + Step 2: Processing: Run the processing script. This script transforms the raw dictionary data into processed HTML files using Pandas and Plotly.
         + Step 3: Viewing: Once the data is placed in the processed data directory (/static/visualizations/mcv/), the Flask application automatically detects the new file and makes it viewable on the live site.
 * **Test Credentials** - Currently, we do not have test credentials available for site access. This item is planned for a future sprint.

### Sprint 4
* **New Features**

  * **Supreme Court Check (Visualization System)**
    - Implemented a full-stack interactive choropleth map to model how states might respond to federal rulings under the *Supreme Court Veto* concept.
    - **What the User Sees**:
      - A dynamic U.S. map with state-level classifications (Support, Override, Mixed).
      - Toggle controls for switching between historical and simulated case studies (e.g., *Brown v. Board*, *Dobbs*, *Shelby County*).
    - **Geospatial Data Integration**:
      - Added a standardized GeoJSON mapping layer aligning state boundaries with judicial and legislative sentiment datasets.
    - **Interactive UI Components**:
      - Built a JavaScript-driven “switcher bar” using Jinja2 templates to swap between case visualizations without reloading the page.

  * **Automated QA & CI/CD**
    - Added automated tests for visualization logic within the GitHub Actions workflow.
    - Implemented a pytest suite to validate GeoJSON loading and correct color-scale rendering for choropleth maps.
    - Updated the deployment pipeline to automatically regenerate and move processed visualization files into the production `static/` directory after a successful merge.

  * **Documentation & Metadata**
    - Added standardized “Last Updated” timestamps across all concept pages.
    - Expanded technical documentation with workflows for adding new Supreme Court cases to the visualization pipeline.
    - Documented judicial and legislative data sources used in simulation modeling (Oyez, Cornell Law, historical state legislative records).

  * **Repository & Workflow Enhancements**
    - Updated the pull-request workflow to require at least one reviewer approval for visualization-related scripts.
    - Resolved a navigation bug where header highlights did not correctly reflect the active concept page.

* **Test Credentials**  
  Currently, we do not have test credentials available for site access. This item is planned for a future sprint.


### Sprint 5
* **New Features**

  * **Collaborative Veto (County-Level Visualization)**
    - Implemented a county-level choropleth map using Wyoming as a case study.
    - **What the User Sees**:
      - A state map displaying counties color-coded based on support (approve/veto) outcomes.
      - Multiple scenarios representing different policy simulations.
    - **Geospatial Data Integration**:
      - Integrated U.S. Census-derived county GeoJSON data (filtered to Wyoming).
      - Mapped FIPS codes to simulated voting outcomes.
    - **Scenario-Based Data Modeling**:
      - Created datasets modeling county-level responses to controversial state policies.
      - Applied simple majority rule (51% of counties) to determine veto outcomes.
    - **Known Issues (Documented)**:
      - State boundary rendering issue when toggling specific approval/veto views.
      - Minor UI wording inconsistency in explanation text.

  * **Testing & QA Enhancements**
    - Added dedicated test cases for county-level visualization rendering.
    - Documented QA findings with supporting screenshots in `/docs/QA/`.
    - Verified correct mapping between dataset values and visual output.

  * **Accessibility Improvements**
    - Introduced accessibility-focused UI enhancements:
      - High-contrast compatibility
      - Improved readability considerations
    - Established groundwork for future accessibility expansion.

  * **Repository & Workflow Updates**
    - Cleaned and merged GeoJSON datasets with simulation data.
    - Maintained traceability between issues, PRs, and visualization outputs.
    - Continued enforcement of PR review and QA validation prior to merge.

* **Test Credentials**  
  Currently, we do not have test credentials available for site access. This item is planned for a future sprint.

### Sprint 6
* **New Features**

  * **Production Deployment & Infrastructure**
    - Successfully deployed the full application to PythonAnywhere production environment.
    - Configured domain routing and ensured application availability via **HTTPS/SSL**.
    - Completed SSL certificate setup for secure communication.

  * **CI/CD & Deployment Pipeline**
    - Finalized CI/CD pipeline for automated deployment from GitHub to production.
    - Ensured consistency between local development, staging, and production environments.

  * **Final QA & Validation**
    - Conducted full-system QA testing before and after deployment.
    - Validated:
      - Visualization rendering across all modules (MCV, SCV, Collaborative Veto)
      - Navigation and routing integrity
      - External API functionality (GitHub “last updated” feature)
    - Performed HTTPS/SSL validation testing to confirm secure site behavior.

  * **Bug Fixes & Stability Improvements**
    - Resolved Collaborative Veto visualization mapping issue identified in Sprint 5.
    - Addressed UI inconsistencies and minor rendering issues.
    - Improved overall system stability for production use.

  * **Documentation & Final Deliverables**
    - Created final system architecture documentation.
    - Developed initial user manual draft for system handoff.
    - Updated README with complete sprint history and feature documentation.

  * **Testing & Evidence**
    - Added final QA validation artifacts and documentation.
    - Ensured all completed issues include traceable evidence of testing and resolution.

* **Test Credentials**  
  No authentication is required to access the application at this stage.

## Sprints
 * [Sprint 1](docs/sprints/SprintOne/SprintLogOne.md)
 * [Sprint 2](docs/sprints/SprintTwo/SprintLogTwo.md)
 * [Sprint 3](docs/sprints/SprintThree/SprintLog3.md)
 * [Sprint 4](docs/sprints/SprintFour/SprintLog4.md)
 * [Sprint 5](docs/sprints/SprintFive/SprintLog5.md)
 * [Sprint 6](docs/sprints/SprintSix/SprintLog6.md)
 * [Sprint 7](docs/sprints/SprintSeven/)
 * [Sprint 8](docs/sprints/SprintEight/)
 

## Contributions 
1. Fork repository 
2. Contribute in the fork with your changes 
3. Pull upstream, and push your changes to your fork
4. Open a pull request to the original repo
5. Notify team so someone can review; keep watch for comments
6. Update issue in Github projects, DevOps will close

## Website 
* [Home Page](SSDFlask/templates/home.html) 
* [data Processed](SSDflask/data/processed/)
* [data Raw](SSDflask/data/raw/)
* [data Sample](SSDflask/data/sample/)
* [Accessibility](docs/Accessibility/)  
* [Style sheet](SSDFlask/static/style.css)

[Getting Started Devs](docs/Founding/GettingStarted.md)

We are a not currently open to contributions beyond our seed team at this time. Contributions may open to the public after May 2026.

