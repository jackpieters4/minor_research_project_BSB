# minor_research_project_BSB

This repository holds the code for the Minor Research Project by Jack Pieters in collaboration with the Neurosurgery lab at Erasmus Medical Center in Rotterdam (led by Dr. Martine Lamfers) and the Dannis van Vuurden lab at Prinses Maxima Center in Utrecht. 

The smiles_generator.py script takes a .txt file with a list of compound names and retrieves the SMILES format from PubChem, strips it of salts and canonicalizes it. The output is a tab-separated file that can be used as input for the CNS-MPO notebook.

The CNS-MPO notebook is a custom python notebook that takes a tab-separated file with two columns: one column with SMILES strings and one with compound names. The notebook predicts the six physicochemical descriptors using RDKit and pKasolver and subsquently calculates the CNS-MPO score according to the original formulation by Wager et al. (2010). 

References: 
Wager, T. T., Hou, X., Verhoest, P. R., & Villalobos, A. (2010). Moving beyond rules: the development of a central nervous system multiparameter optimization (CNS MPO) approach to enable alignment of druglike properties. ACS chemical neuroscience, 1(6), 435–449. https://doi.org/10.1021/cn100008c
