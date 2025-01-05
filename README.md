# Explainable AI Lab

## Table of Contents
1. [Introduction](#introduction)
2. [Instructions to run on Azure](#instructions-to-run-on-azure)
    - [Clone project](#clone-project)
    - [Go to workspace](#go-to-workspace)
    - [Create Compute](#create-compute)
    - [Create conda environment + Kernel](#create-conda-environment--kernel)
    - [Run notebook](#run-notebook)
3. [Instructions to run locally](#instructions-to-run-locally)
    - [Prerequisites](#prerequisites)
    - [Create conda environment + Kernel](#create-conda-environment--kernel-1)
    - [Run notebook](#run-notebook-1)

## Introduction

Explainable AI (XAI) focuses on the transparency and understandability of AI model decisions, fostering trust among users. By making complex AI processes clear and comprehensible, XAI addresses the need for fairness, ethical assurance, and regulatory compliance, particularly in sensitive domains. In this XAI lab, you will experiment with different XAI methods on tabular, image and text data.


**Clone project**
1. `git clone git@github.com:ann-w/xai_labs.git` or download as zip (code > download ZIP)

### Prerequisites
- Anaconda

**Create conda environment + Kernel**
1. Open project in Jupyterlab
2. Open new terminal
3. Open a new terminal and run the following commands from the project directory
5. Run the following commands: 
    ```
    conda create -y --name xai_lab python=3.11
    conda activate xai_lab
    pip install -r requirements.txt
    conda install ipykernel -y
    python -m ipykernel install --user --name xai_lab --display-name "python_xai_lab"
    ```

**Run notebook**
1. Open xai_lab.ipynb. Select kernel "pyhon_xai_lab"
2. Follow the instructions in the notebook. Feel free to run the three sections (tabular, text, image) in any order you want.


Goodluck!


## References

This tutorial is based on the documentation and information provided by the following resources.

- [Captum](https://captum.ai/tutorials/)
- [Lime]()
- [Shap]()
- [inseq]()
- [Explainable AI: A brief survey on history, research areas, approaches and challenges (Xu et al., 2019)](https://www.researchgate.net/profile/Feiyu-Xu/publication/336131051_Explainable_AI_A_Brief_Survey_on_History_Research_Areas_Approaches_and_Challenges/links/5e2b496f92851c3aadd7bf08/Explainable-AI-A-Brief-Survey-on-History-Research-Areas-Approaches-and-Challenges.pdf)
- [Explainability for large language models: A survey (Zhao et al., 2023)](https://dl.acm.org/doi/pdf/10.1145/3639372)

