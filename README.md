# Autism Analysis Copilot 🧩

**AI-Based Decision Support System for Autism Spectrum Disorder (ASD) Screening and Coaching**

Autism Analysis Copilot is an AI-powered web-based decision support system designed to assist specialists and caregivers in **early ASD screening, multimodal analysis, report generation, and personalized coaching**.

The system combines machine learning, explainable AI concepts, multimodal data analysis, and a web-based platform to support specialists throughout the screening and coaching process.

> **Important:** Autism Analysis Copilot is a research and decision-support system. It is **not a medical diagnostic tool** and does not replace professional clinical assessment or human interaction.

---

## 📌 Project Overview

Early identification of Autism Spectrum Disorder can help children receive appropriate support at an earlier stage. However, ASD assessment may involve multiple behavioral, linguistic, physiological, and neurological indicators.

Autism Analysis Copilot aims to provide a unified platform where specialists can review different types of data, obtain AI-assisted screening results, generate reports, and create personalized coaching plans.

The project consists of two main phases:

1. **ASD Screening & Analysis**
2. **Personalized Coaching**

---

## 🎯 Objectives

* Assist specialists with AI-based ASD screening.
* Analyze multiple modalities related to ASD.
* Provide transparent and interpretable AI-assisted results.
* Generate structured screening reports.
* Support communication between specialists and caregivers.
* Provide personalized coaching activities for children.
* Track coaching progress and goals.
* Maintain the role of human specialists throughout the decision-making process.

---

## 🧠 Multimodal ASD Analysis

The project explores several modalities that can contribute to ASD screening:

| Modality            | Purpose                                                           |
| ------------------- | ----------------------------------------------------------------- |
| 👁️ Eye Tracking    | Analyze visual attention, fixation patterns, and scanpaths        |
| 🗣️ Speech Analysis | Analyze linguistic features and predict ADOS-related scores       |
| 🧠 EEG              | Analyze neurological signals associated with ASD                  |
| 🧬 Neuroimaging     | Consider neuroimaging data as a potential screening modality      |
| 📋 ADOS             | Use standardized behavioral assessment information as a reference |

### Implemented Modalities

The implemented prototype focuses on:

* Eye-tracking analysis
* Speech analysis
* EEG analysis

Other modalities were investigated as part of the overall multimodal system design.

---

# 🔬 AI Models

## 👁️ Eye-Tracking Analysis

The eye-tracking module analyzes visual attention patterns to distinguish between ASD and typically developing (TD) samples.

### Dataset

* 300 ASD samples
* 300 TD samples
* Total: 600 samples
* Input shape: `224 × 224 × 3`

### Model

A Convolutional Neural Network (CNN) was used for classification.

### Results

| Metric   | Result |
| -------- | -----: |
| Accuracy |  75.0% |
| F1 Score | 73.68% |
| AUC      | 82.25% |

Confusion Matrix:

```text
[[48, 12],
 [18, 42]]
```

The results demonstrate the potential of eye-tracking patterns as an AI-assisted screening signal.

---

## 🗣️ Speech Analysis

The speech module analyzes linguistic information and predicts an ADOS-related score.

### Dataset

The speech dataset contains:

* 136 children
* 100 time steps
* 49 features
* ADOS scores ranging from 0–22

Dataset shape:

```text
(136, 100, 49)
```

### Models

Two machine learning models were evaluated:

* Random Forest
* XGBoost

### Results

| Model         |  RMSE |
| ------------- | ----: |
| Random Forest | 4.032 |
| XGBoost       | 3.626 |

XGBoost achieved a lower RMSE on the evaluated dataset.

---

## 🧠 EEG Analysis

The project also incorporates EEG-based analysis as one of the neurological modalities considered for ASD screening.

A deep learning approach was investigated using **EEGNet**, a convolutional neural network architecture designed for EEG signal analysis.

The EEG component is intended to demonstrate how neurological signals can complement behavioral and linguistic information within a multimodal screening framework.

---

# 🤖 Explainable AI

A major goal of Autism Analysis Copilot is to move beyond simply producing an AI prediction.

The system follows an **Explainable AI (XAI)** approach to help specialists understand the factors behind AI-assisted results.

The AI output is therefore presented as **decision-support information**, rather than an independent diagnosis.

The system is designed around the principle:

```text
AI Recommendation
       ↓
Explanation / Supporting Evidence
       ↓
Specialist Review
       ↓
Clinical Decision
```

---

# 👨‍⚕️ System Users

The platform contains different user roles to support the screening and coaching workflow.

### 👨‍⚕️ Specialist

Specialists can:

* Review child information.
* Review screening results.
* Analyze different modalities.
* Complete customized assessment checklists.
* Review generated reports.
* Send reports to caregivers.
* Create coaching goals.
* Set activity difficulty and duration.
* Monitor coaching progress.

### 👨‍👩‍👧 Caregiver / Parent

Caregivers can:

* Enter child information.
* Select a specialist.
* View screening reports.
* Receive specialist feedback.
* Follow the child's coaching progress.

### 👦 Child

Children can access assigned coaching activities based on the goals created by the specialist.

---

# 🎮 Personalized Coaching

The second phase of the project focuses on personalized coaching.

The coaching component is inspired by **ABLLS-R domains** and organizes activities around areas such as:

* Social Interaction
* Communication
* Cognitive Skills
* Behavioral Skills
* Daily Living Skills
* Emotional Recognition

Specialists can personalize activities according to the child's needs by adjusting:

* Activity type
* Difficulty
* Duration
* Goals
* Progress tracking

The coaching component is intended to **support existing intervention and educational practices**, not replace professional therapy or human interaction.

---

# 🏗️ System Architecture

The overall workflow can be summarized as:

```text
                    ┌─────────────────────┐
                    │      Caregiver      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Child Information │
                    └──────────┬──────────┘
                               │
                               ▼
              ┌─────────────────────────────────┐
              │       Autism Analysis Copilot   │
              │                                 │
              │  ┌──────────┐  ┌────────────┐  │
              │  │   Eye    │  │   Speech   │  │
              │  │ Tracking │  │  Analysis  │  │
              │  └────┬─────┘  └──────┬─────┘  │
              │       │               │        │
              │       └───────┬───────┘        │
              │               │                │
              │        ┌──────▼──────┐         │
              │        │     EEG     │         │
              │        │   Analysis  │         │
              │        └──────┬──────┘         │
              │               │                │
              │        ┌──────▼──────┐         │
              │        │ AI Decision │         │
              │        │   Support   │         │
              │        └──────┬──────┘         │
              │               │                │
              └───────────────┼────────────────┘
                              │
                 ┌────────────▼────────────┐
                 │   Specialist Review     │
                 └────────────┬────────────┘
                              │
                 ┌────────────▼────────────┐
                 │    Screening Report     │
                 └────────────┬────────────┘
                              │
                 ┌────────────▼────────────┐
                 │ Personalized Coaching   │
                 └─────────────────────────┘
```

---

# 💻 Technology Stack

### Programming & AI

* Python
* PyTorch
* Scikit-learn
* XGBoost
* Pandas
* NumPy

### Deep Learning

* CNN
* ResNet18
* EEGNet

### Backend

* Django
* Python

### Data & Analysis

* NumPy
* Pandas
* MATLAB datasets
* Machine Learning pipelines

### Reporting

* ReportLab
* PDF report generation

### Development

* Git
* GitHub
* VS Code

---

# 🌐 Web Application

The web application provides a centralized environment for specialists and caregivers.

### Main workflow

```text
Register / Login
      ↓
Select User Role
      ↓
Enter Child Information
      ↓
Upload / Process Assessment Data
      ↓
AI Analysis
      ↓
Review Results
      ↓
Generate Report
      ↓
Specialist Review
      ↓
Personalized Coaching
      ↓
Progress Tracking
```

---

# 📊 Project Results

The developed prototype demonstrates how multiple AI-based analysis components can be integrated into a single decision-support platform.

Key results include:

* **Eye-tracking classification:** 75% accuracy and 82.25% AUC.
* **Speech analysis:** XGBoost achieved an RMSE of 3.626.
* **EEG analysis:** EEGNet was investigated for neurological signal analysis.
* **Web platform:** Integrated screening, reporting, specialist review, and coaching workflows.
* **Personalized coaching:** Supports goal setting, activity customization, and progress tracking.

---

# 🔐 Ethics & Limitations

Because ASD screening involves sensitive information, privacy, ethics, and responsible AI are important considerations.

### Limitations

* Available datasets were relatively small.
* Access to real-world authorized child data was limited because of privacy and ethical requirements.
* Model performance may not generalize to different populations or clinical environments.
* The prototype has not been validated as a clinical diagnostic system.
* AI predictions should not be interpreted as definitive diagnoses.
* Human specialists remain essential for assessment and intervention decisions.

### Responsible AI

The project is designed to support:

* Human oversight
* Explainability
* Privacy-aware data handling
* Responsible interpretation of predictions
* Non-replacement of professional assessment

---

# 📁 Project Structure

```text
Autism-Analysis-Copilot/
│
├── backend/
│   ├── ...
│   └── ...
│
├── models/
│   ├── asd_model.pth
│   └── ...
│
├── eye_tracking/
│   ├── ...
│   └── ...
│
├── speech_analysis/
│   ├── ...
│   └── ...
│
├── eeg_analysis/
│   ├── ...
│   └── ...
│
├── reports/
│   └── ...
│
├── static/
│   └── ...
│
├── templates/
│   └── ...
│
├── requirements.txt
├── manage.py
└── README.md
```

> The exact structure may vary depending on the final version of the project repository.

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/autism-analysis-copilot.git
cd autism-analysis-copilot
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Django Application

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

---

# 📌 Future Improvements

Potential future improvements include:

* Larger and more diverse datasets.
* Subject-level data splitting to improve evaluation reliability.
* Additional multimodal fusion techniques.
* More advanced explainability methods.
* Improved EEG classification performance.
* Integration of additional clinical assessment information.
* More personalized coaching recommendations.
* Improved progress analytics.
* Deployment to a secure cloud environment.
* Further validation with authorized real-world data.

---

# 🎓 Graduation Project

**Project:** Autism Analysis Copilot
**Title:** AI-Based Decision Support System for Autism Spectrum Disorder (ASD) Screening and Coaching
**Project Grade:** A+
**Field:** Software Engineering / Artificial Intelligence / Data Analysis

This project was developed as a **graduation project** with the goal of combining AI, data analysis, and software engineering to create a responsible decision-support platform for ASD screening and personalized coaching.

---

# 👩‍💻 Authors

**Rawan Montasser**
Software Engineering Graduate | Junior Data Engineer | Data Analyst

**Team Members:**
Gana Ahmed, Joelle Fouad, Farida Diaa

---

# 📄 Disclaimer

Autism Analysis Copilot is an academic research project and prototype.

The system is **not intended to diagnose Autism Spectrum Disorder**, provide medical advice, or replace qualified healthcare professionals. AI-generated results are intended to support specialist review and should be interpreted within the appropriate professional and clinical context.
