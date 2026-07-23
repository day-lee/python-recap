https://leetcode.com/problems/big-countries


1. 다중 조건 인덱싱 boolean index with multiple conditions
# 가독성을 위해 쪼개서 작성 

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # 조건 변수를 만듦 (조건식) or (조건식)
    big_condition = (world['area'] >= 3000000 ) | ( world['population'] >= 25000000)
    # df[조건식]을 변수로 분리함. 만족하는 로우들만 df 형태로 하나의 변수에 저장 
    big_df = world[big_condition]
    # 필터링 된 결과 df에서 원하는 열만 출력
    result = big_df[['name', 'population', 'area']]
    return result


2. loc[]이용 인덱싱