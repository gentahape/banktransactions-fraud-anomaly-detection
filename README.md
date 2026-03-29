# Bank Transaction Fraud & Anomaly Detection System

An end-to-end Machine Learning engineering project that transforms raw banking data into a production-ready anomaly detection system. 

This project demonstrates a **Hybrid Machine Learning Approach**, utilizing Unsupervised Learning (K-Means Clustering) to discover hidden transaction patterns and define customer personas, followed by Supervised Learning (XGBoost) to classify and detect suspicious activities in real-time.

## Project Origin
This project originally started as a final submission for the **"Belajar Machine Learning untuk Pemula"** (Learn Machine Learning for Beginners) certification at [Dicoding](https://www.dicoding.com/academies/184). 

Taking it a step further, I leveraged my background as a **Fullstack Web Developer** to go beyond the standard Jupyter Notebook environment. I architected and deployed the trained machine learning pipeline into a decoupled, real-world application featuring a high-performance REST API and an interactive web interface.

## Key Features
* **Custom Scikit-Learn Pipeline:** Encapsulates custom feature engineering, preprocessing, and the tuned XGBoost model into a single `.joblib` artifact.
* **RESTful AI Backend:** Powered by **FastAPI** to serve model predictions asynchronously with strict data validation using Pydantic.
* **Interactive Detection Lab:** A **Streamlit** frontend allowing users to simulate normal transactions and fraud scenarios with quick-load presets.
* **Explainable AI (XAI):** Integration of SHAP (SHapley Additive exPlanations) insights to provide transparency on why the AI flagged a transaction as anomalous.

## Tech Stack
**Machine Learning & Data Science:**
* Python, Pandas, Matplotlib, Plotly
* Scikit-Learn, XGBoost, SHAP
* Jupyter Notebook (Google Colab)

**Software Engineering & Deployment:**
* **Backend:** FastAPI, Uvicorn, Pydantic
* **Frontend:** Streamlit
* **Tools:** Git, Pipenv, Joblib

## Project Structure
```text
├── backend/
│   └── models
│       └── final_fraud_pipeline_tuned.joblib
│   ├── main.py
│   ├── transformer.py
├── frontend/
│   ├── app.py
│   └── assets/
├── notebooks/
│   └── Bank_Transactions_Fraud_Anomaly_Detection.ipynb
├── .env.example
├── .gitignore
├── Pipfile
└── README.md
```

## Installation & Setup
Follow these steps to run the application on your local machine.

1. Clone the Repository
```bash
git clone https://github.com/gentahape/banktransactions-fraud-anomaly-detection.git
cd banktransactions-fraud-anomaly-detection
```

2. Install Dependencies
Make sure you have Python 3.9+ installed. You can install the required packages using pip or pipenv.
```bash
pip install fastapi uvicorn streamlit scikit-learn xgboost pandas requests python-dotenv
```

3. Environment Setup
Create a `.env` file in the root directory and specify your backend URL:
```text
API_URL=http://127.0.0.1:8000
```

4. Run the Backend (FastAPI)
Open a terminal and start the Uvicorn server:
```bash
cd backend
uvicorn main:app --reload
```

*The API will be available at `http://127.0.0.1:8000`. You can view the interactive API documentation at `http://127.0.0.1:8000/docs`.*

5. Run the Frontend (Streamlit)
Open a new/separate terminal and start the Streamlit app:
```bash
streamlit run frontend/app.py
```

*The interactive simulator will open automatically in your browser at `http://localhost:8501`.*