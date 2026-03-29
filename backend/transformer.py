import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        df = X.copy()
        cols_date = ['TransactionDate', 'PreviousTransactionDate']
        for col in cols_date:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col])
        
        if 'TransactionDate' in df.columns and 'PreviousTransactionDate' in df.columns:
            df['TimeSinceLastTransaction'] = (df['TransactionDate'] - df['PreviousTransactionDate']).dt.total_seconds()
            df['TimeSinceLastTransaction'] = df['TimeSinceLastTransaction'].fillna(999999999)
        
        if 'LoginAttempts' in df.columns and 'TransactionAmount' in df.columns:
            df['RiskScoreLoginAmount'] = (np.log1p(df['LoginAttempts'])) * (np.log1p(df['TransactionAmount']))

        if 'CustomerAge' in df.columns:
            df['CustomerAgeCategory'] = pd.cut(df['CustomerAge'], bins=[0, 29, 59, 150], labels=['Young', 'Adult', 'Older']).astype(str)
        if 'TransactionAmount' in df.columns:
            df['TransactionAmountCategory'] = pd.cut(df['TransactionAmount'], bins=[-1, 250, 1000, 5000, float('inf')], labels=['Low', 'Medium', 'High', 'Very High']).astype(str)

        cols_to_drop = ['TransactionID', 'AccountID', 'DeviceID', 'IP Address', 'MerchantID', 'TransactionDate', 'PreviousTransactionDate']
        df = df.drop(columns=[c for c in cols_to_drop if c in df.columns], errors='ignore')
        return df