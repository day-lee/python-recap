https://leetcode.com/problems/get-the-size-of-a-dataframe

- df.shape 데이터프레임 사이즈 확인
- 튜플 형태로 (행 개수, 열 개수) 반환 
"""
df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4], "col3": [5, 6]})
df.shape
(2, 3)
"""
import pandas as pd 

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)