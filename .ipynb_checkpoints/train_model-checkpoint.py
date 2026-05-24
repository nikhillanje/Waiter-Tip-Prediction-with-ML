import pandas as pd
import joblib
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor

# =====================================
# LOAD DATASET
# =====================================

df = pd.read_csv("tips.csv")

# =====================================
# ENCODE CATEGORICAL DATA
# =====================================

encoder = LabelEncoder()

for col in ['sex', 'smoker', 'day', 'time']:

    df[col] = encoder.fit_transform(df[col])

# =====================================
# FEATURES AND TARGET
# =====================================

X = df.drop('tip', axis=1)

y = df['tip']

# =====================================
# FEATURE SCALING
# =====================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# =====================================
# TRAIN MODEL
# =====================================

model = GradientBoostingRegressor()

model.fit(X_scaled, y)

# =====================================
# CREATE FOLDER
# =====================================

os.makedirs("outputs/models", exist_ok=True)

# =====================================
# SAVE MODEL
# =====================================

joblib.dump(
    model,
    "outputs/models/gradient_boosting.pkl"
)

# =====================================
# SAVE SCALER
# =====================================

joblib.dump(
    scaler,
    "outputs/models/scaler.pkl"
)

print("Model and scaler saved successfully")