from pathlib import Path
import pandas as pd
data_path = Path("../data4")

df = pd.read_csv(data_path / "listings.csv")

df["last_review"] = pd.to_datetime(df["last_review"])

print(df.head())
print(df.tail())
print(df.info())
print(df.describe(include="all"))
print("Shape:", df.shape)

#Check missing values
print("Missing values:", df.isna().sum())

#Empty strings
print((df == "").sum())

#Check duplicates
print("Duplicated rows:", df.duplicated().sum())

#Data types
print(df.dtypes)

#Dropping neighbourhood_group column due the full na values in the column
df.drop(columns=["neighbourhood_group"], inplace=True)


#Dropping the few minimum_nights values in the set
df.dropna(subset=["minimum_nights"], inplace=True)


print(df["license"].value_counts().head(20))

print((df["minimum_nights"]<=0).sum())

cleaned_path = Path("../data4/cleaned")
cleaned_path.mkdir(exist_ok=True)

df.to_csv(cleaned_path / "cleaned_listings.csv", index=False)