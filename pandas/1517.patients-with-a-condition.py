https://leetcode.com/problems/patients-with-a-condition

- regex ( | ) 캡쳐 그룹 사용
- \s는 스페이스 포함 모든 공백임(\t \n ...) 만약 한칸만 지정하고 싶다면 그냥 빈칸(스페이스) 줘야함 
- df.loc[] or df[col]: they handle the underlying memory differently. Best practice is to use df.loc[] 

import pandas as pd

def find_patients(patients:pd.DataFrame) -> pd.DataFrame:
    regex = r"(^|\s)DIAB1"
    condition = patients['conditions'].str.contains(regex, regex=True)
    return patients.loc[condition, ["patient_id","patient_name","conditions"]]


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    condition = patients["conditions"].str.contains(r"(^| )DIAB1")
    return patients[condition]  #조건식 바로 넣어도 나오네, 내부적으로 TF 매핑해서 남은 로우만 리턴해줌   


