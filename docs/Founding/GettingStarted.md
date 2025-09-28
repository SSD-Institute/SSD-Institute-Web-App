[Back to read me](../../README.md)

# Getting Started (Developers)

This project uses **Flask** (Python web framework) and visualization libraries (**Plotly** and **D3.js**) to demonstrate governance and voting concepts.  
Deployment is hosted on **PythonAnywhere**, and development is managed through **GitHub**.

[See Flask app Version 1 SSD]()
## 1. Python & Flask
- Flask Documentation: https://flask.palletsprojects.com/
- Flask is a lightweight Python framework for building web apps.
- Tutorials: [Flask Mega Tutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## 2. Gunicorn (Web Server for Flask)
- Gunicorn Documentation: https://gunicorn.org/
- Gunicorn is a production-ready server for running Flask apps.
- On PythonAnywhere, Flask apps typically run behind Gunicorn by default.

## 3. Plotly (Python-based Visualizations)
- Plotly Documentation: https://plotly.com/python/
- Plotly Express Quickstart: https://plotly.com/python/plotly-express/
- Good for:
  - Choropleth maps of states/counties
  - Interactive bar/line charts
  - Dynamic dashboards

## 4. D3.js (JavaScript Visualizations)
- D3.js Documentation: https://d3js.org/
- Tutorials: https://observablehq.com/@d3/learn-d3
- Good for:
  - Highly customized static/interactive maps
  - State/county polygons (GeoJSON)
  - Advanced transitions/animations

## 5. Mapping Resources
- US States & Counties GeoJSON: https://eric.clst.org/tech/usgeojson/
- Example: Use **Plotly Choropleth** for states/counties or **D3 TopoJSON** for detailed maps.     

## 6. PythonAnywhere (Hosting)
- PythonAnywhere Docs: https://help.pythonanywhere.com/
- Used to host our Flask application online.
- Paid plan at $60 dollars a year is sufficent for MVP
- Domain name will be purchased before Semester 2 $30 max
- SSL Certificate will be purchased at time of domain $30

## 7. Git & GitHub
- Git Basics: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com/
- Git workflow we’ll use:
  - `git clone` to copy the repo
  - `git pull` to sync latest changes
  - `git add`, `git commit`, `git push` for updates
- Our repo will also include:
  - `/docs` folder for documentation
  - `/app` folder for Flask code
          
## Summary
- **Flask + Gunicorn** = Web app core
- **Plotly + D3.js** = Visualizations (state, county, municipality level)
- **PythonAnywhere** = Hosting
- **GitHub** = Version control & team workflow
