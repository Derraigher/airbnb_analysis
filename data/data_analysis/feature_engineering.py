from pathlib import Path
import pandas as pd

data_path = Path("../data4/cleaned")

merged_df = pd.read_csv(data_path / "merged_airbnb.csv")

#Price category
def price_category(price):
    if price < 100:
        return "Budget"
    elif price < 200:
        return "Medium range"
    else:
        return "Luxury"

merged_df["price_category"] = merged_df["price"].apply(price_category)

#Host type
merged_df["host_type"] = merged_df["calculated_host_listings_count"].apply(
    lambda x: "Single Host" if x == 1 else "Multi Host"
)

#Availability rate
merged_df["availability_rate"] = (
    merged_df["available_days"] / merged_df["total_days"]
)


