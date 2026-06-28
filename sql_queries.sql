-- View All Data
SELECT * FROM Orders;

-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM Orders;

-- Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM Orders;

-- Total Orders
SELECT COUNT(DISTINCT [Order ID]) AS Total_Orders
FROM Orders;

-- Total Customers
SELECT COUNT(DISTINCT [Customer ID]) AS Total_Customers
FROM Orders;

-- Sales by Category
SELECT Category, SUM(Sales) AS Total_Sales
FROM Orders
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Profit by Category
SELECT Category, SUM(Profit) AS Total_Profit
FROM Orders
GROUP BY Category
ORDER BY Total_Profit DESC;

-- Sales by Region
SELECT Region, SUM(Sales) AS Total_Sales
FROM Orders
GROUP BY Region
ORDER BY Total_Sales DESC;

-- Sales by Segment
SELECT Segment, SUM(Sales) AS Total_Sales
FROM Orders
GROUP BY Segment
ORDER BY Total_Sales DESC;

-- Top 10 Products
SELECT [Product Name], SUM(Sales) AS Total_Sales
FROM Orders
GROUP BY [Product Name]
ORDER BY Total_Sales DESC
LIMIT 10;

-- Top 10 Customers
SELECT [Customer Name], SUM(Sales) AS Total_Sales
FROM Orders
GROUP BY [Customer Name]
ORDER BY Total_Sales DESC
LIMIT 10;

-- Average Discount
SELECT AVG(Discount) AS Average_Discount
FROM Orders;

-- Monthly Sales
SELECT MONTH([Order Date]) AS Month,
       SUM(Sales) AS Total_Sales
FROM Orders
GROUP BY MONTH([Order Date])
ORDER BY Month;