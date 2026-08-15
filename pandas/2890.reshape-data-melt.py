https://leetcode.com/problems/reshape-data-melt

- melt는 unpivoting이라고도 불리며, wide 리포트 형식을 long DB 형식으로 변환할 때 사용
- 공식 문서 전혀 이해가 안됨.. 이 포스트 참고 https://www.datacamp.com/tutorial/pandas-melt 

- pd.melt(df, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)

id_vars, value_vars: id_vars 만 지정하고, value_vars를 생략하면, id_vars 제외 모든 칼럼을 대상으로 하게 됨 
var_name, value_name 

"""
frame: The DataFrame to reshape. Only required when using pandas.melt().
    - dataframe을 명시 
id_vars: Column or list of columns to keep unchanged. These columns identify each row after reshaping.
    - 변하지 않을 컬럼. 기준
value_vars: Column or list of columns to unpivot. If omitted, pandas melts all columns that are not in id_vars.
    - melt 해서 세로로 쌓을 컬럼 이름들 리스트에 나열 
    
var_name: Name of the new column that stores the original column names. Defaults to ”variable” if not specified.
    - 새롭게 만들어질 컬럼 이름. melt 해서 세로로 쌓인 컬럼 이름이 들어감. 기본값은 variable
value_name: Name of the new column that stores the values. Defaults to ”value” if not specified.
    - 각자 컬럼으로 존재하다가 melt되어서 값으로 들어가다보니, 해당 컬럼에 값에 새로 컬럼 이름을 붙여줘야함. 

col_level: Optional, specifies which level to melt when working with MultiIndex columns.
ignore_index: If True (default), creates a new sequential index. If False, preserves the original index.
"""

import pandas as pd 

def melt_table(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars='product', value_vars= ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], var_name='quarter', value_name='sales')

Input:
+-------------+-----------+-----------+-----------+-----------+
| product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella    | 417       | 224       | 379       | 611       |
| SleepingBag | 800       | 936       | 93        | 875       |
+-------------+-----------+-----------+-----------+-----------+
Output:
+-------------+-----------+-------+
| product     | quarter   | sales |
+-------------+-----------+-------+
| Umbrella    | quarter_1 | 417   |
| SleepingBag | quarter_1 | 800   |
| Umbrella    | quarter_2 | 224   |
| SleepingBag | quarter_2 | 936   |
| Umbrella    | quarter_3 | 379   |
| SleepingBag | quarter_3 | 93    |
| Umbrella    | quarter_4 | 611   |
| SleepingBag | quarter_4 | 875   |
+-------------+-----------+-------+

