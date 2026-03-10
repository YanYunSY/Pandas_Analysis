#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
"""
Pandas 数据分析实战训练营
涵盖：数据探查→清洗→特征工程→筛选→分组聚合→多表合并
适用场景：电商销售数据清洗与分析
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===================== 0. 环境配置 & 数据加载 =====================
# 中文显示配置
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 销售流水表（脏数据）
sales_data = {
    'OrderID': ['1001', '1002', '1003', '1004', '1005', '1001', '1006', '1007'],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-01', '2023-01-05', '2023-01-06'],
    'CustomerID': ['C10', 'C11', 'C11', 'C12', 'C13', 'C10', 'C14', 'C15'],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop', 'Laptop', 'Desk', 'Chair'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics', 'Electronics', 'Furniture', 'Furniture'],
    'Price': [5000, 100, 250, 1500, np.nan, 5000, 800, 300],
    'Quantity': [1, np.nan, 2, 1, 1, 1, 2, 4]
}
df_sales = pd.DataFrame(sales_data)

# 2. 客户维表（干净数据）
customer_data = {
    'CustomerID': ['C10', 'C11', 'C12', 'C13', 'C14'],
    'City': ['Beijing', 'Shanghai', 'Shanghai', 'Shenzhen', 'Guangzhou'],
    'VIP_Level': ['Gold', 'Silver', 'Gold', 'Bronze', 'Silver']
}
df_customers = pd.DataFrame(customer_data)

# ===================== 第一关：数据探查与概览 =====================
print("===== 第一关：数据探查 =====")
# 查看前5行
print("1. df_sales 前5行：")
print(df_sales.head())

# 基本信息（列名、非空值、数据类型）
print("\n2. df_sales 基本信息：")
df_sales.info()

# 缺失值统计
print("\n3. 缺失值统计：")
print(df_sales.isnull().sum())

# ===================== 第二关：数据清洗 =====================
print("\n===== 第二关：数据清洗 =====")
# 1. 剔除完全重复行（修改原表）
df_sales.drop_duplicates(keep='first', inplace=True)
print(f"1. 去重后数据行数：{len(df_sales)}")

# 2. 处理空值（无警告写法）
df_sales['Quantity'] = df_sales['Quantity'].fillna(1)  # 数量空值填1
price_median = df_sales['Price'].median()
df_sales['Price'] = df_sales['Price'].fillna(price_median)  # 价格空值填中位数
print(f"2. 空值处理后缺失值统计：\n{df_sales.isnull().sum()}")

# ===================== 第三关：特征工程 =====================
print("\n===== 第三关：特征工程 =====")
# 1. 日期格式转换
df_sales['Date'] = pd.to_datetime(df_sales['Date'])
print(f"1. Date列类型转换后：{df_sales['Date'].dtype}")

# 2. 创建订单总金额列
df_sales['Total_Amount'] = df_sales['Price'] * df_sales['Quantity']
print("2. 新增Total_Amount列后前5行：")
print(df_sales[['OrderID', 'Price', 'Quantity', 'Total_Amount']].head())

# ===================== 第四关：多条件筛选 =====================
print("\n===== 第四关：多条件筛选 =====")
# 筛选：总金额≥1000 且 类别=Electronics
condition1 = df_sales['Total_Amount'] >= 1000
condition2 = df_sales['Category'] == 'Electronics'
filtered_df = df_sales[condition1 & condition2]
print(f"1. 符合条件的记录数：{len(filtered_df)}")
print("2. 筛选结果：")
print(filtered_df[['OrderID', 'Category', 'Total_Amount']])

# ===================== 第五关：分组聚合 =====================
print("\n===== 第五关：分组聚合 =====")
# 按分类统计总销售额、平均客单价（汇报友好版）
category_agg = df_sales.groupby('Category')['Total_Amount'].agg(
    总销售额='sum',
    平均客单价='mean'
).reset_index().sort_values(by='总销售额', ascending=False)
# 金额格式化
category_agg['总销售额'] = category_agg['总销售额'].round(2)
category_agg['平均客单价'] = category_agg['平均客单价'].round(2)
print("1. 按分类统计（降序）：")
print(category_agg)

# ===================== 第六关：多表合并 =====================
print("\n===== 第六关：多表合并 =====")
# 左连接：销售表 + 客户表
df_final = pd.merge(
    left=df_sales,
    right=df_customers,
    on='CustomerID',
    how='left'
)
print("1. 合并后最终表前7行（关键列）：")
print(df_final[['OrderID', 'CustomerID', 'Total_Amount', 'City', 'VIP_Level']])
print(f"2. 未匹配到客户信息的记录数：{df_final['City'].isnull().sum()}")

# ===================== 最终结果导出（可选） =====================
# 导出为Excel，方便汇报
df_final.to_excel('sales_analysis_result.xlsx', index=False)
print("\n✅ 分析完成！结果已导出为 sales_analysis_result.xlsx")

