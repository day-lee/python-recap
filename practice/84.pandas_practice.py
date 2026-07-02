
"""
You are provided with a CSV file named sales_data_missing. csv containing detailed sales information.

 Your task is to:
1. Replace missing values in the promotion_id column with "No Promotion" string.
2. Calculate the total sales for a specific product _id in a given month. 

3. Add a column for each month's total sales to the dataset. 

4. There are only two months present in the data; 

5. order these columns in ascending order by month number. If there were no sales, fill the column with "0.0".

Ensure the final dataset contains only order_id, product_id, promotion_1d, and the monthly total sales columns.

loading 
Return the cleaned dataset as a NumPy array.

Example Input:
order_id, product_id, promotion_id, currency, order_value, order_date, origin, order_value_column 1,100,, USD,278.77,2021-01-01,0ffline, 2124.86
2,200, PROMO_2,, 130.73, 2021-01-02, OnLine, 4283.22
3,200,, 112.01,112.01, 2021-02-04,Direct, 1055.08
4,200,, 112.01,112.01,2021-02-03,Direct, 1055.08

Example Output:
It1 200 "No Promotion' 2124,86 0.0] [2 200 *PROMO_2'4283.22 2110.16] [3 200 No Promotion* 4283.22 2110.16]
[4 200 *No Promotion' 4283.22 2110.16)]
"""

import pandas as pd
import numpy as np 

import os 
# print(os.getcwd())
# ./orders_codebar.csv
csv_dir = r"/Users/dayeonlee/Documents/Projects/26/python-recap/practice/orders_codebar.csv"
csv_data = pd.read_csv(csv_dir)
# print(type(csv_data))
# pd.
# fillna
csv_data['promotion_id'] = csv_data['promotion_id'].fillna("No Promotion", inplace=False)
# csv_data['promotion_id'].fillna("No Promotion", inplace=True)

# print(csv_data)
# import sys 
# print(dir(sys))
# print(sys.version)

# Calculate the total sales for a specific product _id in a given month. 

csv_data['order_date'] = pd.to_datetime(csv_data['order_date'])
# csv_data['month'] = csv_data['order_date'].apply(lambda x:x.month)
csv_data['month'] = csv_data['order_date'].dt.month
# print(dir(csv_data['order_date'].dt))
# print(csv_data)

sales_df = csv_data.pivot_table(values='order_value', index='product_id', columns='month', aggfunc='sum', fill_value=0.0)

print(sales_df)