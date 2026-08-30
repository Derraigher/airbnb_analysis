from pathlib import Path
import pandas as pd

data_path = Path("../data4/cleaned")

listings_df = pd.read_csv(data_path / "cleaned_listings.csv")
calendar_df = pd.read_csv(data_path / "cleaned_calendar.csv")
reviews_df = pd.read_csv(data_path / "cleaned_reviews.csv")

listings_df = listings_df.rename(columns={"id": "listing_id"})

# After reviewing the datasets, I decided not to merge reviews.csv,
# as listings.csv already contains the necessary review metrics.
# Instead, I aggregate calendar.csv and merge it with listings,
# keeping listings as the main dataset.
calendar_df["available"] = calendar_df["available"] == "t"

calendar_summary = (
    calendar_df
    .groupby("listing_id")
    .agg(
        total_days=("available", "size"),
        available_days=("available", "sum")
        )
    .reset_index()
)
calendar_summary["unavailable_days"] = (
    calendar_summary["total_days"] - calendar_summary["available_days"]
)

#After creating a summary for calendar I proceed to merge listings and calendar

merged_df = listings_df.merge(
    calendar_summary,
    on="listing_id",
    how="left"
)



print(merged_df.head())
print(merged_df.shape)
print(merged_df.info())

print(
    merged_df[
        ["available_days", "total_days", "unavailable_days"]
    ].isnull().sum()
)

print(
    merged_df[
        ["available_days",
         "unavailable_days",
         "total_days"]
    ].describe()
)

check = (
    merged_df["available_days"]
        + merged_df["unavailable_days"]
        == merged_df["total_days"]

    )
print(check.all())

merged_df.to_csv(
    data_path / "merged_airbnb.csv",
    index=False
)




