elections = {

    # SOURCE DATA DOCUMENTATION
    # Project: Approval Voting Historical Simulations
    # Purpose: Document official election data sources and explain modeled approval estimates.

    # This file contains:
    # 1. Official plurality vote totals (primary data).
    # 2. Documentation of simulated approval vote assumptions.
    # 3. Direct links to authoritative primary sources.
    #


    # ============================================================
    # 2000 UNITED STATES PRESIDENTIAL ELECTION
    # ============================================================

    # WHY THIS DATA:
    # The 2000 election is widely cited as a classic spoiler-effect case.
    # It is used to model how approval voting could reduce vote-splitting.

    # PRIMARY OFFICIAL SOURCE (Plurality Data):
    # Federal Election Commission (FEC) Official Results
    # TODO: BROKEN LINK
    # https://www.fec.gov/resources/cms-content/documents/2000presgeresults.pdf

    # National Archives Electoral College Records
    # https://www.archives.gov/electoral-college/2000

    # APPROVAL ESTIMATES:
    # Simulated approval totals are modeled using political science literature
    # indicating that a majority of Ralph Nader voters preferred Al Gore over
    # George W. Bush in two-way preference polling.

    # These approval totals are hypothetical and designed for structural modeling,
    # not historical claim-making.

    "2000 United States Presidential Election": {
        "2000 Election, Actual Results": {
            "George W. Bush": 50456002, 
            "Al Gore": 50999897,
            "Ralph Nader": 2882955
        },

        "2000 Election, Simulated Results with Approval Voting": {
            "George W. Bush": 52000000,
            "Al Gore": 54500000,
            "Ralph Nader": 3200000
        }
    },


    # ============================================================
    # 1992 UNITED STATES PRESIDENTIAL ELECTION
    # ============================================================
   
    # WHY THIS DATA:
    # The 1992 election featured a historically strong third-party candidate
    # (Ross Perot). It is used to model coalition breadth under approval voting.

    # PRIMARY OFFICIAL SOURCE (Plurality Data):
    # Federal Election Commission (FEC) Official Results
    # https://www.fec.gov/resources/cms-content/documents/1992presgeresults.pdf

    # National Archives Electoral College Records
    # https://www.archives.gov/electoral-college/1992

    # APPROVAL ESTIMATES:
    # Simulated approval totals are based on political science research showing
    # Perot voters were ideologically mixed, with many preferring Bush over Clinton
    # in head-to-head matchups.

    # These numbers represent modeled cross-approval behavior and are not
    # historical vote totals.

    "1992 United States Presidential Election": {
        "1992 Election, Actual Results": {
            "Bill Clinton": 44909889,
            "George H. W. Bush": 39104550,
            "Ross Perot": 19743821
        },

        "1992 Election, Simulated Results with Approval Voting": {
            "Bill Clinton": 48000000,
            "George H. W. Bush": 50500000,
            "Ross Perot": 21000000
        }
    },


    # ============================================================
    # 1824 UNITED STATES PRESIDENTIAL ELECTION
    # ============================================================

    # WHY THIS DATA:
    # The 1824 election resulted in a contingent election decided by the House
    # of Representatives. It is used to model how approval voting might reduce
    # institutional legitimacy crises.

    # PRIMARY OFFICIAL SOURCE (Plurality Data):
    # National Archives Electoral College Records
    # https://www.archives.gov/electoral-college/1824

    # Historical vote totals compiled from:
    # U.S. House of Representatives Historical Office
    # https://history.house.gov/

    # APPROVAL ESTIMATES:
    # Simulated approval totals are modeled based on documented ideological
    # alignment (e.g., Clay voters likely approving Adams).

    # Because national popular vote data in 1824 was incomplete and varied
    # by state suffrage rules, approval totals are modeled for structural
    # demonstration purposes only.

    "1824 United States Presidential Election": {
        "1824 Election, Actual Results": {
            "Andrew Jackson": 151271,
            "John Quincy Adams": 113122,
            "William H. Crawford": 40856,
            "Henry Clay": 47531
        },

        "1824 Election, Simulated Results with Approval Voting": {
            "Andrew Jackson": 160000,
            "John Quincy Adams": 175000,
            "William H. Crawford": 60000,
            "Henry Clay": 65000
        }
    }
}


# ============================================================
# APPROVAL VOTING THEORY SOURCES
# ============================================================

"""
WHY THIS DATA:
Approval voting simulations are grounded in established political science
and mathematical voting theory.

PRIMARY ACADEMIC SOURCES:

Brams, Steven J., and Peter C. Fishburn (1983).
Approval Voting.
Cambridge University Press.

American Political Science Review (1978).
Brams & Fishburn — Approval Voting.

Election Science (modern research and implementation data)
https://electionscience.org/

These sources establish the theoretical basis for modeling coalition
acceptability rather than single-preference plurality.
"""