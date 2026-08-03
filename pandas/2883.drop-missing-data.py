https://leetcode.com/problems/drop-missing-data

- seriese.notna() 는 필터링해서 조회
- df.drop_na(subset=['name'])는 실제로 제거함

import pandas as pd

def drop_missing_data(students:pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])


import pandas as pd 
def drop_missing_data(students:pd.DataFrame) -> pd.DataFrame:
    return students[students['name'].notna()]