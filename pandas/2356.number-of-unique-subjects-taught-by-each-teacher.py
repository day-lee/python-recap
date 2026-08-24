https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher

1단계
- 그룹바이는 방만 배정해준다. 데이터를 실제로 합치거나 계산하지 않음. DataFrameGroupBy 객체 상태 
- as_index=False는 나중에 계산 결과가 나왔을 때 방 번호를 행 인덱스로 쓰지 말고 일반 데이터 컬럼으로 놔두라는 의미 
    -> groupby의 디폴트 행동은 기준 컬럼을 행 인덱스로 밀어버리려고함 
     - 인덱스를 붙이면 데이터 조회가 쉬울거라고 짐작해서 판다스는 빠른 연산을 위해 자동으로 인덱싱 해버림. 
""" groupby에만 존재하는 as_index 인자 | (다른 함수에서는 항상 .reset_index())
as_index=True
            subject_id  <-- subject_id는 일반 컬럼
teacher_id              <-- teacher_id는 아래로 툭 떨어진 '인덱스' 라벨 구역
1                    3
2                    4

as_index=False 
   teacher_id  subject_id  <-- 둘 다 정당한 일반 데이터 컬럼!
0           1           3  <-- 인덱스는 판다스가 주는 기본 숫자(0, 1, 2...)가 채움
1           2           4
"""
2단계
- 그룹마다 수많은 컬럼 데이터가 들어있는데, 그 중 ["subject_id"] 지정해서 이 컬럼으로 좁히는 단계
- SeriesGroupBy 객체로 바뀜 
- .nunique()로 실제 연산을 진행함. 그룹바이에서 쪼개놓은 방에서 2단계에서 고른 subject_id를 확인한다. 
- number of unique: 중복 제거한 개수 세라. 
- 데이터프레임 리턴함 


import pandas as pd
def count_unique_subjects_1(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.groupby(by='teacher_id')['subject_id'].nunique().reset_index().rename(columns={'subject_id':'cnt'})
    
def count_unique_subjects_2(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.groupby(by=["teacher_id"], as_index=False)["subject_id"].nunique().rename(columns={"subject_id":"cnt"})

def count_unique_subjects_production(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.groupby(by=["teacher_id"], as_index=False).agg(
        cnt=('subject_id', 'nunique')  # 집계와 컬럼명 변경을 동시에 해결
    )
