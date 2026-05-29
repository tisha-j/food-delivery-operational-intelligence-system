import pandas as pd # type: ignore
import numpy as np # type: ignore
from pathlib import Path


# ======================================
# LOAD DATA
# ======================================

DATA_PATH = Path("data/raw/food_delivery.csv")

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully")
print(df.head())


# ======================================
# BASIC INSPECTION
# ======================================

print("\n Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())


# ======================================
# REMOVE DUPLICATES
# ======================================

df = df.drop_duplicates()


# ======================================
# HANDLE MISSING VALUES
# ======================================

categorical_columns = [
    'Weather',
    'Traffic_Level',
    'Time_of_Day'
]

for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

df['Courier_Experience_yrs'] = df[
    'Courier_Experience_yrs'
].fillna(
    df['Courier_Experience_yrs'].median()
)


# ======================================
# FEATURE ENGINEERING
# ======================================

# Peak Hour Identification
peak_hours = ['Morning', 'Evening']

df['Peak_Hour'] = df['Time_of_Day'].apply(
    lambda x: 1 if x in peak_hours else 0
)


# Delivery Efficiency
df['Delivery_Efficiency'] = (
    df['Distance_km'] /
    df['Delivery_Time_min']
)


# ======================================
# SIMULATED BUSINESS METRICS
# ======================================

np.random.seed(42)

# Simulated Order Value
df['Order_Value'] = np.random.normal(
    loc=500,
    scale=150,
    size=len(df)
)

df['Order_Value'] = df[
    'Order_Value'
].clip(100, 2000)


# Traffic Cost Multipliers
traffic_multiplier = {
    'Low': 1.0,
    'Medium': 1.3,
    'High': 1.6
}

df['Traffic_Multiplier'] = df[
    'Traffic_Level'
].map(traffic_multiplier)


# Delivery Cost
df['Delivery_Cost'] = (
    30
    + (df['Distance_km'] * 4)
    + (df['Delivery_Time_min'] * 0.8)
    + (df['Traffic_Multiplier'] * 15)
)


# Discount Logic
df['Discount'] = np.where(
    df['Order_Value'] > 700,
    df['Order_Value'] * 0.12,
    df['Order_Value'] * 0.06
)


# Profit Calculation
df['Profit'] = (
    df['Order_Value']
    - df['Delivery_Cost']
    - df['Discount']
)


# Profit Margin
df['Profit_Margin'] = (
    df['Profit'] /
    df['Order_Value']
) * 100


# ======================================
# PERFORMANCE CATEGORIES
# ======================================

df['Delivery_Performance'] = pd.cut(
    df['Delivery_Time_min'],
    bins=[0, 30, 45, 60, 120],
    labels=[
        'Excellent',
        'Good',
        'Average',
        'Poor'
    ]
)


# ======================================
# SAVE CLEAN DATA
# ======================================

OUTPUT_PATH = Path(
    "data/processed/processed_food_delivery.csv"
)

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("\n Processed dataset saved successfully.")