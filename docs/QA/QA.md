# QA Session: Issues and Fixes Sprint 3

During the QA portion of the presentation, Justin and Thom addressed several bugs and refinements that surfaced during the sprint.

   ## 1. Navigation Indicator
**Issue:**  
When selecting a new page, the navigation indicator (the purple highlight in the header) was not updating correctly to show the active section.

[Navigation Indicator Issue](IMG/NavigationIndicatorIssue.PNG)

**Fix:**  
The team identified the issue in base.html the header template. Although the fix was implemented, were waiting for the server to fully update and deploy the corrected version.

[Navigation Indicator Fix](IMG/NavigationIndicatorFix.PNG)

---

## 2. Button Mapping on Election Charts

**Issue:**  
On the *Multi-Choice Voting* page, the buttons used to switch between historical election years were not functioning. The view remained stuck on the year 2000 results.

**Fix:**  
Thom updated the server‑side files to ensure the new changes were reflected, allowing the buttons and maps to function properly.

[Button Mapping on Election Charts](IMG/ButtonMappingonElectionChartsFix.PNG)

---

## 3. Data Redundancy and Source Documentation

**Issue:**  
The sample data file (`ApprovalVotingData.py`) contained redundant information.

**Fix:**  
Austin cleaned and reorganized the raw data, removing duplicates and ensuring that all historical election results (1824, 1992, and 2000) were formatted as a nested dictionary structure for easier modular access by the web application.

---

## 4. Broken Link

**Issue:**  
A broken link was discovered in the documentation/explanation section of the site.

**Fix:**  
This was logged as an **Incomplete Task**. The team chose to defer the fix to Sprint 4 to prioritize stability of the core visualization features for the current release.

---

# QA Session: Issues and Fixes Sprint 4

## 1. Last Update Date

**Issue:**

One issue we identified in the last sprint was that the table’s ‘last updated’ information wasn’t displaying correctly on the site.

**Fix:**

Updated the code to display the page’s last‑updated timestamp above the footer for end users.

[Last Update Fix](IMG/LastUpdateFix.PNG)

## 2. ReadMe File

**Issue:**

The README file was missing the Feature Updates from previous sprints and needed a clear definition of the project’s intended purpose.

**Fix:**

We updated the README file to include the website’s mission and the new features introduced in each sprint.

## 3. Testing

The following screenshots show the testing of the Supreme Court Check mapping to verify that all components are functioning correctly. During testing, I did not encounter any issues. Every indicator and toggle operated as expected.

   - [Brown V Board of Education All Toggled](IMG/ButtonBrownVBoardOfEducationAll.PNG)
   - [Brown V Board of Education Override Only](IMG/ButtonBrownVBoardOfEducationOverride.PNG)
   - [Dobbs V Jackson All Toggled](IMG/ButtonDobbsVJacksonAll.PNG)
   - [Dobbs V Jackson Override Only](IMG/ButtonDobbsVJacksonOverride.PNG)
   - [Prigg V Pennsylvania All Toggled](IMG/ButtonPriggVPennsylvaniaAll.PNG)
   - [Prigg V Pennsylvania Override Only](IMG/ButtonPriggVPennsylvaniaOverride.PNG)
   - [Shelby V Holder All Toggled](IMG/ButtonShelbyVHolderAll.PNG)
   - [Shelby V Holder Override Only](IMG/ButtonShelbyVHolderOverride.PNG)

# QA Session: Issues and Fixes Sprint 5

During the QA review, several issues were identified while testing the Collaborative Veto and Wyoming Veto Scenario mappings. Below is a summary of the findings and planned fixes.

- [Collaborative Veto Map Energy Regulation - Only Allow](IMG/collaborativeVetoMapOnlyAllow.PNG)
- [Collaborative Veto Map Energy Regulation - All Toggled](IMG/CollaborativeVetoMapEnergyRegulationAllToggled.PNG)  
- [Collaborative Veto Map Firearm Restriction - Only Allow](IMG/CollaborativeVetoMapFirearmRestrictionOnlyAllow.PNG)
- [Collaborative Veto Map Firearm Restriction - All Toggled](IMG/CollaborativeVetoMapFirearmRestrictionAllToggled.PNG)
- [Collaborative Veto Map Zoning Control - Only Allow](IMG/CollaborativeVetoMapZoningControlOnlyAllow.PNG)
- [Collaborative Veto Map Zoning Control - All Toggled](IMG/CollaborativeVetoMapZoningControlAllToggled.PNG)   


## 1. Collaborative Veto Mapping  Toggle Behavior

**Issue:**  
The following screenshots show the testing of the Collaborative Veto mapping. All toggles were verified to be functioning correctly; however, one issue was identified in the Wyoming mapping system. When deselecting either the **Allow** or **Veto** option, the map removes a county and leaves a blank space. When both options are deselected, the map becomes blank except for the legend and title.

- [Collaborative Veto Map Only Allow](IMG/collaborativeVetoMapOnlyAllow.PNG)  
- [Collaborative Veto Map No Options Selected](IMG/collaborativeVetoMapNoOptionsSelected.PNG)

**Fix:**  
The team will investigate this behavior in the next sprint and implement a proper fix. Since the options still display the correct information, the current version will be committed for now.



## 2. Wyoming Firearm Restriction Veto Scenario Legend Order

**Issue:**  
During testing, the legend options for the **Wyoming Firearm Restriction Veto** scenario were found to be flipped. This does not affect functionality but is noticeable when comparing maps for consistency.

**Fix:**  
This visual inconsistency will be addressed in a future sprint.



## 3. Text Consistency “Above” vs. “Following”

**Issue:**  
The first sentence below the map used the phrase **“the following simulations model”**, which did not match the layout of the page.

**Fix:**  
The text will be updated to read **“The above simulations model…”** to maintain consistency with the map’s placement.


