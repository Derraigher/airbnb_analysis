from pathlib import Path
import pandas as pd

data_path = Path("../data4/cleaned")

merged_df = pd.read_csv(data_path / "merged_featured.csv")

#Multi hosts are more expensive than the Single hosts?
print(
    merged_df.groupby("host_type")["price"]
    .agg(["count", "mean", "median", "min", "max"])
)
#As expected considering the trend it seems that the multi hosts are slightly more expensive than the single host.

#What is the most common price category?
print(
    merged_df["price_category"]
    .value_counts()
)
#The medium range is the most purchased and the Luxury is the second one while the Budget category is the Less purchased with much Less purchases.

#Which neighbourhoods have the higher average price?
print(
    merged_df.groupby("neighbourhood")["price"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
#

#Which neighbourhoods have the higher listing?
print(
    merged_df["neighbourhood"]
    .value_counts()
    .head(10)
)
#

#Does the room type affect the price?
print(
    merged_df.groupby("room_type")["price"]
    .agg(["mean", "median"])
)


print(
    merged_df.groupby("price_category")["available_days"]
      .mean()
)

print(
    merged_df.groupby("host_type")["available_days"]
      .mean()
)

print(
    merged_df.groupby("host_name")["calculated_host_listings_count"]
      .max()
      .sort_values(ascending=False)
      .head(10)
)

numeric = merged_df.select_dtypes(include="number")

print(
    numeric.corr(numeric_only=True)
)


