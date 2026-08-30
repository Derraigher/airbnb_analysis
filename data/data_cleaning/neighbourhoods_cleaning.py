from pathlib import Path
import pandas as pd

data_path = Path("../data4")
df = pd.read_csv(data_path / "neighbourhoods.csv")

#Remove neighboourhood_group column (100% missing values)
if "neighbourhood_group" in df.columns:
    df.drop(columns=["neighbourhood_group"], inplace=True)
print(df.columns)

cleaned_path = Path("../data4/cleaned")

df.to_csv(cleaned_path / "cleaned_neighbourhoods.csv", index=False)