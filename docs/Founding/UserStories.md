[Back to README.md](../../README.md)

# User Stories

User stories provide valuable feedback on how the intended users of the software will actually interact with it, as well as what features they need or expect to see. We have identified 3 core user groups that will be interacting with the finished project: the general public, the non-profit volunteers/staff that will have to administer the final software, and the core development team.

## General Public

- As a citizen, I want to visit the site and read clear, updated definitions of governance models so that I understand concepts like “collaborative veto”, “multiple choice voting”, and “supreme court veto”.  
- As a citizen, I want to view a Plotly bar chart showing candidate approval totals under multiple choice voting so that I can compare how many citizens support each candidate.  
- As a citizen, I want to see a US state-level choropleth map with states proportionally colored based on whether 26 or more object to a supreme court veto, so that I can visually see if the veto threshold is met.  
- As a citizen, I want to see a county-level map for West Virginia showing which counties would veto a state law, so I can understand local regional variation.  
- As a citizen accessing the site, I want to be sure that the site is secure, and uses the most up-to-date security features.

## Non-Profit / Admin

- As a non-profit admin, I want the documentation content to be reorganized and rewritten with updated examples so that educational materials are clearer and more engaging.  
- As a non-profit admin, I want the site to load quickly and host these visualizations statically so that users with moderate connections see them without slowdown.
- As a non-profit admin, I would like application deployment to be as seamless as possible. I would benefit from using a simple platform like PythonAnywhere.
- As a non-profit admin, I want the website to be memorable and easily accessible, so we should have a domain name instead of using the PythonAnywhere default.

## Developers

- As a developer, I want the repository to include sample GeoJSON or shapefile data for states and counties so that I can build and test visualizations without hunting for data.  
- As a developer, I want new visualization code to be modular (e.g. each viz in its own file or module) so that it's easier to maintain and potentially reuse.  
- As a developer, I want clear documentation in the docs folder that explains how to run the Flask app, add new visualizations, and update data so that future contributors can work confidently. 
- As a developer, I want to maintain a clean separation of concerns, with a modern frontend/backend archetecure.