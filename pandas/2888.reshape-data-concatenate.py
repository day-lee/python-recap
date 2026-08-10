https://leetcode.com/problems/reshape-data-concatenate

- UNION ALL: 중복 허용 
    pd.concat([df1, df2], ignore_index=True) 
    -> 새로운 인덱스 번호를 추가해줌 
- UNION DISTINCT: 중복 제거 
    pd.concat([df1, df2], ignore_index=True).drop_duplicates() 

- 컬럼명이 일치할 땐 vertically 쌓임
- 컬럼명이 다를 때 모든 컬럼을 유지하고 결측치 NaN로 채움 
- 공통 컬럼만 남기고 싶다면 join='inner' 옵션 
    
import pandas as pd

def reshape(df1: pd.DataFrame, df2:pd.DataFrame)-> pd.DataFrame:
    result = pd.concat([df1, df2])
    return result