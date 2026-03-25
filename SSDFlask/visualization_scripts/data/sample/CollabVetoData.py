"""
Project: Collaborative Veto (County-Level Override Simulation)
Scope: Wyoming Counties

DESCRIPTION:
This dataset models a “Collaborative Veto” system in which counties
can collectively reject (veto) state-level legislation.

- Each county casts a binary vote:
    1 = Veto state law
    0 = Allow state law

- A simple majority (12 out of 23 counties in Wyoming) determines outcome.

This file contains:
1. County metadata (FIPS codes)
2. Three policy scenarios
3. Modeled county-level votes
4. Source-backed explanations

IMPORTANT:
This is a STRUCTURAL and ANALYTICAL dataset.
It is not a record of real votes, but a model grounded in
economic, legal, and demographic research.

------------------------------------------------------------
GEOJSON (NO DOWNLOAD REQUIRED)
------------------------------------------------------------

Use Plotly-compatible GeoJSON (recommended for development):

https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json

Instructions:
- Filter counties where STATE == "56" (Wyoming)
- Match with FIPS codes provided below

Download only if needed for production stability.
"""

# ============================================================
# WYOMING COUNTY METADATA (FIPS)
# ============================================================

WYOMING_COUNTIES = {
    "56001": "Albany",
    "56003": "Big Horn",
    "56005": "Campbell",
    "56007": "Carbon",
    "56009": "Converse",
    "56011": "Crook",
    "56013": "Fremont",
    "56015": "Goshen",
    "56017": "Hot Springs",
    "56019": "Johnson",
    "56021": "Laramie",
    "56023": "Lincoln",
    "56025": "Natrona",
    "56027": "Niobrara",
    "56029": "Park",
    "56031": "Platte",
    "56033": "Sheridan",
    "56035": "Sublette",
    "56037": "Sweetwater",
    "56039": "Teton",
    "56041": "Uinta",
    "56043": "Washakie",
    "56045": "Weston"
}

# ============================================================
# SCENARIO 1: ENERGY REGULATION VETO
# ============================================================

"""
WHY THIS SCENARIO:
Wyoming is one of the most energy-dependent states in the U.S.,
with coal, oil, and natural gas forming a major portion of its economy.

SOURCE CONTEXT:
U.S. Energy Information Administration (EIA)
https://www.eia.gov/state/?sid=WY

Wyoming Energy Authority
https://wyoenergy.org/

RATIONALE:
Energy-producing counties are likely to veto restrictive regulation.
Tourism/education-based counties are less dependent and less likely to veto.
"""

energy_regulation_veto = {
    # Non-veto (less energy dependent)
    "56039": 0,  # Teton (tourism economy)
    "56001": 0,  # Albany (university influence)

    # Veto (energy-dependent / rural counties)
    **{fips: 1 for fips in WYOMING_COUNTIES if fips not in ["56039", "56001"]}
}

# ============================================================
# SCENARIO 2: FIREARM RESTRICTION VETO
# ============================================================

"""
WHY THIS SCENARIO:
Wyoming consistently ranks among the most permissive firearm law states.
Gun ownership and Second Amendment support are culturally and politically strong.

SOURCE CONTEXT:
RAND State Firearm Law Database
https://www.rand.org/research/gun-policy.html

Wyoming Legislative Records
https://wyoleg.gov/

RATIONALE:
Rural counties overwhelmingly oppose firearm restrictions.
Only Teton County (more urbanized/demographically moderate) may not veto.
"""

firearm_restriction_veto = {
    fips: (0 if fips == "56039" else 1)
    for fips in WYOMING_COUNTIES
}

# ============================================================
# SCENARIO 3: STATE LAND-USE / ZONING CONTROL VETO
# ============================================================

"""
WHY THIS SCENARIO:
Western states historically favor local control over land use.
Statewide zoning mandates often face resistance from rural counties.

SOURCE CONTEXT:
Wyoming Countys
https://en.wikipedia.org/wiki/List_of_counties_in_Wyoming

Land Use Policy Research (Lincoln Institute of Land Policy)
https://www.lincolninst.edu/

RATIONALE:
Urban / high-growth counties may support zoning
Rural counties resist centralized land-use authority
"""

zoning_control_veto = {
    # Allow state law (urban / regulated counties)
    "56039": 0,  # Teton
    "56021": 0,  # Laramie
    "56025": 0,  # Natrona
    "56001": 0,  # Albany

    # Veto (rural counties)
    **{fips: 1 for fips in WYOMING_COUNTIES if fips not in ["56039", "56021", "56025", "56001"]}
}

# ============================================================
# MASTER DATA STRUCTURE
# ============================================================

collaborative_veto_scenarios = {
    "Wyoming Energy Regulation Veto Scenario": energy_regulation_veto,
    "Wyoming Firearm Restriction Veto Scenario": firearm_restriction_veto,
    "Wyoming Zoning Control Veto Scenario": zoning_control_veto
}


# ============================================================
# NOTES FOR FUTURE VISUALIZATION (DO NOT IMPLEMENT HERE)
# ============================================================

"""
Visualization Tools (to be used later, not in this file):

- Plotly Choropleth Map
    * plotly.express.choropleth
    * Requires:
        - County FIPS codes (already provided)
        - GeoJSON (external link above)
        - Color mapping (0 = allow, 1 = veto)

- Flask Integration
    * Similar to MCV visualization switching
    * Render pre-generated HTML or dynamic Plotly output

- Optional Enhancements:
    * Hover text showing county name + vote
    * Legend: Veto vs Allow
    * Threshold indicator (12 counties)

This file is intentionally data-only for modular architecture.
"""