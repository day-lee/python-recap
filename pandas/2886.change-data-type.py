https://leetcode.com/problems/change-data-type


- 판다스는 기본적으로 원본을 파괴하지 않고 새 객체를 반환한다. 
- 원본을 바꾸려면 df = df... 처럼 재할당하거나 inplace=True를 써야 한다.

- astype() 함수는 원본 데이터프레임을 직접 수정하지 않고, 데이터 형식이 변경된 '새로운 데이터프레임'을 복사해서 반환
- 따라서 원본에 대입해줘야함.

import pandas as pd 

def change_data_type(students: pd.DataFrame) -> pd.DataFrame:   
    students["grade"] = students["grade"].astype("int32")
    return students 

