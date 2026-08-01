https://leetcode.com/problems/drop-duplicate-rows

- DISTINCT 
- drop_duplicates(subset=['col_name'])


import pandas as pd 

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'])
