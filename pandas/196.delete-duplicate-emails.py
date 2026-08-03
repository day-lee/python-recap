https://leetcode.com/problems/delete-duplicate-emails

# inplace=True를 사용할 때는 체이닝 하지말고 한 단계씩 줄을 나눠서 실행해야함 
# drop_duplicates()의 keep='first' 인자는 처음 나타나는 값만 남겨둠 
# inplace=True를 사용하면 기존의 df를 수정하므로 return 하지 않아도 됨. 

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', ascending=True, inplace=True)
    person.drop_duplicates(subset=["email"], keep='first', inplace=True)