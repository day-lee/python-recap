https://leetcode.com/problems/invalid-tweets

- len(df)하면 행 수가 나옴
- df.shape: (행 수, 열 수)가 나옴
- df.size: 전제 요소 개수 (데이터 있는지 없는지 확인, 결측치 비율 구할 때 사용)

- 특정 컬럼 안의 데이터(스트링 값) 접근하려면 Pandas.Series.str 
- str.len()

import pandas as pd 

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame: 
    invalid_condition = tweets['content'].str.len() > 15
    return tweets.loc[invalid_condition, ['tweets_id']]