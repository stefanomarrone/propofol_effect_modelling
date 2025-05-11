# Towards a pre-surgery clinical decision support system

## 📦 Table of Contents

- [Overview](#overview)  
- [Installation](#installation)  
- [Dataset](#dataset)  
- [Running the Code](#running-the-code)  
- [Reproducibility](#reproducibility)  
- [License](#license)  
- [Contact](#contact)
---

## 🧠 Overview

This repository contains the replication materials for the paper **"Towards a pre-surgery clinical decision support 
system"**, which investigates the temporal and causal structure of clinical and physiological variables during  
propofol-induced general anesthesia. The work has the objective to create a lightweight model of the heart rate 
under anaesthetic administration. The model is developed according to the Bayesian Network formalism. The analysis 
is based on data provided by the PhysioNet repository
🔗 [Propofol Anesthesia Dynamics Dataset (v1.0)](https://physionet.org/content/propofol-anesthesia-dynamics/1.0/), 
consisting of a pre-processing step and a model building phase. 

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

To replicate the results both the *preprocessing* and the *modelling* phase should be run. Each phase is in a 
separate script file.

### ▶️ Preprocessing

```bash
python preprocessing.py
```

As a result, the `dataset.csv` file is generated, containing the whole dataset.

### ▶️ Model Genaration & Inference

```bash
mkdir results
python model.py
```

As a result, the `results` folder contains all the confusion matrices for all the considered hear rate variables.

## ▶️ Reprudicibility

The code reported in this paper is enough to replicate the graphs reported in the paper. Further repository evolution  
After execution, results will be saved to:

- `results/` — Graphs, plots, and model visualizations  
- `dataset.csv` — Who  

These outputs reproduce the main findings reported in the paper.
