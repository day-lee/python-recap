"""
======================================================================
[묶음 2] 기본~중급 연습 문제 (Level 1.5) - dictionary, set, tuple
======================================================================
"""


def question_10():
    """
    [10번 문제] 카테고리별 데이터 분류 및 집계 (dict)

    - 상황: 쇼핑몰의 유저별 구매 금액 로그가 들어왔습니다.
    - 요구사항:
        1. 주어진 리스트를 순회하며 유저별 총 구매 금액을 합산한 딕셔너리를 만드세요.
        2. {이름: 총금액} 형태여야 합니다.
    - 조건: 처음 등장하는 유저는 딕셔너리에 키를 새로 생성하고, 
           이미 존재하는 유저는 기존 금액에 더해주는 예외 처리 논리를 구현하세요.
    - 힌트: 앞서 배운 `if-else` 구조나 `dict.get(key, 0)` 공식을 활용하면 좋습니다.
    - 출력 예시: {'Alice': 45000, 'Bob': 30000, 'Charlie': 12000}
    """
    purchase_logs = [
        ("Alice", 15000),
        ("Bob", 30000),
        ("Alice", 30000),
        ("Charlie", 12000),
    ]

    result_dict = {}
    pass 





    # if result_dict.get(user): 이것보다 in 으로 키 존재여부 확인하는게 더 빠름 
    # for user, amount in purchase_logs:
    #     if user in result_dict:
    #         result_dict[user] += amount 
    #     else:
    #         result_dict[user] = amount 

    # 더 짧게 만들려면, 값이 있으면 가져와서 더해주고 아니면 0을 할당해준다(이때 amount는 초기 값)
    # JS에서 nullish coalescing 연산자 사용과 같음: (obj[key] ?? 0) + amount 
    # for user, amount in purchase_logs: 
    #     result_dict[user] = result_dict.get(user, 0) + amount

    print(f"10번 결과: {result_dict}")
    return result_dict


if __name__ == "__main__":
    # 코드를 완성한 후 실행하여 결과를 확인해보세요!
    question_10()
