import pandas as pd # type: ignore
from pathlib import Path


# =====================================
# LOAD PROCESSED DATA
# =====================================

df = pd.read_csv(
    "data/processed/processed_food_delivery.csv"
)

print("Processed dataset loaded successfully.\n")


# =====================================
# CREATE OUTPUT FOLDER
# =====================================

output_path = Path("dashboards/data")

output_path.mkdir(
    parents=True,
    exist_ok=True
)


# =====================================
# EXECUTIVE KPI SUMMARY
# =====================================

executive_summary = pd.DataFrame({

    "Total_Orders": [len(df)],

    "Total_Revenue": [
        round(df['Order_Value'].sum(), 2)
    ],

    "Total_Profit": [
        round(df['Profit'].sum(), 2)
    ],

    "Average_Delivery_Time": [
        round(df['Delivery_Time_min'].mean(), 2)
    ],

    "Average_Profit_Margin": [
        round(df['Profit_Margin'].mean(), 2)
    ]
})

executive_summary.to_csv(
    output_path / "executive_summary.csv",
    index=False
)

print("Executive summary table created.")


# =====================================
# TRAFFIC ANALYSIS TABLE
# =====================================

traffic_analysis = (
    df.groupby('Traffic_Level')
    .agg({
        'Delivery_Time_min': 'mean',
        'Profit': 'mean',
        'Profit_Margin': 'mean',
        'Order_ID': 'count'
    })
    .reset_index()
)

traffic_analysis.columns = [
    'Traffic_Level',
    'Average_Delivery_Time',
    'Average_Profit',
    'Average_Profit_Margin',
    'Total_Orders'
]

traffic_analysis.to_csv(
    output_path / "traffic_analysis.csv",
    index=False
)

print("Traffic analysis table created.")


# =====================================
# VEHICLE PERFORMANCE TABLE
# =====================================

vehicle_analysis = (
    df.groupby('Vehicle_Type')
    .agg({
        'Delivery_Time_min': 'mean',
        'Profit': 'mean',
        'Profit_Margin': 'mean'
    })
    .reset_index()
)

vehicle_analysis.columns = [
    'Vehicle_Type',
    'Average_Delivery_Time',
    'Average_Profit',
    'Average_Profit_Margin'
]

vehicle_analysis.to_csv(
    output_path / "vehicle_analysis.csv",
    index=False
)

print("Vehicle analysis table created.")


# =====================================
# WEATHER ANALYSIS TABLE
# =====================================

weather_analysis = (
    df.groupby('Weather')
    .agg({
        'Delivery_Time_min': 'mean',
        'Profit': 'mean',
        'Profit_Margin': 'mean'
    })
    .reset_index()
)

weather_analysis.columns = [
    'Weather',
    'Average_Delivery_Time',
    'Average_Profit',
    'Average_Profit_Margin'
]

weather_analysis.to_csv(
    output_path / "weather_analysis.csv",
    index=False
)

print("Weather analysis table created.")


# =====================================
# PEAK HOUR ANALYSIS TABLE
# =====================================

peak_hour_analysis = (
    df.groupby('Peak_Hour')
    .agg({
        'Delivery_Time_min': 'mean',
        'Profit': 'mean',
        'Order_ID': 'count'
    })
    .reset_index()
)

peak_hour_analysis.columns = [
    'Peak_Hour',
    'Average_Delivery_Time',
    'Average_Profit',
    'Total_Orders'
]

peak_hour_analysis.to_csv(
    output_path / "peak_hour_analysis.csv",
    index=False
)

print("Peak hour analysis table created.")


# =====================================
# HIGH RISK DELIVERIES TABLE
# =====================================

high_risk_deliveries = df[
    (df['Delivery_Time_min'] > 60)
    &
    (df['Profit'] < 200)
]

high_risk_deliveries.to_csv(
    output_path / "high_risk_deliveries.csv",
    index=False
)

print("High-risk deliveries table created.")


# =====================================
# FINAL MESSAGE
# =====================================

print("\nAll dashboard datasets created successfully.")