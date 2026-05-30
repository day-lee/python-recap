"""
[미니 프로젝트: 글로벌 리뷰 데이터 태깅 및 정제]

상황:
글로벌 가전 쇼핑몰의 백엔드 엔지니어로서, 여러 국가에서 수집된 제품 리뷰 데이터를 정제해야 합니다.
리뷰 텍스트의 공백을 제거하고, 평점 데이터를 검증하여 특정 조건에 맞는 유저의 ID만 추출하는 시스템입니다.

미션:
1. 메인 함수 구현 (`clean_and_tag_reviews`)
   - 이 함수는 위치 가변 인자(`*args`)로 유저 ID(문자열)들을 순서대로 받습니다.
   - 키워드 가변 인자(`**kwargs`)로 '유저ID=리뷰텍스트' 형태의 딕셔너리 데이터를 받습니다.
   - 함수 정의 시 `ratings`라는 옵셔널 인자(리스트 형태, 기본값은 None)를 함께 받습니다. 
     * `ratings` 리스트에는 유저 ID 순서대로 매칭되는 평점(정수 또는 실수)들이 들어있습니다.

2. 데이터 정제 및 예외 처리 (try-except 필수):
   - `zip`을 활용하여 위치 인자로 들어온 `user_ids`와 옵셔널 인자로 들어온 `ratings` 데이터를 쌍으로 묶어 순회하세요.
   - `kwargs`에서 해당 유저 ID의 리뷰 텍스트를 꺼내오세요. (단, `.get()`을 사용하여 리뷰가 없는 유저라면 기본값으로 "No Review"를 설정하세요.)
   - **평점 검증**: 평점 데이터가 숫자가 아니거나(int 또는 float 계열이 아닌 경우), 1점 미만 또는 5점 초과인 경우 `ValueError`를 발생시키고, 
     "[_에러_] {유저ID}: 올바르지 않은 평점"을 출력한 뒤 해당 유저는 건너뛰세요.
   - **텍스트 정제**: 정상적인 리뷰 텍스트는 앞뒤 공백을 제거하고 모두 대문자로 변경하세요. (힌트: .strip().upper())

3. 결과물 반환 (딕셔너리 컴프리헨션 필수):
   - 최종적으로 검증을 통과한 유저들 중, 정제된 리뷰 텍스트에 "GOOD" 또는 "BEST"라는 단어가 포함된 유저들만 필터링하세요.
   - `{유저ID: 평점}` 형태의 딕셔너리를 컴프리헨션으로 만들어 반환하세요.
"""

def clean_and_tag_reviews(*args, ratings=None, **kwargs):
    # 1. zip과 언패킹을 활용해 args(유저ID들)와 ratings(평점들)를 동시에 순회하세요.

    # 2. try-except 문을 내부 구성을 통해 평점을 검증하고 텍스트를 정제하여 valid_users에 채우세요.
    
    # 3. 최종 결과를 딕셔너리 컴프리헨션을 사용해 조건에 맞게 필터링하여 반환하세요.





# def clean_and_tag_reviews(*args, ratings=None, **kwargs):
#     if ratings is None:
#         ratings = []
        
#     valid_users = {} # 예외를 통과한 정상 데이터들을 임시 저장할 공간
#     # 1. zip과 언패킹을 활용해 args(유저ID들)와 ratings(평점들)를 동시에 순회하세요.
#     zipped = zip(args, ratings)
#     for id, rating in zipped:
#         try:
#             if not isinstance(rating, (int, float)) or rating < 1 or rating > 5:
#                 raise ValueError(f"[_에러_] {id}: 올바르지 않은 평점")
#             review_text = kwargs.get(id, "No Review").strip().upper()
#             valid_users[id] = (rating, review_text) 
#             print(valid_users)
#         except ValueError as e:
#             print(e)
#     return { user: rating_review[0] for user, rating_review in valid_users.items() if "GOOD" in rating_review[1] or "BEST" in rating_review[1] }
#     # 2. try-except 문을 내부 구성을 통해 평점을 검증하고 텍스트를 정제하여 valid_users에 채우세요.
    
#     # 3. 최종 결과를 딕셔너리 컴프리헨션을 사용해 조건에 맞게 필터링하여 반환하세요.


# ==============================================================================
# [테스트 실행 코드]
# ==============================================================================
if __name__ == "__main__":
    # 위치 인자로 들어갈 유저 ID 리스트
    user_list = ["user_01", "user_02", "user_03", "user_04", "user_05"]
    
    # 옵셔널 인자로 들어갈 평점 리스트 (유저 ID 순서와 매칭됨)
    review_ratings = [4.5, "최고예요", 1.2, 5.0, -0.5] # 02번(문자열), 05번(음수) 에러 데이터
    
    # 키워드 인자로 들어갈 리뷰 텍스트
    review_texts = {
        "user_01": "  This product is so good!  ",
        "user_02": "Perfect!",
        "user_03": "Bad delivery.",
        "user_04": "  the best item ever   ",
        "user_05": "Not good"
    }

    # 함수 호출 (가변 인자 언패킹 형태로 데이터를 던집니다)
    result = clean_and_tag_reviews(*user_list, ratings=review_ratings, **review_texts)
    
    print("\n[최종 필터링된 리뷰어 결과]")
    print(result)
    
    # 예상 출력 결과:
    # [_에러_] user_02: 올바르지 않은 평점
    # [_에러_] user_05: 올바르지 않은 평점
    # 
    # [최종 필터링된 리뷰어 결과]
    # {'user_01': 4.5, 'user_04': 5.0}
