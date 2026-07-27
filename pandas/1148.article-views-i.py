https://leetcode.com/problems/article-views-i

import pandas as pd 

# - drop_duplicate()
# - sort_values(by='col')
# - rename(columns={'old_col':'new_col'})


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # 1. 필터링 조건 
    condition = views['authoer_id'] == views['viewer_id']
    # 2. 필터링, 컬럼 추출, 중복 제거, 정렬, 이름 변경 한번에 ()
    # 줄바꿈 에러 방지. 코드 아직 안끝났다. 
    result = (views.loc[condition, ['author_id']]
    .drop_duplicates()
    .sort_values(by='author_id')
    .rename(columns={'author_id': 'id'})
    )
    return result