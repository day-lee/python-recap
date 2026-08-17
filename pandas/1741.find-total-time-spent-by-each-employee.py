https://leetcode.com/problems/find-total-time-spent-by-each-employee

#  SQL이라면 그룹바이 event_day, emp_id 해서 전체 sum(out_time) - sum(in_time) 할듯  
select emp_id, event_day,  (sum(out_time) - sum(in_time)) as total
from employees
group by event_day, emp_id


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
  
    # 1. total 계산된 컬럼을 원본 df에 추가 
    employees['total_time'] = employees['out_time'] - employees['in_time']

    # 2. 기준대로 그룹핑: DataFrameGroupBy 객체 상태, 주소 값에 집계 함수 붙이면 계산 결과 볼 수 있음 -> 시리즈 
    group_series = employees.groupby(['event_day', 'emp_id'])['total_time'].sum()

    # 3. reset_index()로 df로 변환: event_day, emp_id는 컬럼이 아니라 시리즈의 멀티 인덱스 상태임 
    return group_series.reset_index().rename(columns={'event_day':'day'})


=========================================================================== 
"""
- 멀티 인덱스
event_day   emp_id
2020-11-28  1         173
            2          30
2020-12-03  1          41
2020-12-09  2          27
Name: total_time, dtype: Int64
------------------------------
- 데이터프레임
         day  emp_id  total_time
0 2020-11-28       1         173
1 2020-11-28       2          30
2 2020-12-03       1          41
3 2020-12-09       2          27
"""

- groupby에 "as_index=False" 인자를 주면 reset_index()를 안해도 됨.

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    result = employees.groupby(["event_day", "emp_id"], as_index = False)["total_time"].sum().rename(columns={"event_day":"day"})
    return result