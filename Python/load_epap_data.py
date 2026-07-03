import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

DB_USER = "postgres"
DB_PASSWORD = "postgres123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "pricing_intelligence"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

load_order = [
    "dim_region",
    "dim_product",
    "dim_account_manager",
    "dim_contract_type",
    "dim_opportunity_stage",
    "dim_customer",
    "dim_date",
    "fact_opportunity",
    "fact_quote",
    "fact_contract",
    "fact_booking",
    "fact_usage",
]

for table in load_order:
    file_path = DATA_DIR / f"{table}.csv"
    df = pd.read_csv(file_path)
    df.to_sql(table, engine, if_exists="append", index=False)
    print(f"Loaded {table}: {len(df)} rows")

print("All EPAP data loaded successfully.")