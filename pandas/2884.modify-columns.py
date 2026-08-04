https://leetcode.com/problems/modify-columns

- 원본 salary 컬럼의 값을 변경하기 
- Reassign the column to update its original values 

import pandas as pd

def modifiy_col(employees:pd.DataFrame) -> pd.DataFrame:

   1. employees['salary'] = employees['salary'] * 2 

   2. employees['salary'] *= 2 

   3. employees.loc[:, 'salary'] = employees['salary'] * 2

    return employees