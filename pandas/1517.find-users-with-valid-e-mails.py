https://leetcode.com/problems/find-users-with-valid-e-mails

- pandas에서 정규표현식 Series.str.contains(regex_expression, regex=True) 
- True/False 시리즈를 리턴한다. 
- regex에서 . 점 하나는 아무 문자나 하나를 의미하므로 백슬래시와 써서 점인걸 확실히 표현해줘야한다. \.


import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    regex_pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    condition = users['mail'].str.contains(regex_pattern, regex=True, na=False) 
    return users.loc[condition, ['user_id', 'name', 'mail']]