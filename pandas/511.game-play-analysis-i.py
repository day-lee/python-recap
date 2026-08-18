https://leetcode.com/problems/game-play-analysis-i

# Write your MySQL query statement below
# with rn_table as (
# select 
# *, row_number() over(partition by player_id order by event_date asc) rn
# from activity)

# select player_id, event_date as first_login
# from rn_table
# where rn=1

- DataFrameGroupby 객체에 ['event_date']를 붙여서, 앞으로의 집계는 이 컬럼만 대상으로 하겠다고 명시해줌 
- .min()은 아무 인자도 받지 않음 
- columnar 관점에서 player_id 컬럼을 기준축으로 잡고, event_date를 연산 대상으로 잡아서 메모리에서 다른 컬럼은 제외됨. 
- .groupby의 'as_index=False'는 기준 컬럼을 인덱스로 보내지 말고 일반 컬럼으로 둬. 라는 뜻임 
- 결론적으로 두 컬럼만 남음.

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    r = activity.groupby('player_id', as_index=False)['event_date'].min().rename(columns={'event_date': 'first_login'})
    return r