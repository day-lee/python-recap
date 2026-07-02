"""
You are provided with a CSV file named sales_data_missing. csv containing detailed sales information.

 Your task is to:
1. Replace missing values in the promotion_id column with "No Promotion" string.
2. Calculate the total sales for a specific product _id in a given month. 

3. Add a column for each month's total sales to the dataset. 
There are only two months present in the data; 

4. order these columns in ascending order by month number. If there were no sales, fill the column with "0.0".

5. Ensure the final dataset contains only order_id, product_id, promotion_1d, and the monthly total sales columns.

loading 
6. Return the cleaned dataset as a NumPy array.

Example Input:
order_id, product_id, promotion_id, currency, order_value, order_date, origin, order_value_column 
1,100,, USD,278.77,2021-01-01,0ffline, 2124.86
2,200, PROMO_2,, 130.73, 2021-01-02, OnLine, 4283.22
3,200,, 112.01,112.01, 2021-02-04,Direct, 1055.08
4,200,, 112.01,112.01,2021-02-03,Direct, 1055.08

Example Output:
It 1 200 "No Promotion' 2124,86 0.0] [2 200 *PROMO_2'4283.22 2110.16] [3 200 No Promotion* 4283.22 2110.16]
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

#TODO 1. Replace missing values in the promotion_id column with "No Promotion" string.
"""
df.fillna() inplace=False 복사복 만들어서 반환하기 때문에 좌변 csv_data['promotion_id']에 넣어줘야함 (실무 방식) / True 원본 수정인데 쓰지말기 
"""
csv_data['promotion_id'] = csv_data['promotion_id'].fillna("No Promotion", inplace=False)
# csv_data['promotion_id'].fillna("No Promotion", inplace=True)

# print(csv_data)
# import sys 
# print(dir(sys))
# print(sys.version)

#TODO 2. Calculate the total sales for a specific product _id in a given month. 
"""
dataframe은 2차원 테이블 클래스 
series는 1차원 column 클래스 
type(csv_data['order_date'][0] 단 한개의 스칼라 값 
.dt 는 데이트타임 accessor: 데이터를 날짜/시간으로 형변환 
pivottable은 데이터 그룹화, 내부적으로는 groupby를 거쳐서 만들어짐. 시각적 보고서 확인용 
"""
csv_data['order_date'] = pd.to_datetime(csv_data['order_date'])
# print(type(csv_data['order_date'])) #<class 'pandas.Series'>
# print(type(csv_data['order_date'][0])) #<class 'pandas.Timestamp'>
# csv_data['month'] = csv_data['order_date'].apply(lambda x:x.month)
csv_data['month'] = csv_data['order_date'].dt.month
# print(dir(csv_data['order_date'].dt))
# print(csv_data)

sales_df = csv_data.pivot_table(values='order_value', index='product_id', columns='month', aggfunc='sum', fill_value=0.0)
# sales_df = csv_data.pivot_table(values='order_value', columns='product_id', index='month', aggfunc='sum', fill_value=0.0)
print(sales_df)

#TODO 3. Add a column for each month's total sales to the dataset. There are only two months present in the data; 
"""
2번 피봇데이블에서 각 월 총 sum() 구하기 
기존 month 컬럼 값 보고 csv_data['month_sales'] 만들어줌 
=> 두 단계, 매출 구하기 + 매핑하기 

groupby() 와 transform() 쓰면 한줄로 가능 

"""
# month_sales = csv_data.groupby('month')['order_value'].sum() 
# # csv_data['month_sales'] = csv_data.groupby('month')['order_value'].sum() # 전체 매핑이 안되어있음 
# csv_data['month_total_sales_map'] = csv_data['month'].map(month_sales)

# SQL select sum(order_value) .. group by month 
csv_data['month_total_sales_transform'] = csv_data.groupby('month')['order_value'].transform('sum')
# # print(csv_data)

#TODO 4. order these columns in ascending order by month number. If there were no sales, fill the column with "0.0".
csv_data['month_total_sales_transform'] = csv_data['month_total_sales_transform'].fillna(0.0)
csv_data = csv_data.sort_values(by='month', ascending=True)
# print(csv_data)

#TODO 5. Ensure the final dataset contains only order_id, product_id, promotion_1d, and the monthly total sales columns.
"""
df.copy()는 데이터프레임 view 얕은 복사본을 만든다. - 새로운 인스턴스 만드는 것 아님!
"""
# selected_cols = ['order_id', 'product_id', 'promotion_id', 'month_total_sales_transform']
# final_data = csv_data[selected_cols].copy() 
final_data = csv_data[['order_id', 'product_id', 'promotion_id', 'month_total_sales_transform']].copy()

# print(final_data)

#TODO 6. Return the cleaned dataset as a NumPy array.
"""
numpy는 파이썬리스트가 겹겹이 쌓인 형태 
"""
final_np = final_data.to_numpy()
print(final_np, type(final_np)) # <class 'numpy.ndarray'>
