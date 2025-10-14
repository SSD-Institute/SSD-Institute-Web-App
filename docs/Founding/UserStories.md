[Back to README.md](../../README.md)

# User Stories

User stories provide valuable feedback on how the intended users of the software will actually interact with it, as well as what features they need or expect to see. We have identified 3 core user groups that will be interacting with the finished project: the general public, the non-profit volunteers/staff that will have to administer the final software, and the core development team.

## General Public

- As a citizen, I want to visit the site and read clear, updated definitions of governance models so that I understand concepts like “collaborative veto,” “multiple choice voting,” and “supreme court veto.” The pages should be dated so that I can determine their recency, be reviewed for accuracy, and displayed in a legible and accessible format. **(Priority: High)**

- As a citizen, I want to view a Plotly bar chart showing candidate approval totals under multiple choice voting so that I can compare how many citizens support each candidate. To be acceptable, the visualization should load quickly (> 3s) and be clearly labelled and legible **(Priority: High)**

- As a citizen, I want to see a US state-level choropleth map with states proportionally colored based on whether 26 or more object to a supreme court veto, so that I can visually see if the veto threshold is met. The map must have a legend that is visible and descriptive, the data sources used must be clearly cited; and hover text must include exact counts. **(Priority: High)**

- As a citizen, I want to see a county-level map for West Virginia showing which counties would veto a state law, so I can understand local regional variation. The map should support all of the expected features of a modern embedded map and comply with all applicable accessibility features. **(Priority: High)**

- As a citizen accessing the site, I want to be sure that the site is secure, and uses the most up-to-date security features. It should implement HTTPS, for instance. **(Priority: High)**

- As a citizen, I want to search by term so I can find relevant governance model definitions quickly. Search returns results within 2 seconds and highlights matched terms. **(Priority: Medium)**

## Non-Profit / Admin

- As a non-profit admin, I want the documentation content to be organized and written with updated and timely examples so that educational materials are clearer and more engaging. Documentation should include visuals, clear headings, and be version-controlled. **(Priority: High)**

- As a non-profit admin, I want the site to load quickly and host these visualizations statically so that users with moderate connections see them without slowdown. Pages should load in under 3 seconds, even for users on slower (eg 3G) connections. **(Priority: Low)**

- As a non-profit admin, I would like application deployment to be as seamless as possible. I would benefit from using a simple platform like PythonAnywhere. Deployment steps should be documented, with the PythonAnywhere configuration tested and reproducible. **(Priority: Medium)**

- As a non-profit admin, I want the website to be memorable and easily accessible, so we should have a domain name instead of using the PythonAnywhere default. **(Priority: Medium)**

- As a non-profit admin, I want to log into an admin dashboard to edit definitions and upload new datasets so that content can be managed without developer assistance. Admin interface includes add/edit/delete functions with confirmation dialogs. **(Priority: Low)**

## Developers

- As a developer, I want the repository to include sample GeoJSON or shapefile data for states and counties so that I can build and test visualizations without hunting for data. Example data could be stored in `/data/sample/`, with the README specifying data ownership and provenance. **(Priority: High)**

- As a developer, I want new visualization code to be modular (e.g. each viz in its own file or module) so that it’s easier to maintain and potentially reuse. To satisfy this, each visualization must run independently without relying on each other. If there is shared functionality, it is to be placed in a shared module. **(Priority: Medium)**

- As a developer, I want clear documentation in the docs folder that explains how to run the Flask app, add new visualizations, and update data so that future contributors can work confidently. README includes setup steps; internal documentation passes link checks. **(Priority: Low)**

- As a developer, I want to maintain a clean separation of concerns, with a modern frontend/backend architecture. No direct database logic in views; frontend uses our own internal API only. **(Priority: Medium)**

- As a developer, I want tests for each visualization so that future changes don’t break functionality. Tests should cover 80% of visualization modules; and run automatically in GitHub CI. **(Priority: Low)**