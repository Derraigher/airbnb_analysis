from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

data_path = Path("../data4/cleaned")
df = pd.read_csv(data_path / "cleaned_listings.csv")


print(df.info())
print("Shape:", df.shape)

#Data quality

#Listing dataset overview
print("Total listings:", len(df))
print("Unique hosts:", df["host_id"].nunique())
print("Neighbourhood:", df["neighbourhood"].nunique())

#Price analysis
print("\n Price analysis")
print(df["price"].describe())
print("Quantile price:",df["price"].quantile(0.25))
print(df["price"].quantile([0.90, 0.95, 0.99]))

#Prices distribution
plt.figure(figsize=(8,5))
plt.hist(df["price"].dropna(), bins=50)
plt.title("Distribution of listing price")
plt.xlabel("Price (€)")
plt.ylabel("Number of listings")
plt.show()

#Neighbourhoods
print("\n Neighbourhoods analysis")
print(df["neighbourhood"].value_counts().head(20))

#Average price by neighbourhood
print(df.groupby("neighbourhood")["price"]\
    .mean()\
    .sort_values(ascending=False))

#Average price by room type
print(df.groupby("room_type")["price"]
    .mean()
    .sort_values(ascending=False))

print(
    df.groupby("room_type")["price"]
      .agg(["count", "mean", "median", "min", "max"])
)

#Top 10 neighbourhood with more listing
top = df["neighbourhood"].value_counts().head(10)

plt.figure(figsize=(8, 5))
top.plot(kind="bar")
plt.title("Top 10 neighbourhoods by listings")
plt.ylabel("Listings")
plt.xticks(rotation=45)
plt.show()


avg_price = df.groupby("room_type")["price"].mean()


#Average price for room type graph
plt.figure(figsize=(7,9))
avg_price.plot(kind="bar")
plt.title("Average Price by Room Type")
plt.ylabel("Average Price (€)")
plt.show()

#Room type distribution
print("\nRoom types analysis")
print(df["room_type"].value_counts())
print(df["room_type"].value_counts(normalize=True) * 100)

#Availability
print("\nAvailability analysis")
print(df["availability_365"].describe())
print(df["availability_365"].value_counts().sort_index())

#Availability distributions
plt.figure(figsize=(8,5))
plt.hist(df["availability_365"], bins=50)
plt.title("Availabity distribution")
plt.xlabel("Days available")
plt.ylabel("Listings")
plt.show()


#Number of reviews
print("\nNumber of reviews")
print(df["number_of_reviews"].describe())
print(df.nlargest(20, "number_of_reviews"))
print(df["number_of_reviews"].quantile([0.5, 0.75, 0.9, 0.99]))

print("\nReviews per month")
print(df["reviews_per_month"].describe())

#Correlations
print("\n Correlations")
numeric = [
    "price",
    "minimum_nights",
    "number_of_reviews",
    "reviews_per_month",
    "availability_365"
]

print(df[numeric].corr())

#Host with multiple listings
print("\nHosts with multiple listings")
print(df.groupby("host_id").size().sort_values(ascending=False).head(20))

#Minimum nights
print("\nMinimum nights")
print(df["minimum_nights"].describe())
print(df["minimum_nights"].value_counts().head(20))







