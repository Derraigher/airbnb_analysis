from pathlib import Path
import pandas as pd
data_path = Path("../data4")
df = pd.read_csv(data_path / "calendar.csv")

#Convert data column to datetime
df["date"] = pd.to_datetime(df["date"])



# Missing values
print("Missing values:",df.isna().sum())

#Empty strings
print((df == "").sum())

# Duplicates
print("Duplicated rows:",df.duplicated().sum())

# Data types
print(df.dtypes)


#Check for invalid minimum nights
print((df["minimum_nights"]<= 0).sum())

#Check for invalid maximum nights
print((df["maximum_nights"]<= 0).sum())

cleaned_path = Path("../data4/cleaned")


df.to_csv(cleaned_path / "cleaned_calendar.csv", index=False)




