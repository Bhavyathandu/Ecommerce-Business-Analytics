import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/Superstore.csv", encoding="latin1")

# Display first 5 rows
print(df.head())

# Display dataset size
print(df.shape)

# Display column names
print(df.columns)

# Display dataset information
print(df.info())

# Display missing values
print(df.isnull().sum())

# Dataset summary
print(df.describe(include="all"))

# ============================
# DATA CLEANING
# ============================

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

print("Duplicate Rows:", df.duplicated().sum())
print("Dataset Shape After Cleaning:", df.shape)

# ============================
# KPI ANALYSIS
# ============================

print("\n========== KPI ANALYSIS ==========")

# Total Sales
total_sales = df["Sales"].sum()
print("Total Sales :", round(total_sales, 2))

# Total Profit
total_profit = df["Profit"].sum()
print("Total Profit :", round(total_profit, 2))

# Total Orders
total_orders = df["Order ID"].nunique()
print("Total Orders :", total_orders)

# Total Customers
total_customers = df["Customer ID"].nunique()
print("Total Customers :", total_customers)

# Average Sales
average_sales = df["Sales"].mean()
print("Average Sales :", round(average_sales, 2))

# Average Profit
average_profit = df["Profit"].mean()
print("Average Profit :", round(average_profit, 2))

# ==========================================
# BUSINESS ANALYSIS - REGION
# ==========================================

print("\n========== REGION ANALYSIS ==========\n")

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print(region_sales)
region_sales.plot(kind="bar", figsize=(8,5))

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.savefig("charts/region_sales.png")
plt.show()
plt.close()

# ==========================================
# CATEGORY ANALYSIS
# ==========================================

print("\n========== CATEGORY ANALYSIS ==========\n")

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print(category_sales)

category_sales.plot(kind="bar", figsize=(8,5))
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("charts/category_sales.png")
plt.show()
plt.close()


# ==========================================
# STATE ANALYSIS
# ==========================================

print("\n========== STATE ANALYSIS ==========\n")

state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False)

print(state_sales.head(10))

state_sales.head(10).plot(kind="bar", figsize=(10,5))

plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("charts/state_sales.png")
plt.show()
plt.close()
# ==========================================
# CUSTOMER SEGMENT ANALYSIS
# ==========================================

print("\n========== CUSTOMER SEGMENT ANALYSIS ==========\n")

segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

print(segment_sales)

segment_sales.plot(kind="bar", figsize=(8,5))

plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Sales")

plt.xticks(rotation=0)

plt.savefig("charts/customer_segment.png")
plt.show()
plt.close()

# ==========================================
# TOP 10 PRODUCTS ANALYSIS
# ==========================================

print("\n========== TOP 10 PRODUCTS ==========\n")

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)

print(top_products.head(10))

top_products.head(10).plot(kind="barh", figsize=(12,6))

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig("charts/top_products.png")
plt.show()
plt.close()
# ==========================================
# MONTHLY SALES TREND
# ==========================================

print("\n========== MONTHLY SALES TREND ==========\n")

# Extract Year-Month
df["Month"] = df["Order Date"].dt.to_period("M")

# Monthly Sales
monthly_sales = df.groupby("Month")["Sales"].sum()

print(monthly_sales)

# Plot
monthly_sales.plot(kind="line", figsize=(12,5), marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)

plt.tight_layout()

plt.savefig("charts/monthly_sales.png")
plt.show()
plt.close()
# ==========================================
# PROFIT ANALYSIS
# ==========================================

print("\n========== PROFIT ANALYSIS ==========\n")

category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

print(category_profit)

category_profit.plot(kind="bar", figsize=(8,5), color="green")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("charts/profit_analysis.png")
plt.show()
plt.close()
# ==========================================
# DISCOUNT IMPACT ANALYSIS
# ==========================================

print("\n========== DISCOUNT IMPACT ANALYSIS ==========\n")

discount_profit = df.groupby("Discount")["Profit"].mean()

print(discount_profit)

discount_profit.plot(kind="line", figsize=(10,5), marker="o")

plt.title("Average Profit by Discount")
plt.xlabel("Discount")
plt.ylabel("Average Profit")

plt.grid(True)

plt.tight_layout()

plt.savefig("charts/discount_analysis.png")
plt.show()
plt.close()
# ==========================================
# TOP 10 CUSTOMERS
# ==========================================

print("\n========== TOP 10 CUSTOMERS ==========\n")

top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False)

print(top_customers.head(10))

top_customers.head(10).plot(kind="barh", figsize=(10,6))

plt.title("Top 10 Customers by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Customer Name")

plt.tight_layout()

plt.savefig("charts/top_customers.png")
plt.show()
plt.close()
# ==========================================
# TOP 10 CITIES ANALYSIS
# ==========================================

print("\n========== TOP 10 CITIES ==========\n")

top_cities = df.groupby("City")["Sales"].sum().sort_values(ascending=False)

print(top_cities.head(10))

top_cities.head(10).plot(kind="barh", figsize=(10,6))

plt.title("Top 10 Cities by Sales")
plt.xlabel("Total Sales")
plt.ylabel("City")

plt.tight_layout()

plt.savefig("charts/top_cities.png")
plt.show()
plt.close()
# ==========================================
# SHIPPING MODE ANALYSIS
# ==========================================

print("\n========== SHIPPING MODE ANALYSIS ==========\n")

shipping = df.groupby("Ship Mode")["Sales"].sum().sort_values(ascending=False)

print(shipping)

shipping.plot(kind="pie", autopct="%1.1f%%", figsize=(7,7))

plt.title("Sales by Shipping Mode")
plt.ylabel("")

plt.savefig("charts/shipping_mode.png")
plt.show()
plt.close()