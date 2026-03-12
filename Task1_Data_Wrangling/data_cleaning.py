import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["Customer_Name"] = df["Customer_Name"].fillna("Unknown")
df["City"] = df["City"].fillna("Unknown")

# Convert date format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned Data:")
print(df)

print("\nData cleaning completed successfully!")