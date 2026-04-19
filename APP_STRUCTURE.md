# SSD Institute Web App - Final Structure Document

## Project Overview
The SSD Institute Web App is a Flask-based single-page application that implements multiple voting system visualizations and comparative analysis tools for education-related electoral cases.

---

## 📁 Root Level

```
SSD-Institute-Web-App/
├── LICENSE                          # Project licensing
├── README.md                        # Project overview and documentation
├── .gitignore                       # Git ignore rules
├── .github/
│   └── workflows/
│       ├── deploy.yml              # CI/CD deployment workflow
│       └── test.yml                # Automated testing workflow
├── SSDFlask/                        # Main application directory
└── docs/                            # Documentation directory
```

---

## 🎯 Application Structure (`SSDFlask/`)

### Core Application

```
SSDFlask/
├── application.py                  # Main Flask application entry point
│
├── static/                          # Static assets (served directly)
│   ├── assets/                     # Images and icons
│   │   ├── GithubImage.png
│   │   ├── home_page_image.png
│   │   ├── accessibilityOptions.png
│   │   └── [social media SVGs]     # Facebook, Twitter, LinkedIn, etc.
│   │
│   ├── scripts/                    # Client-side JavaScript
│   │   ├── ApprovalVotingSwitcher.js
│   │   ├── CollaborativeVetoSwitcher.js
│   │   ├── SupremeCourtVetoSwitcher.js
│   │   └── accessibility.js        # Accessibility feature controls
│   │
│   └── styles/                     # CSS stylesheets
│       ├── styles.css              # Global styles
│       ├── home.css
│       ├── collaborative_veto.css
│       ├── multiple_choice_voting.css
│       ├── supreme_court_check.css
│       ├── contact.css
│       ├── accessibility.css
│       └── font-faces/
│           └── inter-variable/     # Custom font files
│               ├── inter-variable.css
│               └── inter-variable.woff2
│
├── templates/                      # Jinja2 HTML templates
│   ├── base.html                  # Base template (inherited by others)
│   ├── home.html                  # Landing page
│   ├── collaborative-veto.html    # Collaborative Veto voting system
│   ├── multiple-choice-voting.html # Multiple Choice voting system
│   ├── supreme-court-check.html   # Supreme Court Check voting system
│   ├── minimum-space.html         # Minimum Space voting system
│   └── contact.html               # Contact page
```

### Testing

```
test_app/                           # Test suite directory
├── app.py                          # Test application instance
├── conftest.py                     # Pytest configuration
├── requirements.txt                # Test dependencies
│
├── tests/
│   ├── test_routes.py             # Route/endpoint tests
│   └── test_logic.py              # Business logic tests
│
├── utils/
│   ├── data_utils.py              # Data processing utilities
│   └── __init__.py
│
└── data/
    └── election_data.csv          # Sample election data for testing
```

### Visualization & Data

```
visualization_scripts/              # Data visualization and analysis tools
├── cv_viz.py                       # Collaborative Veto visualization
├── mcv_viz.py                      # Multiple Choice Voting visualization
├── scv_viz.py                      # Supreme Court Check visualization
├── wy_county_viz.py                # Wyoming county-level visualization
│
├── data/
│   ├── raw/                        # Raw data sources (.gitkeep)
│   ├── processed/                  # Processed data outputs (.gitkeep)
│   │
│   ├── sample/                     # Sample datasets
│   │   ├── ApprovalVotingData.py
│   │   ├── CollabVetoData.py
│   │   ├── SupremeCourtCheckData.py
│   │   ├── WYCountyData.py
│   │   └── Site_Research/
│   │
│   └── wy_counties.geojson        # Wyoming county geographic boundaries
│
└── tests/
    ├── app.py
    ├── test_app.py
    ├── test_wy_county.py
    └── wy_county_app.py
```

---


