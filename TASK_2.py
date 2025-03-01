import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

file_path = "C:\python\shodow_fox\Sample - Superstore.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

df.head()
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Month'] = df['Order Date'].dt.to_period("M").astype(str)
df.fillna(0, inplace=True)

sales_trend = df.groupby('Month')['Sales'].sum().reset_index()
px.line(sales_trend, x='Month', y='Sales', title='Monthly Sales Trend').show()

category_sales = df.groupby(['Category', 'Sub-Category'])['Sales'].sum().reset_index()
px.bar(category_sales, x='Category', y='Sales', color='Sub-Category', title='Category Sales Analysis').show()

profit_trend = df.groupby('Month')['Profit'].sum().reset_index()
px.line(profit_trend, x='Month', y='Profit', title='Monthly Profit Trend').show()

segment_profit = df.groupby('Segment')['Profit'].sum().reset_index()
px.bar(segment_profit, x='Segment', y='Profit', title='Profit by Customer Segment').show()

df['Sales_to_Profit_Ratio'] = df['Sales'] / (df['Profit'] + 1e-6)
segment_ratio = df.groupby('Segment')['Sales_to_Profit_Ratio'].mean().reset_index()
px.bar(segment_ratio, x='Segment', y='Sales_to_Profit_Ratio', title='Sales-to-Profit Ratio by Segment').show()

print("✅ Store Sales and Profit Analysis Completed Successfully!")

most_profitable_product = df.groupby('Product Name')['Profit'].sum().reset_index()
most_profitable_product = most_profitable_product.sort_values(by='Profit', ascending=False).iloc[0]

print("✅ Store Sales and Profit Analysis Completed Successfully!")
print(f"\n🔥 The Most Profitable Product is: **{most_profitable_product['Product Name']}**")
print(f"💰 Total Profit: ${most_profitable_product['Profit']:.2f}")
