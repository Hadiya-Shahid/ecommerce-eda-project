import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("C:/Users/Administrator/Downloads/ecommerce_sales_200_rows.csv")
print(df.head(3))

# Check missing values
print(df.isnull().sum())

# Convert Order Date column to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])
print(df["Order Date"])

# Top selling products
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
top_products.plot(kind="bar", color="skyblue")
plt.title("Top Selling Products")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Sales by region
region_sales = df.groupby("Region")["Sales"].sum()
plt.figure(figsize=(7,5))
region_sales.plot(kind="pie", autopct='%1.1f%%')
plt.title("Sales by Region")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Sales trend over time
sales_trend = df.groupby("Order Date")["Sales"].sum()
plt.figure(figsize=(10,5))
sales_trend.plot(kind="line", marker="o")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Final Summary
print("\nSummary Stats:\n", df.describe())