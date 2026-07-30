https://leetcode.com/problems/fix-names-in-a-table

- str manipulation
- Series.str.slice(start=1) 슬라이싱
- Series.str.upper() 대문자
- s.str.capitalize() 슬라이싱 할 것도 없이 바로 첫 대문자+소문자 조합으로 만들어줌 


import pandas as pd 

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.slice(stop=1).str.upper() + users['name'].str.slice(start=1).str.lower() 

    return users[['user_id', 'name']].sort_values(by='user_id')

# str.capitalize()
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # 갱신: 원본에 새로운 값 대입하는 조작
    users['name'] = users['name'].str.capitalize() 

    # 위에서 이미 원본 데이터 직접 수정됨.
    return users.sort_values(by='user_id')

# df.assign() 원본 변경하지 않고, 복사하여 새 데이터프레임 반환
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    return users.assign(name=users['name'].str.capitalize()).sort_values(by='user_id')