# Minor Research Project – Predicting CNS Drug Penetration in Glioblastoma

This repository accompanies the **Minor Research Project** conducted by **Jack Pieters** in collaboration with the **Neurosurgery Lab at Erasmus Medical Center** (Prof. Martine Lamfers) and the **Dannis van Vuurden Lab at Prinses Máxima Center**.  
The project evaluated an *in-silico* framework for predicting **brain penetration of oncology drugs** to accelerate **drug repurposing in glioblastoma (GBM)**.

---

## Project Overview
Glioblastoma multiforme (GBM) is the most aggressive primary brain tumor, and effective therapies are limited largely due to the **blood–brain barrier (BBB)**, which restricts drug delivery to the central nervous system (CNS).  

This project tested whether an *in-silico* model — originally developed by **Watanabe et al. (2021)** — can be applied to predict **unbound brain-to-plasma partition coefficients (Kp,uu,brain)** for approved oncology drugs.   
The predictions were combined with known pharmacokinetic data to estimate the concentration of compounds in the brain extracellular matrix (in unbound/active form). Subsequently, the predicted brain concentrations were compared to **in-vitro drug sensitivity data** from patient-derived GBM stem-like cells to rank compounds for potential repurposing.

---

## Repository Contents
| Folder/File | Description |
|--------------|-------------|
| `smiles_generator.py` | Python script that retrieves compound SMILES from PubChem, removes salts, and canonicalizes structures using RDKit. |
| `CNS-MPO.ipynb` | Jupyter notebook calculating **CNS-MPO scores** based on six physicochemical descriptors (MW, TPSA, HBD, clogP, bpKa, logD). |
| `/docs/GBM_Brain_Exposure.html` | Rendered R Markdown report containing the full R analysis, figures, and plots (see live version below). |
| `/docs/GBM_Brain_Exposure_files/` | Associated image and data assets for the HTML report. |

**View the rendered report:**  
[GBM_Brain_Exposure.html](https://jackpieters4.github.io/minor_research_project_BSB/)

---

## Key Analyses
- **Physicochemical profiling** of 75 FDA-approved oncology drugs (Liston & Davis, 2017).  
- **CNS-MPO scoring** to estimate passive BBB permeability.  
- **Kp,uu,brain predictions** via the *DRUMAP* online tool implementing the Watanabe model.  
- **Integration with in-vitro drug sensitivity data** to compute a **Brain Exposure Index (BEI)** combining predicted exposure and efficacy.  
- **Validation against Phase-0 clinical trial data** where measured tumor concentrations were available.  

The full R analysis and figures (e.g., correlation plots, compound ranking, and validation results) are presented in the HTML report above.

---

## Main Findings
- The framework correctly identified **temozolomide** as the known CNS-active GBM drug.  
- **Overestimation** of brain penetration occurred for large, lipophilic, or efflux-transporter substrates.  
- Integrating predicted exposure with *ex-vivo* efficacy data (BEI) highlighted several **promising repurposing candidates**, including **cabazitaxel** and **dactinomycin**.  
- Results emphasize the need for **human-validated physiologically based pharmacokinetic (PBPK) models** to improve translational accuracy.

---

## Methods & Tools
- **Python**: RDKit, PubChemPy, pKaSolver for SMILES generation and descriptor computation.  
- **R / R Markdown**: data visualization and compound ranking.  
- **External tools**: [DRUMAP](https://drumap.nibiohn.go.jp/) for *in-silico* pharmacokinetic parameter prediction.  

---

## Reference
Watanabe R. et al. (2021). *Development of an in-silico prediction model for P-glycoprotein efflux potential in brain capillary endothelial cells toward the prediction of brain penetration.* **Drug Metab. Pharmacokinet.**, 36(5):2725-2738.  

---

*Maintained by Jack Pieters — Bioinformatics & Systems Biology MSc, Vrije Universiteit Amsterdam.*  
*Contact: jackpieters4@gmail.com • [LinkedIn](https://www.linkedin.com/in/jackpieters4)*  


