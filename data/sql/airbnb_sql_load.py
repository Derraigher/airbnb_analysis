from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

data_path = Path("../data4/cleaned")

engine = create_engine(
    "mysql+pymysql://root:0000@localhost/airbnb"
)


tables = [
    "cleaned_calendar",
   "cleaned_listings",
    "cleaned_neighbourhoods",
    "cleaned_reviews",
    "merged_airbnb",
    "merged_featured"
]

print(tables)



for table in tables:
    print(f"Loading {table}...")

    df = pd.read_csv(data_path / f"{table}.csv")

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table} loaded")