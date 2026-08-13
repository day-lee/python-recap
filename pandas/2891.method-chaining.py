https://leetcode.com/problems/method-chaining

- sort_values()는 by로 기준을 정해준다. order by 처럼. 정렬은 ascending에 True, False를 넣어준다. 

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # filtered_animals = animals[animals['weight'] > 100]
    condition = animals['weight'] > 100 
    result = animals.loc[condition].sort_values(by=['weight'], ascending=False)
    return result[['name']]