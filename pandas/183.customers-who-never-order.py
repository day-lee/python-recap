https://leetcode.com/problems/customers-who-never-order

import pandas as pd

"""
LEFT JOIN 후 IS NULL 필터링 
JOIN: .merge()
IS NULL: .isna()
컬럼 alias: .rename(columns={'name': 'Customers'})
"""

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # .merge(table to merge with, how- inner, left..., on - 컬럼이 같은 이름일 때만, left_on, right_on)
    joined = customers.merge(orders, how='left', left_on='id', right_on='customerId')
    # .isna()는 행 null 여부를 불리언으로 반환한다. 
    condition = joined['customerId'].isna()
    # loc[] 불리언 인덱싱, 컬럼 선택하고 rename()으로 이름 바꿔주기 
    result = joined.loc[condition, ['name']].rename(columns={'name': 'Customers'})
    return result

"""
판다스에서 성능과 메모리상 권장 
.isin()은 테이블 합치지 않고도 값만 비교할 수 있어 메모리 아낌 
.isin()은 T/F 시리즈를 만들어냄 
불리언 인덱싱: df[조건식]

NOT IN 서브쿼리 문법과 동일함 

SELECT name AS Customers 
FROM customers 
WHERE id NOT IN (SELECT customerId FROM orders);

단점: Chained Indexing이 일어남 
df[...]로 필터링을 하고, 그 결과에서 df[['name']] 컬럼을 추출하는 2단계 작업으로 복사복인지 원본인지 헷갈려서 SettingWithCopyWarning이 나올 수 있는 구조

"""
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers['id'].isin(orders['customerId'])]
    return df[['name']].rename(columns={'name':'Customers'})


"""
모범 답안 
df.loc[]은 판다스에서 권장하는 행, 열을 동시에 선택하는 방식. 
df.loc[행_조건, [열_선택]]: 이 조건에 맞는 행 중에, name 컬럼만 가져와라. 
SettingWithCopyWarning에서 안전함. 
"""
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame: 
    condition = (~customers['id'].isin(orders['customerId'])) 
    result = customers.loc[condition, ['name']].rename(columns={'name': 'Customers'})
    return result 

