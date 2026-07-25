"""
======================================================================
[묶음 2] 중급 연습 문제 (Level 2)
======================================================================
"""


def question_15():
    """
    [15번 문제] 딕셔너리 데이터 반전 및 정렬

    - 상황: 추천 시스템에서 사용할 유저별 선호 카테고리 태그 데이터가 있습니다.
    - 요구사항:
        1. 현재 {유저: 카테고리} 구조를 {카테고리: [유저, 유저...]} 구조로 역변환(Invert)하세요.
        2. 변환된 딕셔너리의 value인 유저 리스트는 '알파벳 순서'로 정렬되어야 합니다.
    - 조건: 일반 딕셔너리 제어문과 리스트 내장 정렬을 활용하세요.
    - 출력 예시: {'Python': ['Alice', 'Charlie'], 'Java': ['Bob', 'Daniel']}
    """
    user_preferences = {
        "Charlie": "Python",
        "Alice": "Python",
        "Daniel": "Java",
        "Bob": "Java",
    }

    inverted_dict = {}

    # TODO: user_preferences를 순회하며 데이터를 역변환하고 정렬하세요.
    # dict.setdefault()나 collections.defaultdict를 사용











    """ 모범 답안
    미리 정렬해놓고 순회하기. 
    키를 not in 키워드로 골라서 키 없으면 빈 리스트 생성
    키 있다면 그대로 추가.

    for name, stack in sorted(user_preferences.items()):
        if stack not in inverted_dict:
            inverted_dict[stack] = []
        inverted_dict[stack].append(name)
    """

    # 첫번쨰 시도
    # for name, stack in user_preferences.items():
    #     if inverted_dict.get(stack) is None:
    #         inverted_dict[stack] = [name]
    #     else:
    #         inverted_dict.get(stack).append(name)

    # for key, names in inverted_dict.items():
    #    inverted_dict[key] = sorted(names)




    print(f"15번 결과: {inverted_dict}")
    return inverted_dict


if __name__ == "__main__":
    # 코드를 완성한 후 실행하여 결과를 확인해보세요!
    question_15()
