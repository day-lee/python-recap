https://leetcode.com/problems/fill-missing-data

- fillna() 
- 시리즈 선택해서 fillna() 적용하고, 기존의 시리즈에 할당해서 원본 변경함 

import pandas as pd 

def fill_na(products:pd.DataFrame) -> pd.DataFrame:
    1. re-assign: products['quantity'] = products['quantity'].fillna(0)
    2. overwrite: products['quantity'].fillna(0, inplace=True)
    return products