"""Synthetic Data Generator for Customer Churn Prediction."""

import os
import numpy as np
import pandas as pd

def generate_churn_dataset(file_path: str, n_samples: int = 150, seed: int = 42):
    np.random.seed(seed)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    customer_ids = [f"CUST_{1000 + i}" for i in range(n_samples)]
    tenure = np.random.randint(1, 72, size=n_samples)
    monthly_charges = np.round(np.random.uniform(20.0, 115.0, size=n_samples), 2)
    contract = np.random.choice(['Month-to-month', 'One year', 'Two year'], size=n_samples, p=[0.55, 0.25, 0.20])
    tech_support = np.random.choice(['Yes', 'No'], size=n_samples, p=[0.4, 0.6])
    online_security = np.random.choice(['Yes', 'No'], size=n_samples, p=[0.45, 0.55])
    payment_method = np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'], size=n_samples)

    total_charges = np.round(tenure * monthly_charges * np.random.uniform(0.95, 1.05, size=n_samples), 2)

    # Churn probability based on realistic business rules:
    # High monthly charge + short tenure + month-to-month contract + no tech support => higher churn
    logits = (
        (monthly_charges - 60) * 0.03
        - (tenure - 30) * 0.05
        + (contract == 'Month-to-month') * 1.2
        - (tech_support == 'Yes') * 0.8
        - 0.5
    )
    probs = 1 / (1 + np.exp(-logits))
    churn = (np.random.uniform(0, 1, size=n_samples) < probs).astype(int)

    df = pd.DataFrame({
        'CustomerID': customer_ids,
        'Tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'Contract': contract,
        'TechSupport': tech_support,
        'OnlineSecurity': online_security,
        'PaymentMethod': payment_method,
        'Churn': churn
    })

    df.to_csv(file_path, index=False)
    print(f"Generated {len(df)} records at {file_path}. Churn rate: {df['Churn'].mean():.2%}")

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "churn_data.csv")
    generate_churn_dataset(out)
