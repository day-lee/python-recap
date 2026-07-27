https://leetcode.com/problems/create-a-dataframe-from-list

- pd.DataFrame()의 인자로 data, index, columns 등이 있다.
- data는 2차원 배열, index는 행 이름, columns는 열 이름을 의미한다.

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # pd.DataFrame()은 nested list를 한번에 df로 바꿔준다. 
    cols = ["student_id", "age"]
    return pd.DataFrame(data=student_data, columns=cols)


# nested list를 이용해 DataFrame을 생성하는 예시
student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

"""
Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
"""