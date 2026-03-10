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

## Sprints
 * [Sprint 1](docs/sprints/SprintOne/SprintLogOne.md)
 * [Sprint 2](docs/sprints/SprintTwo/SprintLogTwo.md)
 * [Sprint 3](docs/sprints/SprintThree/SprintLog3.md)
 * [Sprint 4](docs/sprints/SprintFour/)
 * [Sprint 5](docs/sprints/SprintFive/)
 * [Sprint 6](docs/sprints/SprintSix/)
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

