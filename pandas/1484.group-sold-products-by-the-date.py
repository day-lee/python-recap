https://leetcode.com/problems/group-sold-products-by-the-date

- 애그함수: agg(새로운 열 이름 = (기존 열, 함수))
- 집계함수는 그룹바이와 단짝. 그룹바이로 데이터 쪼개고, 애그로 뭉쳐서 계산함 
- 람다의 인수로 보내는 x는 시리즈(열)이고, 이를 sorted() 함수에서 오름차순 정렬한 뒤 ','.join()으로 문자열로 다시 조합해줌 
- 시리즈는 리스트로 이해하면 된다. 리스트 함수 sorted()를 쓸 수 있는 이유. 
- 람다 함수를 쓴 이유는 체이닝해서 여러 메소드를 연결하기 위함. 

import pandas as pd

# 그룹화 먼저 한 뒤 람다 함수로 유니크 정렬
def categorize_products_1(activities: pd.DataFrame) -> pd.DataFrame:
    r= activities.groupby(by='sell_date', as_index=False).agg(
        num_sold=('product', 'nunique'),
        products=('product', lambda x: ','.join(sorted(x.nunique())))
    )
    return r.sort_values(by='sell_date')


# 중복 제거, 정렬 먼저 한 뒤, 문자열로 join해주기 
def categorize_products_2(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.drop_duplicates().sort_values(by=['sell_date', 'product'])

    result = df.groupby('sell_date').agg(
        num_sold=('product', 'count'),
        products=('product', ','.join) 
    ).reset_index() 

    return result