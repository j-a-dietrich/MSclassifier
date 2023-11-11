# MSclassifier
MSclassifier is a program for analyzing the chemical classification of metabolites based on the accurate mass of the MS1 peak.
</br>
It is based on the assumption that large molecules do not exhaust the combinatorial possibilities of structures, but are rather constrained and produced from similar frameworks and origins.
</br>
**This feasibility study incorporates the following functionalities:**
</br>
- MSbuddy, to find the molecular formula through accurate mass.
- Finding all structures with a given molecular formula from the COCONUT database (which must be installed as a MongoDB dump).
- Using NPclassifier and Classyfire to predict/calculate the chemical class.
- Plotting the distribution of different classes for a given molecular formula.
- (Structures can be visualized with RDKit).

**To-Do List:**
</br>
- [ ] Incorporate retention time (for model training). 
- [ ] Use PubChem instead of COCONUT.
- [ ]  Utilize LLM to predict high NP-score structures from chemical formulas.
- [ ]  Accept MS1 as input.