from pathlib import Path
import pandas as pd

data_path = Path("../data4/cleaned")
df = pd.read_csv(data_path / "cleaned_calendar"".csv")

df["date"] = pd.to_datetime(df["date"])


print(df.info())
print("Shape:", df.shape)

#Data quality

#Rooms availability
print(df["available"].value_counts())

#Minimum nights
print(df["minimum_nights"].describe())

print(df["minimum_nights"].value_counts().head(20))

#Maximum nights
print(df["maximum_nights"].describe())

df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year

availability = (
    df.groupby("month")["available"]
    .value_counts(normalize=True)
)
print(availability)

#Quality controls
invalid = df[df["minimum_nights"] > df["maximum_nights"]]

print(invalid[["listing_id", "minimum_nights", "maximum_nights"]].head(20))
print(invalid["minimum_nights"].value_counts().head(20))
print(invalid["maximum_nights"].value_counts().head(20))

invalid = df[df["minimum_nights"] > df["maximum_nights"]]

print("Rows:", len(invalid))
print("Unique listings:", invalid["listing_id"].nunique())

#Found 28 listings where minimum_nights exceeds maximum_nights. Since the pattern consistently affects the same listings across multiple dates and no official documentation indicates these values are erroneous, the records were preserved.



