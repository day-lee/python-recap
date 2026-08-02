https://leetcode.com/problems/display-the-first-three-rows

Pandas, comparison with SQL
https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html

Intro - 10 minutes to pandas
https://pandas.pydata.org/docs/user_guide/10min.html#min

- SQL equivalent: LIMIT 3

import pandas as pd 

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)