[Back to README.md](../../../README.md)

# Project Plan

This is the basic project plan and links to details for the project plan. 

## WBS

# Work Breakdown Structure (WBS)  
**Level 1 — SSD Web App**

## 1.0 Project Management
- 1.1 Meeting minutes, RACI, updates

## 2.0 Flask Framework
- 2.1 Setup  
- 2.2 Routing  
- 2.3 Templates  

## 3.0 Visualizations
- 3.1 Multi-Choice Voting  
- 3.2 Supreme Court Veto  
- 3.3 Collaborative Veto  
- 3.4 Minimum Space *(stretch goal)*  

## 4.0 Documentation
- 4.1 Concept pages  
- 4.2 Civic impact summaries  
- 4.3 FAQs & help  

## 5.0 Deployment
- 5.1 PythonAnywhere  
- 5.2 SSL/HTTPS  
- 5.3 Testing/QA  

## 6.0 Maintenance
- 6.1 Version control  
- 6.2 Future roadmap  

# Gahntt Chart Image

Please go to SSD-Institute Organization > Projects > SSD Workflow 
and click the "RoadMap", this is if you have contributer access; if you don't 
you can request it from Thommond / Thom on Github. 

Made with Mermaid Markdown syntax based off Github issues. 

## Critical Path view 

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title SSD Institute – Critical Path Gantt Chart (Stretch Goal Removed, 2026)

    section Sprint 1 Jan 20 – Feb 2
    Flask Scaffold (57)                       :crit, s1a, 2026-01-20, 4d
    Base Routing System (59)                  :crit, s1b, after s1a, 5d
    PythonAnywhere Setup (118)                :crit, s1c, 2026-01-20, 3d
    CI + Deploy Scaffold (58,120)             :crit, s1d, after s1b, 4d
    Documentation Foundations (60,86,87,88)   :crit, s1e, 2026-01-20, 6d

    section Sprint 2 Feb 3 – Feb 16
    Collect Sources (89)                      :crit, s2a, 2026-02-03, 3d
    Draft Definitions (90)                    :crit, s2b, after s2a, 4d
    Create Jinja Templates (61)               :crit, s2c, 2026-02-03, 5d
    Routing Tests (63)                        :crit, s2d, after s2c, 3d
    Visualization Planning (92)               :crit, s2e, 2026-02-03, 4d

    section Sprint 3 Feb 17 – Mar 2
    R&D MC Dataset (93)                       :crit, s3a, 2026-02-17, 4d
    Prep Data (94)                            :crit, s3b, after s3a, 3d
    Build Bar Chart (64)                      :crit, s3c, after s3b, 4d
    Write Explanation (66)                    :crit, s3d, after s3c, 3d
    QA + Tests (65,96)                        :crit, s3e, after s3d, 3d

    section Sprint 4 Mar 3 – Mar 16
    R&D SC Dataset (97)                       :crit, s4a, 2026-03-03, 4d
    Retrieve US GeoJSON (98)                  :crit, s4b, after s4a, 3d
    Merge Data (99)                           :crit, s4c, after s4b, 3d
    Build Choropleth (67)                     :crit, s4d, after s4c, 4d
    Add Legend + Hover (68)                   :crit, s4e, after s4d, 2d
    Write Explanation (69)                    :crit, s4f, after s4e, 3d
    Add Tests (100)                           :crit, s4g, after s4f, 3d

    section Sprint 5 Mar 17 – Mar 30
    R&D WV Boundaries (101)                   :crit, s5a, 2026-03-17, 4d
    Prep Veto Dataset (102)                   :crit, s5b, after s5a, 3d
    GeoJSON Clean + Merge (103)               :crit, s5c, after s5b, 3d
    Build County Map (71)                     :crit, s5d, after s5c, 4d
    Accessibility Review (72)                 :crit, s5e, after s5d, 2d
    Write Explanation (73)                    :crit, s5f, after s5e, 3d
    Add Tests (104)                           :crit, s5g, after s5f, 3d

    section Sprint 6 Mar 31 – Apr 13
    Build Search Bar (74)                     :crit, s6a, 2026-03-31, 4d
    Fuzzy Index (105)                         :crit, s6b, after s6a, 3d
    Term Highlighting (106)                   :crit, s6c, after s6b, 3d
    Performance Optimization (75,108)         :crit, s6d, after s6c, 4d
    Lighthouse + UX Review (107,76)           :crit, s6e, after s6d, 3d

    section Sprint 8 Apr 28 – May 8
    Setup PythonAnywhere (113)                :crit, s8a, 2026-04-28, 3d
    Deploy App (80)                           :crit, s8b, after s8a, 2d
    Domain + SSL (117,119)                    :crit, s8c, after s8b, 2d
    SSL Validation (81,114)                   :crit, s8d, after s8c, 2d
    Accessibility Check (115)                 :crit, s8e, after s8d, 2d
    Final Architecture Diagram (116)          :crit, s8f, after s8e, 2d
    Final QA (82)                             :crit, s8g, after s8f, 2d
```

## Full Features for this portion 

This does not include admin pages. 

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title SSD Institute – Full Project Gantt Chart (All Issues, 2026)

    section Sprint 1 Foundation
    Technical Design Specification (19)        :s1a, 2026-01-20, 4d
    Create PythonAnywhere Account (118)        :s1b, 2026-01-20, 2d
    Purchase Domain Name (117)                 :s1c, 2026-01-20, 2d
    Data Folder Architecture Design (88)       :s1d, 2026-01-20, 3d
    Accessibility Baseline Checklist (87)      :s1e, 2026-01-20, 3d
    Create Concept Definition Templates (86)   :s1f, 2026-01-20, 3d
    Create Flask Scaffold (57)                 :s1g, 2026-01-20, 4d
    CI Workflow (58)                           :s1h, after s1g, 3d
    Base Flask Routing (59)                    :s1i, after s1h, 3d
    Polish Documentation (60)                  :s1j, 2026-01-20, 4d
    CI + Deploy Scaffold to PythonAnywhere (120):s1k, after s1i, 3d

    section Sprint 2 Templates Content
    Define Plotly Implementation (92)          :s2a, 2026-02-03, 4d
    Initial Accessibility Review (91)          :s2b, 2026-02-03, 3d
    Research Governance Texts (89)             :s2c, 2026-02-03, 3d
    Create Jinja Templates (61)                :s2d, 2026-02-03, 4d
    Draft Content Placeholders (62)            :s2e, 2026-02-03, 3d
    Routing + Navigation Testing (63)          :s2f, after s2d, 3d
    Draft Concept Definitions (90)             :s2g, after s2c, 4d

    section Sprint 3 Multi Choice Viz
    Automated Test for MC Viz (96)             :s3a, 2026-02-17, 3d
    Sample MC Dataset (93)                     :s3b, 2026-02-17, 4d
    Plotly Data Functions (95)                 :s3c, after s3b, 3d
    Build MC Bar Chart (64)                    :s3d, after s3c, 4d
    QA + Usability Test (65)                   :s3e, after s3d, 3d
    Write Explanation (66)                     :s3f, after s3e, 3d
    Prep Sample for Bar Chart (94)             :s3g, 2026-02-17, 3d

    section Sprint 4 SC Veto Choropleth
    Tests for SC Viz (100)                     :s4a, 2026-03-03, 3d
    Join SC Data + GeoJSON (99)                :s4b, after s4a, 3d
    Retrieve US States GeoJSON (98)            :s4c, 2026-03-03, 3d
    SC Veto Dataset (97)                       :s4d, 2026-03-03, 4d
    Build SC Choropleth (67)                   :s4e, after s4b, 4d
    Add Legend + Hover (68)                    :s4f, after s4e, 2d
    Write Explanation (69)                     :s4g, after s4f, 3d

    section Sprint 5 WV County Map
    Tests for County Viz (104)                 :s5a, 2026-03-17, 3d
    GeoJSON Clean + Merge (103)                :s5b, after s5a, 3d
    Prep County Veto Dataset (102)             :s5c, 2026-03-17, 3d
    County Boundaries (101)                    :s5d, 2026-03-17, 4d
    WY County GeoJSON (70)                     :s5e, 2026-03-17, 3d
    Build County Map (71)                      :s5f, after s5b, 4d
    Accessibility Review (72)                  :s5g, after s5f, 2d
    Write Explanation (73)                     :s5h, after s5g, 3d

    section Sprint 6 Search Performance
    Fuzzy Search (105)                         :s6a, 2026-03-31, 4d
    Flask Asset Caching (108)                  :s6b, 2026-03-31, 3d
    Term Highlighting (106)                    :s6c, after s6a, 3d
    Search Bar + Highlight (74)                :s6d, after s6c, 3d
    Lighthouse Report (107)                    :s6e, 2026-03-31, 3d
    Optimize Static Assets (75)                :s6f, after s6b, 3d
    Accessibility Contrast (76)                :s6g, after s6e, 3d

    section Sprint 7 Minimum Space Viz
    Transform Functions (111)                  :s7a, 2026-04-14, 4d
    Tests for Minimum Space (112)              :s7b, after s7a, 3d
    Federal Land Boundaries (110)              :s7c, 2026-04-14, 4d
    Minimum Land per Population (109)          :s7d, 2026-04-14, 4d
    Prototype Minimum Space Viz (77)           :s7e, after s7d, 4d
    Integrate Data + Style (78)                :s7f, after s7e, 3d
    Document Concept (79)                      :s7g, after s7f, 3d

    section Sprint 8 Deployment QA
    Setup Flask on PythonAnywhere (113)        :s8a, 2026-04-28, 3d
    Deploy to PythonAnywhere (80)              :s8b, after s8a, 2d
    Architecture Diagram (116)                 :s8c, 2026-04-28, 3d
    Get SSL for Site (119)                     :s8d, 2026-04-28, 3d
    Accessibility Check (115)                  :s8e, 2026-04-28, 2d
    SSL Setup + Bugfixes (81)                  :s8f, after s8d, 2d
    SSL Validation Test (114)                  :s8g, after s8f, 2d
    Final QA Testing (82)                      :s8h, after s8g, 2d
```
## Github Project at Start

![Sprint Image 1](SprintsImage2.png)
![Sprint Image 2](SprintsImage1.png)

Please see the project board for more details


## PMP Table Information 

#### Notes
- **User story mapping**
  - **US‑1:** Definitions + navigation (Home, content pages)
  - **US‑2:** Multiple‑choice / approval bar chart (MC voting)
  - **US‑3:** Supreme Court Check (SC veto choropleth)
  - **US‑4:** Collaborative / County veto maps (WV / county maps)
  - **US‑5:** HTTPS / site security
  - **US‑6:** Search + highlighting + performance
  - **US‑7:** Documentation clarity and publishing
  - **US‑8:** Deployment, hosting, domain
  - **US‑9:** Minimum Space visualization (stretch)
- **Wireframes** referenced the exact filenames `docs/Founding/ScreenSequenceIMG`.  
- **Milestones** match sprints exactly (Sprint 1…Sprint 8) meaning M1-M8 matches sprints.  




| Sprint | Dates               | PMP Task ID | Task                                   | Milestone  | User Story | Screen/Wireframe                                                                                          | Deliverables                                           | Acceptance criteria                                 |
|--------|---------------------|-------------|----------------------------------------|------------|------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|-------------------------------------------------------------|
| 1      | Jan 20–Feb 2, 2026  | 19          | Technical Design Specification         | Sprint 1   | US‑7       | N/A                                                                                                        | Design spec                                            | Spec approved; no major gaps                                 |
| 1      | Jan 20–Feb 2, 2026  | 118         | Create PythonAnywhere Account          | Sprint 1   | US‑8       | N/A                                                                                                        | Host account created                                   | Account active; login verified                               |
| 1      | Jan 20–Feb 2, 2026  | 117         | Purchase Domain Name                   | Sprint 1   | US‑8       | N/A                                                                                                        | Domain purchased                                       | Domain resolves; ownership confirmed                         |
| 1      | Jan 20–Feb 2, 2026  | 88          | Data Folder Architecture Design        | Sprint 1   | US‑7       | N/A                                                                                                        | Data folder structure                                  | Folders created; consistent naming                           |
| 1      | Jan 20–Feb 2, 2026  | 87          | Accessibility Baseline Checklist       | Sprint 1   | US‑5       | [MobileLandingPage.png](../../docs/Founding/ScreenSequenceIMG/MobileLandingPage.png)                       | Baseline checklist                                     | Checklist completed; issues logged                           |
| 1      | Jan 20–Feb 2, 2026  | 86          | Concept Definition Templates           | Sprint 1   | US‑7       | [DesktopLandingPage.png](../../docs/Founding/ScreenSequenceIMG/DesktopLandingPage.png)                     | Template files                                         | Templates render without errors                              |
| 1      | Jan 20–Feb 2, 2026  | 57          | Create Flask Scaffold                  | Sprint 1   | US‑8       | N/A                                                                                                        | Flask app scaffold                                     | App runs locally                                             |
| 1      | Jan 20–Feb 2, 2026  | 58          | CI Workflow                            | Sprint 1   | US‑8       | N/A                                                                                                        | CI pipeline                                            | CI passes on push                                            |
| 1      | Jan 20–Feb 2, 2026  | 59          | Base Flask Routing                     | Sprint 1   | US‑1       | [MobileLandingPage.png](../../docs/Founding/ScreenSequenceIMG/MobileLandingPage.png)                       | Base routes                                            | Routes return 200                                            |
| 1      | Jan 20–Feb 2, 2026  | 60          | Polish Documentation                   | Sprint 1   | US‑7       | [DesktopLandingPage.png](../../docs/Founding/ScreenSequenceIMG/DesktopLandingPage.png)                     | Project docs                                           | Docs updated; links work                                     |
| 1      | Jan 20–Feb 2, 2026  | 120         | CI + Deploy Scaffold to PythonAnywhere | Sprint 1   | US‑8       | N/A                                                                                                        | Deployment job                                         | App deploys to host                                          |
| 2      | Feb 3–Feb 16, 2026  | 92          | Define Plotly Implementation           | Sprint 2   | US‑2       | [MultipleChoiceVotingDesktopPage.png](../../docs/Founding/ScreenSequenceIMG/MultipleChoiceVotingDesktopPage.png) | Plotly plan + prototype                                | Prototype renders a sample chart                             |
| 2      | Feb 3–Feb 16, 2026  | 91          | Initial Accessibility Review           | Sprint 2   | US‑1       | [MobileLandingPage.png](../../docs/Founding/ScreenSequenceIMG/MobileLandingPage.png)                       | A11y review report                                     | Key issues listed; basic fixes begun                         |
| 2      | Feb 3–Feb 16, 2026  | 89          | Research Governance Texts              | Sprint 2   | US‑1       | [DesktopLandingPage.png](../../docs/Founding/ScreenSequenceIMG/DesktopLandingPage.png)                     | Source list                                            | Sources cited; accessible formats                            |
| 2      | Feb 3–Feb 16, 2026  | 61          | Create Jinja Templates                 | Sprint 2   | US‑1       | [MobileMenuPage.png](../../docs/Founding/ScreenSequenceIMG/MobileMenuPage.png)                             | Templates for pages                                    | Pages render; layout stable                                  |
| 2      | Feb 3–Feb 16, 2026  | 62          | Draft Content Placeholders             | Sprint 2   | US‑1       | [DesktopMenuViewPage.png](../../docs/Founding/ScreenSequenceIMG/DesktopMenuViewPage.png)                   | Draft content + placeholders                           | Content visible; links present                               |
| 2      | Feb 3–Feb 16, 2026  | 63          | Routing + Navigation Testing           | Sprint 2   | US‑1       | [DesktopMenuViewPage.png](../../docs/Founding/ScreenSequenceIMG/DesktopMenuViewPage.png)                   | Navigation test suite                                  | All nav paths work                                           |
| 2      | Feb 3–Feb 16, 2026  | 90          | Draft Concept Definitions              | Sprint 2   | US‑1       | [DesktopLandingPage.png](../../docs/Founding/ScreenSequenceIMG/DesktopLandingPage.png)                     | Draft definitions                                      | Word count met; clarity passes                               |
| 3      | Feb 17–Mar 2, 2026  | 96          | Automated Test for MC Viz              | Sprint 3   | US‑2       | [MultipleChoiceVotingDesktopPage.png](../../docs/Founding/ScreenSequenceIMG/MultipleChoiceVotingDesktopPage.png) | Test suite for MC viz                                  | Tests green for viz                                          |
| 3      | Feb 17–Mar 2, 2026  | 93          | Sample MC Dataset                      | Sprint 3   | US‑2       | [MultipleChoiceVotingDesktopPage.png](../../docs/Founding/ScreenSequenceIMG/MultipleChoiceVotingDesktopPage.png) | Sample dataset                                         | Dataset loads; basic stats OK                                |
| 3      | Feb 17–Mar 2, 2026  | 95          | Plotly Data Functions                  | Sprint 3   | US‑2       | [MultipleChoiceVotingDesktopPage.png](../../docs/Founding/ScreenSequenceIMG/MultipleChoiceVotingDesktopPage.png) | Data transform functions                               | Functions return expected output                             |
| 3      | Feb 17–Mar 2, 2026  | 64          | Build MC Bar Chart                     | Sprint 3   | US‑2       | [MultipleChoiceVotingDesktopPage.png](../../docs/Founding/ScreenSequenceIMG/MultipleChoiceVotingDesktopPage.png) | Bar chart                                              | Chart renders; labels clear; loads < 3s                      |
| 3      | Feb 17–Mar 2, 2026  | 65          | QA + Usability Test                    | Sprint 3   | US‑2       | [MultipleChoiceVotingDesktopPage.png](../../docs/Founding/ScreenSequenceIMG/MultipleChoiceVotingDesktopPage.png) | QA checklist + findings                                | No blocking issues                                           |
| 3      | Feb 17–Mar 2, 2026  | 66          | Write Explanation                      | Sprint 3   | US‑2       | [MultipleChoiceVotingDesktopPage.png](../../docs/Founding/ScreenSequenceIMG/MultipleChoiceVotingDesktopPage.png) | Explanation text                                       | Text published; links valid                                  |
| 3      | Feb 17–Mar 2, 2026  | 94          | Prep Sample for Bar Chart              | Sprint 3   | US‑2       | [MultipleChoiceVotingDesktopPage.png](../../docs/Founding/ScreenSequenceIMG/MultipleChoiceVotingDesktopPage.png) | Prepared sample data                                   | Data formatted for chart                                     |
| 4      | Mar 3–Mar 16, 2026  | 100         | Tests for SC Viz                       | Sprint 4   | US‑3       | [SupremeCourtCheckDesktop.png](../../docs/Founding/ScreenSequenceIMG/SupremeCourtCheckDesktop.png)           | Test suite                                             | Tests green                                                  |
| 4      | Mar 3–Mar 16, 2026  | 99          | Join SC Data + GeoJSON                 | Sprint 4   | US‑3       | [SupremeCourtCheckDesktop.png](../../docs/Founding/ScreenSequenceIMG/SupremeCourtCheckDesktop.png)           | Merged dataset                                         | Merge complete; spot check OK                                |
| 4      | Mar 3–Mar 16, 2026  | 98          | Retrieve US States GeoJSON             | Sprint 4   | US‑3       | [SupremeCourtCheckMobile.png](../../docs/Founding/ScreenSequenceIMG/SupremeCourtCheckMobile.png)             | GeoJSON acquired                                       | File loads; schema valid                                     |
| 4      | Mar 3–Mar 16, 2026  | 97          | SC Veto Dataset                        | Sprint 4   | US‑3       | [SupremeCourtCheckDesktop.png](../../docs/Founding/ScreenSequenceIMG/SupremeCourtCheckDesktop.png)           | Dataset R&D                                            | Fields defined; sample ready                                 |
| 4      | Mar 3–Mar 16, 2026  | 67          | Build SC Choropleth                    | Sprint 4   | US‑3       | [SupremeCourtCheckDesktop.png](../../docs/Founding/ScreenSequenceIMG/SupremeCourtCheckDesktop.png)           | Choropleth map                                         | Map renders; colors correct                                  |
| 4      | Mar 3–Mar 16, 2026  | 68          | Add Legend + Hover                     | Sprint 4   | US‑3       | [SupremeCourtCheckDesktop.png](../../docs/Founding/ScreenSequenceIMG/SupremeCourtCheckDesktop.png)           | Legend + hover interactivity                           | Legend readable; hover shows exact counts                    |
| 4      | Mar 3–Mar 16, 2026  | 69          | Write Explanation + Citations          | Sprint 4   | US‑3       | [SupremeCourtCheckDesktop.png](../../docs/Founding/ScreenSequenceIMG/SupremeCourtCheckDesktop.png)           | Explanation + citations                                | Text published; citations present                            |
| 5      | Mar 17–Mar 30, 2026 | 104         | Tests for County Viz                   | Sprint 5   | US‑4       | [CollaberativeVetoDeskopPage.png](../../docs/Founding/ScreenSequenceIMG/CollaberativeVetoDeskopPage.png)     | Test suite                                             | Tests green                                                  |
| 5      | Mar 17–Mar 30, 2026 | 103         | GeoJSON Clean + Merge                  | Sprint 5   | US‑4       | [CollaberativeVetoDeskopPage.png](../../docs/Founding/ScreenSequenceIMG/CollaberativeVetoDeskopPage.png)     | Cleaned + merged GeoJSON                               | Valid GeoJSON; no errors                                     |
| 5      | Mar 17–Mar 30, 2026 | 102         | Prep County Veto Dataset               | Sprint 5   | US‑4       | [CollaberativeVetoMobilePage.png](../../docs/Founding/ScreenSequenceIMG/CollaberativeVetoMobilePage.png)     | Prepared dataset                                       | Dataset fields complete                                      |
| 5      | Mar 17–Mar 30, 2026 | 101         | County Boundaries                      | Sprint 5   | US‑4       | [CollaberativeVetoDeskopPage.png](../../docs/Founding/ScreenSequenceIMG/CollaberativeVetoDeskopPage.png)     | Boundary research                                      | Counties verified                                            |
| 5      | Mar 17–Mar 30, 2026 | 70          | WY County GeoJSON                      | Sprint 5   | US‑4       | [CollaberativeVetoMobilePage.png](../../docs/Founding/ScreenSequenceIMG/CollaberativeVetoMobilePage.png)     | WY County GeoJSON                                      | File loads; counties match                                   |
| 5      | Mar 17–Mar 30, 2026 | 71          | Build County Map                       | Sprint 5   | US‑4       | [CollaberativeVetoDeskopPage.png](../../docs/Founding/ScreenSequenceIMG/CollaberativeVetoDeskopPage.png)     | County map                                             | Map renders without errors                                   |
| 5      | Mar 17–Mar 30, 2026 | 72          | Accessibility + Style Review           | Sprint 5   | US‑4       | [CollaberativeVetoMobilePage.png](../../docs/Founding/ScreenSequenceIMG/CollaberativeVetoMobilePage.png)     | Review checklist                                       | Issues logged; critical fixed                                |
| 5      | Mar 17–Mar 30, 2026 | 73          | Write Explanation + Details            | Sprint 5   | US‑4       | [CollaberativeVetoDeskopPage.png](../../docs/Founding/ScreenSequenceIMG/CollaberativeVetoDeskopPage.png)     | Explanation                                            | Text published                                               |
| 6      | Mar 31–Apr 13, 2026 | 105         | Implement Fuzzy Search                 | Sprint 6   | US‑6       | [SearchDesktop.png](../../docs/Founding/ScreenSequenceIMG/SearchDesktop.png)                                  | Fuzzy search                                           | Finds close matches                                          |
| 6      | Mar 31–Apr 13, 2026 | 108         | Flask Asset Caching                    | Sprint 6   | US‑6       | [SearchDesktop.png](../../docs/Founding/ScreenSequenceIMG/SearchDesktop.png)                                  | Caching approach                                       | Assets cached; load faster                                   |
| 6      | Mar 31–Apr 13, 2026 | 106         | Implement Term Highlighting            | Sprint 6   | US‑6       | [SearchDesktop.png](../../docs/Founding/ScreenSequenceIMG/SearchDesktop.png)                                  | Term highlighting                                      | Highlights correct terms                                     |
| 6      | Mar 31–Apr 13, 2026 | 74          | Search Bar + Highlight                 | Sprint 6   | US‑6       | [SearchDesktop.png](../../docs/Founding/ScreenSequenceIMG/SearchDesktop.png)                                  | Search UI                                              | Search executes; no errors                                   |
| 6      | Mar 31–Apr 13, 2026 | 107         | Lighthouse Report                      | Sprint 6   | US‑6       | [SearchDesktop.png](../../docs/Founding/ScreenSequenceIMG/SearchDesktop.png)                                  | Lighthouse results                                     | Performance ≥ target threshold                               |
| 6      | Mar 31–Apr 13, 2026 | 75          | Optimize Static Assets                 | Sprint 6   | US‑6       | [SearchDesktop.png](../../docs/Founding/ScreenSequenceIMG/SearchDesktop.png)                                  | Optimized assets                                       | Reduced bundle size                                          |
| 6      | Mar 31–Apr 13, 2026 | 76          | Accessibility + Color Contrast         | Sprint 6   | US‑6       | [SearchDesktop.png](../../docs/Founding/ScreenSequenceIMG/SearchDesktop.png)                                  | Contrast adjustments                                   | Passes contrast checks                                       |
| 7      | Apr 14–Apr 27, 2026 | 111         | Transform Functions                    | Sprint 7   | US‑9       | [MinimumAmountOfSpacePage.png](../../docs/Founding/ScreenSequenceIMG/MinimumAmountOfSpacePage.png)           | Transform utilities                                    | Functions run; sample output OK                              |
| 7      | Apr 14–Apr 27, 2026 | 112         | Tests for Minimum Space                | Sprint 7   | US‑9       | [MinimumAmountOfSpacePage.png](../../docs/Founding/ScreenSequenceIMG/MinimumAmountOfSpacePage.png)           | Test suite                                             | Tests green                                                  |
| 7      | Apr 14–Apr 27, 2026 | 110         | Federal Land Boundaries                | Sprint 7   | US‑9       | [MinimumAmountOfSpaceDesktop.png](../../docs/Founding/ScreenSequenceIMG/MinimumAmountOfSpaceDesktop.png)     | Boundary dataset                                       | Dataset loads; fields defined                                |
| 7      | Apr 14–Apr 27, 2026 | 109         | Minimum Land per Population            | Sprint 7   | US‑9       | [MinimumAmountOfSpaceDesktop.png](../../docs/Founding/ScreenSequenceIMG/MinimumAmountOfSpaceDesktop.png)     | Metric approach                                        | Formula agreed; sample calc OK                               |
| 7      | Apr 14–Apr 27, 2026 | 77          | Prototype Minimum Space Viz            | Sprint 7   | US‑9       | [MinimumAmountOfSpaceDesktop.png](../../docs/Founding/ScreenSequenceIMG/MinimumAmountOfSpaceDesktop.png)     | Prototype visualization                                 | Renders; basic interactivity works                           |
| 7      | Apr 14–Apr 27, 2026 | 78          | Integrate Data + Style                 | Sprint 7   | US‑9       | [MinimumAmountOfSpaceDesktop.png](../../docs/Founding/ScreenSequenceIMG/MinimumAmountOfSpaceDesktop.png)     | Integrated viz                                         | Styles consistent; data linked                                |
| 7      | Apr 14–Apr 27, 2026 | 79          | Document Concept                       | Sprint 7   | US‑9       | [MinimumAmountOfSpaceDesktop.png](../../docs/Founding/ScreenSequenceIMG/MinimumAmountOfSpaceDesktop.png)     | Concept doc                                            | Published; readable                                           |
| 8      | Apr 28–May 8, 2026  | 113         | Setup Flask on PythonAnywhere          | Sprint 8   | US‑8       | [ContactUsDesktopPage.png](../../docs/Founding/ScreenSequenceIMG/ContactUsDesktopPage.png)                 | Hosted Flask app                                      | App reachable on domain                                       |
| 8      | Apr 28–May 8, 2026  | 80          | Deploy to PythonAnywhere               | Sprint 8   | US‑8       | [ContactUsDesktopPage.png](../../docs/Founding/ScreenSequenceIMG/ContactUsDesktopPage.png)                 | Deployment script                                     | Deploy runs cleanly                                           |
| 8      | Apr 28–May 8, 2026  | 116         | Architecture Diagram                   | Sprint 8   | US‑7       | [ContactUsDesktopPage.png](../../docs/Founding/ScreenSequenceIMG/ContactUsDesktopPage.png)                 | Architecture diagram                                   | Diagram published; components clear                            |
| 8      | Apr 28–May 8, 2026  | 119         | Get SSL for Site                       | Sprint 8   | US‑5       | [ContactUsMobilePage.png](../../docs/Founding/ScreenSequenceIMG/ContactUsMobilePage.png)                   | SSL certificate                                        | Issued; valid dates                                            |
| 8      | Apr 28–May 8, 2026  | 115         | Accessibility Check                    | Sprint 8   | US‑7       | [ContactUsMobilePage.png](../../docs/Founding/ScreenSequenceIMG/ContactUsMobilePage.png)                   | Accessibility report                                   | No critical issues                                             |
| 8      | Apr 28–May 8, 2026  | 81          | SSL Setup + Bugfixes                   | Sprint 8   | US‑5       | [ContactUsMobilePage.png](../../docs/Founding/ScreenSequenceIMG/ContactUsMobilePage.png)                   | SSL configuration                                     | HTTPS works; no mixed content                                  |
| 8      | Apr 28–May 8, 2026  | 114         | HTTPS/SSL Validation Test              | Sprint 8   | US‑5       | [ContactUsMobilePage.png](../../docs/Founding/ScreenSequenceIMG/ContactUsMobilePage.png)                   | Validation test suite                                  | Tests green; cert chain valid                                  |
| 8      | Apr 28–May 8, 2026  | 82          | Final QA Testing                       | Sprint 8   | US‑7       | [ContactUsDesktopPage.png](../../docs/Founding/ScreenSequenceIMG/ContactUsDesktopPage.png)                 | QA sign‑off                                            | No P1 issues; sign‑off recorded                                |



