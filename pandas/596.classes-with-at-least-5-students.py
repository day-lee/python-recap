https://leetcode.com/problems/classes-with-at-least-5-students

- 조건부 집계

import pandas as pd 

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby(by='class', as_index=False).agg(total=('student', 'count'))
    return df.loc[df['total']>=5, ['class']]


def find_classes_2(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby(by='class', as_index=False).count()
    return df.loc[df['student']>=5, ['class']]