https://leetcode.com/problems/calculate-special-bonus

- df.loc[조건식, 열] 방식

-  "조건이 True인 행의 bonus 방에만 동일한 행의 salary 값을 대입하고, False인 행은 기존 값을 보존해라"라는 판다스의 가장 강력하고 표준적인 데이터 업데이트 방식
- 결측치는 결과에 붙여줌. 

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # id가 홀수 & str.'M'으로 시작 안함
    bonus_condition = (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith("M"))

    # df.loc[조건, 열]으로 보너스 조건에 맞는 T/F "시리즈"가 나오면, 거기에 employees['salary'] 시리즈를 대입해서 T에만 값을 넣어줌
    employees.loc[bonus_condition, 'bonus'] = employees['salary']

    return employees[['employee_id', 'bonus']].fillna(0).sort_values(by='employee_id')



- np.where(조건문, T만족시 값, F불만족시 값) 
- np.where은 파이썬 for 돌지않고 C언어 연산엔진으로 성능이 빠르다. 

import numpy as np

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    bonus_condition = (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith("M"))

    # 조건 만족하면 salary 넣고, 아니면 0
    employees['bonus'] = np.where(bonus_condition, employees['salary'], 0)

    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')