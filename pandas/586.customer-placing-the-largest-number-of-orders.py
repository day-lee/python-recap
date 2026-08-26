https://leetcode.com/problems/customer-placing-the-largest-number-of-orders

import pandas as pd

# idxmax()는 series에서 가장 큰 값의 index를 반환
def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby(by='customer_number', as_index=False).count()
    max_idx = df['order_number'].idxmax() 
    return df.loc[[max_idx], ['customer_number']]



# 최빈값 찾아주는 함수 mode()
def largest_orders_2(orders: pd.DataFrame) -> pd.DataFrame:
    # return orders[['customer_number']].mode()
    return pd.DataFrame(orders['customer_number'].mode())