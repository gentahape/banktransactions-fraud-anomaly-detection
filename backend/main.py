from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from transformer import FeatureEngineer
from pathlib import Path

import __main__
__main__.FeatureEngineer = FeatureEngineer

app = FastAPI(title="Bank Transactions Fraud & Anomaly Detection API")

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / 'models' / 'final_fraud_pipeline_tuned.joblib'
try:
    model = joblib.load(f'{BASE_DIR.parent}/backend/models/final_fraud_pipeline_tuned.joblib')
except Exception as e:
    raise RuntimeError(f"Fail to load model. Make sure the model file exist in: {MODEL_PATH}") from e

class TransactionData(BaseModel):
    TransactionDate: str
    PreviousTransactionDate: str
    TransactionAmount: float
    CustomerAge: int
    TransactionDuration: float
    LoginAttempts: int
    AccountBalance: float
    Location: str
    Channel: str
    CustomerOccupation: str
    TransactionType: str

@app.get("/")
def home():
    return {"message": "Bank Transactions Fraud & Anomaly Detection API is Running"}

@app.post("/predict")
def predict(data: TransactionData):
    try:
        input_df = pd.DataFrame([data.dict()])
        
        prediction = model.predict(input_df)[0]
        
        cluster_info = {
            0: "Stable: Infrequent Mature Transactor (Low frequency, moderate value)",
            1: "Stable: Established Adult Segment (High balance, low risk)",
            2: "CRITICAL: Velocity Attack Detected (Zero-second transaction gap!)",
            3: "Stable: Conservative Low-Value Spender (Older age, small transactions)",
            4: "Premium: High-Value Transactor (High transaction amount, low risk)"
        }

        return {
            "status": "success",
            "cluster_id": int(prediction),
            "interpretation": cluster_info.get(int(prediction), "Cluster Unknown")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))