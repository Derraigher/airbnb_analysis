from pathlib import Path
import pandas as pd

data_path = Path("../data4/cleaned")
df = pd.read_csv(data_path / "cleaned_reviews.csv")

df["date"] = pd.to_datetime(df["date"])

print("Total number of reviews:", len(df))
print("Announces reviewd", df["listing_id"].nunique())
print("First review:", df["date"].min())
print("Last review:", df["date"].max())


#Reviews per year
print("\n Reviews per year")
df["year"] = df["date"].dt.year
reviews_per_year = df["year"].value_counts().sort_index
print(reviews_per_year)

#Reviews per month
print("\n Reviews per month")
df["month"] = df["date"].dt.month
reviews_per_month = df["month"].value_counts().sort_index
print(reviews_per_month)

#Monthly performance
print("\n Monthly performance")
df["year_month"] = df["date"].dt.to_period("M")

monthly_reviews = df.groupby("year_month").size()
print(monthly_reviews.tail(20))

#announcements with most reviews
print("\nAnnouncements with most reviews")
top_listings = (
    df["listing_id"]
    .value_counts()
    .head(20)
)

print(top_listings)

