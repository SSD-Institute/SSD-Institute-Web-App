[Back to README.md](../../README.md)

# SSD Institute Web App

## Project Abstract

### Project Purpose

To create a functional web application with visualizations to clearly convey the institutes beliefs, political suggestions and civic impact.

#### Beliefs 

Creating clear descriptionns with a minimum of 500 words of each concept so that an average person can understand the purpose and potential of the governance concepts.

#### Political Suggestions

Visualizing the potlicical suggestions and concepts via three static Ploty charts for citizen viewing which will be coupled with the concept descriptions mentioned earlier. The fourth "Minimum amount of space" visulization will be a stretch goal with the same general concept of visualization and description.

#### Civic Impact 

In addition to concept descriptions having a seperate portion of each concept and explaining why they could be impactful in the modern landscape. Having a minimum of a 250 word explaination of why these concepts could be civically impactful for the average person.

### Stakeholders

The main project stakeholders are:

1. Business leaders at SSD Institute (Thom Mo & Joe Pek)
2. End-users of the civic public (The American public, and those with an internet access to interact with the site)
3. Collaberators and IT proffesioanls affiliated with SSD Insitute 

Secondary Stakeholders:
1. Hosting partners Python Anywhere 
2. Academic staff at Penn west 
3. Donors
4. Subject matter expert advisors

## User stories

With a total of fifteen user stories, which will be implemented for the general citizen, SSD Institute Staff, and developers, for completion of the minimum viable product.

See [User Stories](UserStories.md)

## Anticipated Completion

### Milestones 

**End of December 2025 - Semeter 1**

* Full founding documentation available on Github (I.e: Concepts, Charter, Scope, FAQ, User Stores, etc)
* A prototype displaying all four potential visualizations and documentation in an example 
* The seeding of the framework (Flask) pushed to the main repository

**End of April 2026**

* Three visualizations for collaberative veto, supreme court check and Multi-voting
* Clear documentation with each visuilzation one portion explaining concept the other impact
* Hosted for the general public to see with SSL, HTTPS connections via Python Anywhere servers
* Updatable in a clear way via Github repo and commits for future SSD Institute affiliates 

This Flask, Gunicorn web application with three Ploty, and optional one D3.js visualizations is planned to be completed on May 1st 2026, deployed for public access via Python Anywhere so citizens can view the GUI interface and documentation.

## Functional Scope Table

### Functional Scope

| Feature / Functionality | Description | Priority | Deliverable Phase |
|--------------------------|--------------|-----------|-------------------|
| **Static Concept Pages** | Written explanations (≥500 words each) of Collaborative Veto, Multi-choice Voting, Supreme Court Veto, and Minimum Space concepts. | Core | MVP |
| **Plotly Visualizations (3)** | Static charts for Collaborative Veto (county/state view), Multi-choice Voting (bar chart), and Supreme Court Veto (choropleth map). | Core | MVP |
| **Documentation Pages** | Clear markdown documentation including FAQ, Concepts, Scope, Charter, User Stories, Getting Started. | Core | MVP |
| **Civic Impact Section** | 250-word civic impact analysis accompanying each governance concept. | Core | MVP |
| **Flask Web Framework Setup** | Functional Flask app hosted on PythonAnywhere with Gunicorn, HTTPS, and GitHub integration. | Core | MVP |
| **Mobile Responsiveness** | CSS styling to ensure public usability on phones/tablets. | Core | MVP |
| **GitHub Version Control** | Active Git repository with issues, milestones, and clear commit messages. | Core | MVP |
| **D3.js Visualization (Minimum Space)** | Land allocation concept visualization (treemap/cartogram) based on population and land data. | Stretch | Phase 2 |
| **Interactive Map Functionality** | Basic click/hover tooltips or toggles for states/counties in Plotly visualizations. | Stretch | Phase 2 |
| **User Feedback Form** | Simple contact form for users to submit feedback or questions. | Stretch | Phase 2 |
| **Automated Updates** | Scripts to refresh data or regenerate charts dynamically. | Stretch | Phase 2 |
| **Expanded Publications Feature** | Blog-like section accessible to Institute staff for updates or papers. | Stretch | Phase 2 |


## Approved Budgets

1. Purchase of a domain up to $50 dollars for visibility purposes 
2. Purchase of a PythonAnywhere entry subscription able to hold 10,000 monthly visitors for $60 annually; for hosting the web application
3. Purchase of a SSL sertificat for HTTPS connections up to $20

## Project Team 

Here is the roles and responsibilities of each member of the initial team

* Justin Maga: Dev, Minute/Note-taker, Backup Business Analyst, Backup Documentation Reviewer
* Austin Pringle: Sr Dev, Business Analyst, Backup Devops
* Stuart Krugger: QA, DevOps, Content Writer, Backup Project Manager
* Thom Mo: Project Manager, Dev, QA backup, DevOps, Documentation Reviewer

## Sign off of Stake holders 

* I Thom J Mondeaux, non profit liason and project manager, Sign off on this Project. 

* We the JAST Team Sign off on this project as Developers.

* I Joe Pek sign off on this project as Non-Profit coordinator.
