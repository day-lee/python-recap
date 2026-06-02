"""
======================================================================
[묶음 2] 중급 연습 문제 (Level 2) - dictionary, set, tuple
======================================================================
"""


def question_13():
    """
    [13번 문제] 가맹점 데이터 병합 및 다중 그룹화 (dict + tuple)

    - 상황: 마케팅 부서에서 서로 다른 두 지점의 매출 데이터를 받았습니다.
    - 요구사항:
        1. 두 지점의 데이터를 합산하여 전체 가맹점의 '상품별 총 매출액 및 총 판매량'을 계산하세요.
        2. 최종 결과는 {상품명: (총매출액, 총판매량)} 형태로, value가 '튜플'이어야 합니다.
    - 조건: 앞서 배운 `dict.get(key, (0, 0))` 공식의 확장판을 고민해 보세요.
    - 출력 예시: {'A': (450000, 15), 'B': (200000, 4), 'C': (150000, 5)}
    """
    # 데이터 구조: (상품명, 매출액, 판매량)
    branch_1 = [("A", 150000, 5), ("B", 200000, 4)]
    branch_2 = [("A", 300000, 10), ("C", 150000, 5)]

    total_report = {}

    # TODO: branch_1과 branch_2를 모두 순회하며 total_report를 완성하세요.

    print(f"13번 결과: {total_report}")
    return total_report


def question_14():
    """
    [14번 문제] 타겟 고객 세트 연산 및 등급 분류 (set + dict comprehension)

    - 상황: 신작 게임 출시를 앞두고 VIP 유저와 길드 마스터 유저 명단을 확보했습니다.
    - 요구사항:
        1. VIP이면서 '동시에' 길드 마스터인 핵심 유저(교집합)에게는 "LEGEND" 등급을 부여하세요.
        2. 둘 중 '한 곳에만' 속한 유저(대칭차집합)에게는 "HERO" 등급을 부여하세요.
        3. 최종 결과는 {유저ID: 등급} 형태의 딕셔너리로 만드세요.
    - 조건: set의 교집합(&), 대칭차집합(^) 연산자와 dict comprehension을 조합하세요.
    - 출력 예시: {'user1': 'LEGEND', 'user3': 'LEGEND', 'user2': 'HERO', 'user4': 'HERO'}
               (딕셔너리 특성상 순서는 무관합니다)
    """
    vip_users = {"user1", "user2", "user3"}
    guild_masters = {"user3", "user4", "user1"}

    # TODO: 두 세트의 집합 연산을 수행한 뒤, dict comprehension으로 등급 딕셔너리를 만드세요.
    result_dict = None

    print(f"14번 결과: {result_dict}")
    return result_dict


def question_15():
    """
    [15번 문제] 딕셔너리 데이터 반전 및 정렬 (dict + tuple + list)

    - 상황: 추천 시스템에서 사용할 유저별 선호 카테고리 태그 데이터가 있습니다.
    - 요구사항:
        1. 현재 {유저: 카테고리} 구조를 {카테고리: [유저, 유저...]} 구조로 역변환(Invert)하세요.
        2. 변환된 딕셔너리의 value인 유저 리스트는 '알파벳 순서'로 정렬되어야 합니다.
    - 조건: 일반 딕셔너리 제어문과 리스트 내장 정렬을 활용하세요.
    - 출력 예시: {'Python': ['Alice', 'Charlie'], 'Java': ['Bob', 'Daniel']}
    """
    user_preferences = {
        "Alice": "Python",
        "Bob": "Java",
        "Charlie": "Python",
        "Daniel": "Java",
    }

    inverted_dict = {}

    # TODO: user_preferences를 순회하며 데이터를 역변환하고 정렬하세요.

    print(f"15번 결과: {inverted_dict}")
    return inverted_dict


if __name__ == "__main__":
    # 코드를 완성한 후 실행하여 결과를 확인해보세요!
    question_13()
    question_14()
    question_15()
