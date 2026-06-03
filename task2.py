import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# ----------------------------
# Dataset Overview
# ----------------------------
print("FIRST 5 ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nMISSING VALUES")
print(df.isnull().sum())

# ----------------------------
# Sales by Category
# ----------------------------
sales_by_category = df.groupby("Category")["Sales"].sum().sort_values()

plt.figure(figsize=(10,6))
sales_by_category.plot(kind="bar")
plt.title("Total Sales by Category", fontsize=16)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Sales", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# ----------------------------
# Profit by Category
# ----------------------------
profit_by_category = df.groupby("Category")["Profit"].sum().sort_values()

plt.figure(figsize=(10,6))
profit_by_category.plot(kind="bar")
plt.title("Total Profit by Category", fontsize=16)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Profit", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.show()

# ----------------------------
# Sales by Region
# ----------------------------
sales_by_region = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(10,6))
sales_by_region.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution by Region", fontsize=16)
plt.ylabel("")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

# ----------------------------
# Histogram of Sales
# ----------------------------
plt.figure(figsize=(10,6))
plt.hist(df["Sales"], bins=30)
plt.title("Distribution of Sales", fontsize=16)
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("sales_histogram.png")
plt.show()

print("\nEDA COMPLETED SUCCESSFULLY!")