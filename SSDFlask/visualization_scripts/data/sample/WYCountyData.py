# Wyoming County Land Classification Data
# Source: U.S. Bureau of Land Management (BLM), USDA Forest Service, Wyoming State Land Office
# Purpose: Demonstrate Minimum Space land theory at the county level in Wyoming
# FIPS codes follow U.S. Census Bureau state-county format (Wyoming state FIPS: 56)

WYCountyData = {

   # ============================================================
   # SCENARIO A: CURRENT LAND ADMINISTRATION (2020)
   # ============================================================
   # Reflects approximate dominant land administrator by county area.
   # Primary Source: BLM Wyoming State Office Public Land Statistics (2020)
   # https://www.blm.gov/sites/default/files/docs/2021-07/WY_Public_Land_Stats_2020.pdf

   "Current Land Administration (2020)": {
      "56001": "Mixed Use",                 # Albany
      "56003": "Federal Dominant",          # Big Horn
      "56005": "Private Dominant",          # Campbell
      "56007": "Federal Dominant",          # Carbon
      "56009": "Private Dominant",          # Converse
      "56011": "Private Dominant",          # Crook
      "56013": "Federal Dominant",          # Fremont
      "56015": "Private Dominant",          # Goshen
      "56017": "Federal Dominant",          # Hot Springs
      "56019": "Federal Dominant",          # Johnson
      "56021": "Mixed Use",                 # Laramie
      "56023": "Federal Dominant",          # Lincoln
      "56025": "Mixed Use",                 # Natrona
      "56027": "Private Dominant",          # Niobrara
      "56029": "Federal Dominant",          # Park
      "56031": "Private Dominant",          # Platte
      "56033": "Mixed Use",                 # Sheridan
      "56035": "Federal Dominant",          # Sublette
      "56037": "Federal Dominant",          # Sweetwater
      "56039": "Federal Dominant",          # Teton
      "56041": "Mixed Use",                 # Uinta
      "56043": "Mixed Use",                 # Washakie
      "56045": "Private Dominant"           # Weston
   },

   # ============================================================
   # SCENARIO B: PROPOSED MINIMUM SPACE REALLOCATION
   # ============================================================
   # Models a hypothetical Georgist reallocation shifting excess federal
   # holdings to State Trust Land administration for local use.
   # National Parks (Park, Teton) remain federally protected.
   # Based on Minimum Space Theory as described in project documentation.

   "Proposed Minimum Space Reallocation": {
      "56001": "State Trust Land Dominant",  # Albany
      "56003": "Mixed Use",                  # Big Horn
      "56005": "Private Dominant",           # Campbell
      "56007": "Mixed Use",                  # Carbon
      "56009": "Private Dominant",           # Converse
      "56011": "Private Dominant",           # Crook
      "56013": "State Trust Land Dominant",  # Fremont
      "56015": "Private Dominant",           # Goshen
      "56017": "Mixed Use",                  # Hot Springs
      "56019": "Mixed Use",                  # Johnson
      "56021": "State Trust Land Dominant",  # Laramie
      "56023": "Mixed Use",                  # Lincoln
      "56025": "State Trust Land Dominant",  # Natrona
      "56027": "Private Dominant",           # Niobrara
      "56029": "Federal Dominant",           # Park (Yellowstone preserved)
      "56031": "Private Dominant",           # Platte
      "56033": "State Trust Land Dominant",  # Sheridan
      "56035": "Mixed Use",                  # Sublette
      "56037": "State Trust Land Dominant",  # Sweetwater
      "56039": "Federal Dominant",           # Teton (Grand Teton preserved)
      "56041": "Mixed Use",                  # Uinta
      "56043": "State Trust Land Dominant",  # Washakie
      "56045": "Private Dominant"            # Weston
   }
}
