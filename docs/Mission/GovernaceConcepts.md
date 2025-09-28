[Back to Readme](../../README.md)

# Governance Concepts

## Introduction

The Scientific Self-Determination project introduces governance concepts designed to give communities more direct influence their governments. These models emphasize local choice, citizen participation, and the principle that individuals should have an inalienable place in their government and society.

The following sections explain the core concepts behind our project and how they will be visualized for public understanding.

---

## 1. Collaborative Veto

**Definition**
The collaborative veto is the idea that local communities can override a higher authority’s decision if a significant minority disagrees.

**How It Works**

* If a state passes a law (e.g., banning alcohol), then **one-third of counties** can say “No,” shifting the decision to the county level.
* Within a county, if one-third of municipalities object, the decision moves further down to municipalities.
* This creates a cascading veto, empowering smaller units of government to self-determine policies.

**Why It Matters**

* Leads to more local decision-making.
* Increases participation in local elections, since municipal and county governance would have more impact.
* Makes governance more adaptable and closer to the people.

**Visualization Plan**

* **Static Example:** Map of Wyoming showing counties that “veto” a state law, and municipalities within a county that push decisions further down.
* **Future Simulation (GIS):** Interactive map where users toggle counties/municipalities to see how veto thresholds shift decision-making.

## 2. Multi-choice Voting

**Definition**
Multi-choice voting allows citizens to vote for as many candidates as they support, rather than being restricted to just one.

**How It Works**

* If five candidates are running, a voter can vote for any number of them (but only once per candidate).
* The winner is still the candidate with the most votes overall.
* This system prevents “spoiler effects” and allows citizens to express broader preferences.

**Why It Matters**

* Expands voter choice and reduces pressure to vote strategically.
* Encourages participation from smaller parties and independent candidates.
* More accurately reflects citizen preferences.

**Visualization Plan**

* **Static Example:** Bar chart showing total votes each candidate received, with clear explanation of why one candidate won.
* **Future Simulation:** Interactive tool allowing a user to allocate their votes and see how the results shift.

## 3. Supreme Court Veto

**Definition**
A collective check on the Supreme Court, where states can veto a ruling if a majority object.

**How It Works**

* If **26 or more states** (simple majority) reject a Supreme Court decision, it no longer applies nationwide.
* Each state may then decide how to handle the issue — follow the Supreme Court ruling or set its own policy.

**Why It Matters**

* Introduces a democratic check on a powerful branch of government.
* Gives states more autonomy while allowing diversity in governance.
* Encourages state governments to be more accountable to their citizens.

**Visualization Plan**

* **Static Example:** U.S. map showing states voting “Yea” or “Nay” on a hypothetical or real Supreme Court case (e.g., alcohol regulation).
* **Future Simulation:** Interactive map showing the threshold counter (once 26 states object, a “Veto Achieved” indicator appears).


## 4. Minimum Amount of Space

**Definition**
Every citizen is guaranteed a permanent minimum space of land, ensuring a basic right to exist and live independently.

**How It Works**

* A person’s allocation = **(average height × 3)²** square feet.
* Those who already own land designate a portion of their property as their minimum space (untaxed, inalienable).
* Those without land receive their allocation from federal reserves (e.g., BLM land).
* The land cannot be sold, seized, or taxed — it remains the citizen’s forever.

**Why It Matters**

* Replaces welfare programs with a universal, tangible right to land.
* Ensures all citizens have a guaranteed space of their own.
* Encourages independence, stability, and fairness.

**Visualization Plan**

* **Static Example:** Calculation showing Wyoming’s population and their collective land allocations, compared to available land.
* **Future Simulation (D3.js):** Treemap or cartogram illustrating how land is divided among citizens, with toggles for state/federal/private land assumptions.

## Conclusion

These four concepts together form the foundation of the Scientific Self-Determination project. By making them understandable through clear explanations, static visualizations, and future interactive simulations, the project aims to inspire greater citizen participation in governance and spark discussion about alternative democratic models.