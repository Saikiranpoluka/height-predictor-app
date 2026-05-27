# 📏 Height Prediction Web Application

An interactive Machine Learning web application that predicts an individual's height based on their weight using an optimized 2nd-degree Polynomial Regression pipeline. 

🚀 **Live App Link:** [Insert your Streamlit share URL here]

---

## 📊 Model Performance Matrix

Through systematic architectural iterations, the model achieved the following metrics:


| Model Variant | $R^2$ Accuracy | Adjusted $R^2$ | Mean Squared Error (MSE) |
| :--- | :--- | :--- | :--- |
| Baseline Linear Model | 90.85% | 87.81% | 48.4018 |
| **Polynomial Regression (Degree 2)** | **92.76%** | **90.34%** | **38.3224** |
| Random Forest Regressor | 85.86% | 81.15% | 74.8500 |

* **Robustness Check:** Validated using a shuffled 5-Fold Cross-Validation framework, confirming a stable generalizable accuracy of **79.71%** across unseen data distributions.

---

## 🛠️ Key Features

* **Automated Data Pipeline:** Implements Scikit-Learn's `make_pipeline` to cleanly encapsulate structural scaling (`StandardScaler`) and polynomial generation (`PolynomialFeatures`) to completely prevent data leakage.
* **Outlier Resilience:** Preprocessed using the statistical Interquartile Range (IQR) method to filter out anomalous training distributions.
* **Interactive UI:** A highly intuitive web dashboard featuring real-time sliders and instant conversion metrics (Metric display in Centimeters + standard Imperial conversions).

---

## 📂 Repository File Structure

```text
├── app.py                         # Streamlit interactive application interface
├── height-weight.csv              # Underlying structural dataset
├── perfect_height_predictor.joblib # Serialized inference pipeline 
└── requirements.txt               # Complete cloud environment dependency configurations
```

---

## 💻 Local Setup & Execution Guide

Follow these simple steps to run this application on your local machine:

### 1. Clone the Workspace
```bash
git clone https://github.com
cd YOUR_REPO_NAME
```

### 2. Install Required Dependencies
Ensure you have Python installed, then execute:
```bash
pip install -r requirements.txt
```

### 3. Spin Up the Local Server
Launch the interactive Streamlit engine:
```bash
streamlit run app.py
```
Your browser will automatically launch a new window at `http://localhost:8501`.

---

## ⚙️ Built With
* **Python 3.12**
* **Scikit-Learn** - Machine learning engineering & pipelines
* **Pandas & NumPy** - Data analytics & transformations
* **Matplotlib** - Feature curve plotting & visualization
* **Streamlit** - Production cloud deployment framework
