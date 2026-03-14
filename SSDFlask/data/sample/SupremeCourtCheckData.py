# ============================================================
# SUPREME COURT CHECK SIMULATION DATA
# Project: Scientific Self Determination
# Visualization: Plotly USA Choropleth
#
# PURPOSE
# Demonstrate how a hypothetical "Supreme Court Check"
# (majority of 26 state legislatures rejecting a SCOTUS ruling)
# might appear if state legislatures voted on the ruling.
#
# States are categorized as:
# 1. Override Decision
# 2. Support Decision
# 3. Mixed / Independent Policy
#
# Legislative control is weighted more heavily than state law
# history when determining likely vote behavior.
#
# Hover text should explain reasoning for each state category.
#
# DATA SOURCES
# Legislative control:
# https://www.ncsl.org/about-state-legislatures
#
# Case summaries:
# https://www.oyez.org/
# https://supreme.justia.com/
#
# Policy divergence data:
# https://www.brennancenter.org/
# https://www.kff.org/
# ============================================================

SupremeCourtCheckData = {

# ============================================================
# CASE 1
# PRIGG v PENNSYLVANIA (1842)
# ============================================================

# WHY THIS CASE
#
# Prigg v Pennsylvania ruled that federal fugitive slave law
# preempted state law, limiting the ability of Northern states
# to interfere with slave catchers retrieving escaped slaves.
#
# Although the Court affirmed federal authority, the decision
# sparked widespread resistance across Northern states.
#
# Many states soon passed "Personal Liberty Laws" designed
# specifically to obstruct enforcement of the Fugitive Slave
# Act by denying state cooperation or adding legal protections
# for alleged fugitives.
#
# In a Supreme Court Check system, legislatures in free states
# would likely have voted to override the ruling in order to
# preserve their authority to regulate enforcement inside
# their borders.
#
# Historical evidence supporting this:
# - Personal Liberty Laws enacted in MA, VT, ME, MI, WI, etc.
# - Northern legislative resistance intensified after 1842
# - Abolitionist political coalitions were already active
#
# SOURCE
# https://www.oyez.org/cases/1789-1850/41us539

"Prigg v Pennsylvania (1842)": {

    # Northern free states and several border states
    # likely vote to override the Supreme Court ruling
    # because they opposed federal enforcement of slavery
    # within their jurisdictions.

    "Override Supreme Court Decision": [
            "ME","NH","VT","MA","RI","CT",
            "NY","NJ","PA",
            "OH","IN","IL","MI",
            "DE","MD",
            "MO","KY"
    ],
    # Southern slaveholding states would strongly support
    # the ruling because it reinforced federal protection
    # of slave property rights and recovery of escaped slaves.

    "Support Supreme Court Decision": [
            "VA","NC","SC","GA",
            "AL","MS","LA",
            "AR","TN"
    ],

    # States with mixed political environments or frontier
    # populations that might not have taken a unified stance.

     "Mixed / Independent Policy": [],

    # Not states as of this case.
    "Not a State Yet": [
            "FL","TX","IA","WI","CA","MN","OR",
            "KS","WV","NV","NE","CO","ND","SD","MT","WA","ID","UT","AZ","NM","OK",
            "AK","HI"
        ]
},

# ============================================================
# CASE 2
# BROWN v BOARD OF EDUCATION (1954)
# ============================================================

# WHY THIS CASE
#
# Brown v Board is one of the most consequential Supreme Court
# rulings in U.S. history.
#
# It declared racial segregation in public schools unconstitutional.
#
# However, many state governments—particularly in the Deep South—
# strongly resisted implementation.
#
# This produced a clear federalism conflict where several states
# openly defied the Court.
#
# This makes it an ideal case to model how a democratic
# "Supreme Court Check" might have functioned.

# PRIMARY SOURCE
# https://www.oyez.org/cases/1940-1955/347us483

# HISTORICAL CONTEXT
#
# The Southern Manifesto (1956) was signed by over 100
# members of Congress opposing Brown.
#
# Several states enacted laws attempting to avoid integration
# including school closures and segregation academies.

# SIMULATION METHOD
#
# Southern legislatures modeled as "Override".
# Northern legislatures modeled as "Support".
# Border states modeled as "Mixed".

"Brown v Board of Education (1954)": {

    "Override Supreme Court Decision": [
        "AL","MS","LA","SC","GA","AR","VA"
    ],

    "Support Supreme Court Decision": [
        "CA","NY","MA","IL","WA","OR","MN","WI","NJ","VT","ME"
    ],

    "Mixed / Independent Policy": [
        "TX","FL","TN","NC","KY","MO","OK","AZ","NM","CO","PA",
        "MI","OH","IN","IA","KS","NE","ND","SD","WY","MT","ID",
        "UT","NV","NH","RI","DE","MD","CT","WV"
    ],

    "Not a State Yet": [
        "AK","HI"
    ]
},

# ============================================================
# CASE 3
# SHELBY COUNTY v HOLDER (2013)
# ============================================================

# WHY THIS CASE
#
# Shelby County invalidated the Voting Rights Act's
# preclearance coverage formula.
#
# This removed federal oversight for voting-law changes
# in states with histories of discrimination.
#
# The ruling immediately triggered new voting legislation
# across several states.

# PRIMARY SOURCE
# https://www.oyez.org/cases/2012/12-96

# POLICY DIVERGENCE
#
# Within hours of the ruling:
#
# Texas implemented strict voter ID laws
# North Carolina passed H.B. 589
#
# Meanwhile other states expanded voting access.

# SIMULATION METHOD
#
# Legislatures favoring stronger federal oversight
# are modeled as "Support".
#
# Legislatures emphasizing state autonomy
# are modeled as "Override".

"Shelby County v Holder (2013)": {

   "Override Supreme Court Decision": [
        "TX","AL","MS","LA","GA","SC","NC","TN","OK","AZ","FL"
    ],

   "Support Supreme Court Decision": [
        "CA","NY","MA","WA","OR","VT","NJ","RI","CT","IL","CO","NM"
    ],

    "Mixed / Independent Policy": [
        "PA","MI","WI","MN","IA","KS","MO","IN","OH","KY","WV",
        "AR","NV","UT","ID","MT","WY","ND","SD","NE","AK","HI",
        "ME","NH","DE","MD","VA"
    ]
},

# ============================================================
# CASE 4
# DOBBS v JACKSON WOMENS HEALTH ORGANIZATION (2022)
# ============================================================

# WHY THIS CASE
#
# Dobbs overturned Roe v Wade and returned abortion policy
# authority entirely to the states.
#
# This created one of the clearest modern examples of
# state-level policy divergence.

# PRIMARY SOURCE
# https://www.oyez.org/cases/2021/19-1392

# POLICY DIVERGENCE
#
# Several states enacted trigger bans immediately.
# Others passed constitutional protections.

# SIMULATION METHOD
#
# States with conservative legislative control
# and pre-existing abortion restrictions are modeled
# as supporting the decision (no override).
#
# States with liberal legislatures and abortion
# protections are modeled as likely to vote to override.

"Dobbs v Jackson Womens Health Organization (2022)": {

    "Override Supreme Court Decision": [
        "CA","OR","WA","NV","CO","NM","IL","NY","NJ","MA","VT","ME"
    ],

    "Support Supreme Court Decision": [
        "TX","OK","LA","MS","AL","TN","KY","AR","MO","ID","WY","ND","SD"
    ],

    "Mixed / Independent Policy": [
        "FL","GA","NC","SC","VA","PA","MI","WI","MN","IA","KS","NE",
        "MT","AZ","UT","NH","DE","MD","AK","HI","RI","CT","IN","OH","WV"
    ]
}

}

color_discrete_map={
    "Override Supreme Court Decision": "red",
    "Support Supreme Court Decision": "blue",
    "Mixed / Independent Policy": "lightgray",
    "Not a State Yet": "white"  # or "#f0f0f0" for subtle gray-out
}