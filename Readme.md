# Towards a pre-surgery clinical decision support system


This repository contains the replication materials for the paper **"Towards a pre-surgery clinical decision support 
system"**, which investigates the temporal and causal structure of clinical and physiological variables during  
propofol-induced general anesthesia. The work has the objective to create a lightweight model of the heart rate 
under anaesthetic administration. The model is developed according to the Bayesian Network formalism. The analysis 
is based on data provided by the PhysioNet repository
🔗 [Propofol Anesthesia Dynamics Dataset (v1.0)](https://physionet.org/content/propofol-anesthesia-dynamics/1.0/), 
consisting of a pre-processing step and a model building phase.
---

## 📦 Table of Contents

- [Overview](#overview)  
- [Installation](#installation)  
- [Dataset](#dataset)  
- [Running the Code](#running-the-code)  
- [Results](#results)  
- [Reproducibility](#reproducibility)  
- [License](#license)  
- [Contact](#contact)

---

## 🧠 Overview

This replication package includes:

- Scripts for preprocessing the Propofol Anesthesia Dynamics dataset  
- Implementation of Bayesian network modeling and inference  
- Code to reproduce key figures from the paper
---

## ⚙️ Installation
Clone this repository and install the required dependencies:

```bash
git clone https://github.com/your-username/propofol-anesthesia-replication.git
cd propofol-anesthesia-replication
pip install -r requirements.txt
```

## 📁 Dataset

This project uses the **Propofol Anesthesia Dynamics** dataset, available on PhysioNet.

### 🔽 Download Instructions

You must manually download the dataset from:

➡️ [https://physionet.org/content/propofol-anesthesia-dynamics/1.0/](https://physionet.org/content/propofol-anesthesia-dynamics/1.0/)

In particular, for a perfect reproduction of the content of the paper, replicate the following lines:

```bash
wget -r -N -c -np https://physionet.org/files/propofol-anesthesia-dynamics/1.0/
mv physionet.org/files/propofol-anesthesia-dynamics/1.0/Data/ ./data
rm -rf physionet.org/
```

## ▶️ Running the Code

To replicate the results, run:

```bash
python run_analysis.py

python run_analysis.py --config configs/default.yaml



Let me know if you want to include figures, add argument explanations, or link to a published paper!
