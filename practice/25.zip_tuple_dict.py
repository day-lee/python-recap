"""
[Senior's Challenge: 회원 매칭 및 가변 데이터 정제]

* 토픽: zip_unpacking, list_dict_comprehension, exception, tuple, str, function
* 상황: 서로 다른 데이터베이스(DB)에서 긁어온 '회원 이름 문자열'과 '연락처 튜플'이 있습니다.
        두 데이터를 매칭하여 하나의 깔끔한 딕셔너리로 합쳐야 합니다.
"""

def merge_and_clean_profiles(raw_names: str, contact_tuples: list) -> dict:
    """
    쉼표로 구분된 회원 이름 문자열과 (전화번호, 이메일) 튜플 리스트를 결합합니다.
    데이터 누락 및 에러를 안전하게 방어하면서 딕셔너리로 정제하세요.

    [요구사항]
    1. 이름 정제 (str):
       - `raw_names`는 하나의 긴 문자열입니다 (예: " alice , bob , , charlie ").
       - 쉼표(,)를 기준으로 쪼갠 뒤, 앞뒤 공백을 제거하세요.
       - 만약 쪼갠 값이 빈 문자열("")이거나 공백만 있다면 리스트에서 제외하세요.

    2. 데이터 결합 및 예외 처리 (zip_unpacking & exception):
       - 정제된 이름 리스트와 `contact_tuples`를 `zip`으로 묶어 순서대로 매칭하세요.
       - 단, 이름 리스트와 튜플 리스트의 '길이가 다를 수' 있습니다. 
         * zip 연산 중 어느 한쪽 데이터가 부족해서 빈 값이 생기면 안 됩니다.
         * 만약 데이터 쌍이 완벽하게 맞지 않아 연산 시 문제가 생기거나, 
           contact_tuples 내부의 데이터 형식이 잘못되어 IndexError 등이 발생하면 
           그 시점에서 안전하게 처리를 멈추고(break) 그때까지 완성된 결과만 리턴하세요.
       
    3. 결과 포맷 (Dictionary Comprehension):
       - 최종 결과는 딕셔너리 형태로 리턴해야 합니다.
         * Key: 대문자로 변환된 회원 이름 (예: "ALICE")
         * Value: 딕셔너리 형태의 연락처 정보 `{"phone": 전화번호, "email": 이메일}`
       - (선택 팁) 구현할 때 일반 반복문을 써도 좋고, 최종 단계에서 Dictionary Comprehension을 활용하면 코드가 훨씬 시니어처럼 깔끔해집니다.

    Args:
        raw_names (str): 쉼표로 연결된 지저분한 이름 문자열
        contact_tuples (list): (전화번호, 이메일) 형태로 이루어진 튜플 리스트

    Returns:
        dict: 정제된 회원 프로필 딕셔너리
    """
    pass

# =====================================================================
# 검증용 테스트 코드 (IDE에서 실행하여 결과를 확인하세요)
# =====================================================================
if __name__ == "__main__":
    # 1. 지저분한 로우 데이터 문자열 (중간에 빈 값 ", ," 도 섞여 있음)
    names_data = " alice , bob , , charlie , david "
    
    # 2. 연락처 데이터 튜플 리스트 (이름은 4개인데 연락처는 3개만 있는 불일치 상황)
    contacts_data = [
        ("010-1234-5678", "alice@test.com"),
        ("010-9999-8888", "bob@test.com"),
        ("010-5555-4444", "charlie@test.com")
    ]

    result = merge_and_clean_profiles(names_data, contacts_data)
    
    print("=== 최종 프로필 정제 결과 ===")
    import pprint
    pprint.pprint(result)
    
    """
    [예상 출력 결과]
    {
        'ALICE': {'email': 'alice@test.com', 'phone': '010-1234-5678'},
        'BOB': {'email': 'bob@test.com', 'phone': '010-9999-8888'},
        'CHARLIE': {'email': 'charlie@test.com', 'phone': '010-5555-4444'}
    }
    
    (연락처가 없는 'david'는 결과에서 안전하게 누락/제외되어야 합니다.)
    """
