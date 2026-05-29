import sqlite3
import pandas as pd
from pathlib import Path


# =========================
# CONNECT TO DATABASE
# =========================

conn = sqlite3.connect("food_delivery.db")

print("Connected to database successfully.\n")


# =========================
# LOAD SQL FILE
# =========================

sql_file_path = Path(__file__).resolve().parent.parent / "sql" / "business_queries.sql"

with open(sql_file_path, "r") as file:
    sql_script = file.read()


# =========================
# SPLIT QUERIES
# =========================

queries = sql_script.split(";")



# =========================
# EXECUTE EACH QUERY
# =========================

for i, query in enumerate(queries):

    query = query.strip()

    if query:

        try:
            print(f"\n========== QUERY {i+1} ==========\n")

            result = pd.read_sql_query(query, conn)

            print(result.head())

        except Exception as e:

            print(f"Error in Query {i+1}:")
            print(e)


# =========================
# CLOSE CONNECTION
# =========================

conn.close()

print("\nDatabase connection closed.")