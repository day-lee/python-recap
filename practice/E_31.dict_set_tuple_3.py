"""
======================================================================
[묶음 2] 기본~중급 연습 문제 (Level 1.5) - dictionary, set, tuple
======================================================================
"""

def question_12():
    """
    [12번 문제] 엑셀 VLOOKUP 스타일의 데이터 매칭 (dict + set)

    - 상황: 마케팅 부서에서 이벤트 대상자 ID 세트와, 실제 로그인한 유저 정보 딕셔너리를 가지고 있습니다.
    - 요구사항:
        1. 이벤트 대상자(`event_targets`) 중에서 '실제 오늘 로그인한 유저'만 골라내세요.
        2. 그 유저들의 '실제 이메일 주소'를 밸류로 가지는 딕셔너리를 만드세요.
        3. 즉, {로그인한대상자ID: 이메일} 형태의 딕셔너리가 되어야 합니다.
    - 조건: dict comprehension을 사용하거나 일반 반복문을 사용해 매칭하세요.
    - 출력 예시: {'user1': 'alice@test.com', 'user3': 'charlie@test.com'}
    """
    event_targets = {"user1", "user3", "user5"}  # 이벤트 대상자 ID (set)

    # 오늘 로그인한 유저 정보 (dict) -> {ID: 이메일}
    today_logged_in = {
        "user1": "alice@test.com",
        "user2": "bob@test.com",
        "user3": "charlie@test.com",
        "user4": "david@test.com",
    }

    pass


    # 덩어리가 작은 메인 시트를 루프에 올리는게 좋음. event_target이 더 짧으니까 그걸 기준으로. 내가 처음 짠건 today_logged_in을 기준으로 루프를 돌림. 
    # result_dict = {user: email for user, email in today_logged_in.items() if user in event_targets }

    print(f"12번 결과: {result_dict}")
    return result_dict


if __name__ == "__main__":
    # 코드를 완성한 후 실행하여 결과를 확인해보세요!
    question_12()
