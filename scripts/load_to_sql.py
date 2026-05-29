from sqlalchemy import create_engine
import pandas as pd


# =========================
# LOAD CLEAN DATA
# =========================

df = pd.read_csv(
    "data/processed/processed_food_delivery.csv"
)


# =========================
# CREATE SQLITE DATABASE
# =========================

engine = create_engine(
    "sqlite:///food_delivery.db"
)


# =========================
# LOAD DATA INTO SQL
# =========================

df.to_sql(
    "food_delivery",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully.")