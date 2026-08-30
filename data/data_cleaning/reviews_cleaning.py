from pathlib import Path
import pandas as pd
data_path = Path("../data4")

df = pd.read_csv(data_path / "reviews.csv")

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print("Shape:", df.shape)
print(df.columns)
print(df.dtypes)
print((data_path / "reviews.csv").resolve())

print(df.tail(3))
print(repr(df.iloc[-1]["date"]))

# Check for missing values in the 'date' column.
print(df["date"].isna().sum())
# No missing values were found, so no rows were removed.

cleaned_path = Path("../data4/cleaned")
df.to_csv(cleaned_path / "cleaned_reviews.csv")

