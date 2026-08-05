import pandas as pd 

- columns를 rename한다.
- df.columns는 컬럼 이름을 가지고 있다. 
- 판다스는 row labels, column labels 행 이름, 열 이름을 모두 색인으로 처리함 
열 이름 인덱스 객체: Index(['id', 'first', 'last', 'age'], dtype='object')

- df.rename()은 복사본을 만든다.
def rename_columns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={'id':'student_id', 'first':'first_name', 'last':'last_name', 'age':'age_in_years'})

- df.columns는 원본을 덮어쓴다. 
def reanme_columns(students: pd.DataFrame) -> pd.DataFrame:
    students.columns = ["student_id", "first_name", "last_name", "age_in_years"] 
    return students 