"""
======================================================================
[묶음 1] 심화 연습 문제 (Level 2) - str, list, comprehension
======================================================================
"""


def question_1():
    """
    [1번 문제] 중첩 리스트 평탄화 및 필터링 (Nested List Comprehension)

    - 상황: 부서별 프로젝트 참여자 명단이 2차원 리스트로 들어왔습니다.
        그중 이름에 성(Last name)인 "Kim"이 포함된 사람만 리스트로 반환하세요
    - 조건: 이 모든 과정을 '단 하나의 list comprehension 문법 안에서' 해결하세요.
    - 출력 예시: ['JOHN KIM', 'KIM MINSOO', 'RYAN KIM']
    """
    departments = [
        ["  John KiM ", " Amy Park "],
        [" Kim Minsoo ", " Lee Jisu "],
        ["Ryan Kim"],
    ]

    pass 







    # name_list = []
    # for data in departments:
    #     for name in data:
    #         if "Kim" in name:
    #             name_list.append(name.strip().upper())
    # print(name_list)

    # KiM이라는 예외 데이터를 넣음 
    # r = [ name.strip().upper() 
    #       for data in departments 
    #       for name in data
    #       if "KIM" in name.upper() ]
    # print(r)


    # - 요구사항:
    #     1. 2차원 리스트를 1차원 리스트로 펼치세요 (Flatten).
    #     2. 그중 이름에 성(Last name)인 "Kim"이 포함된 사람만 골라내세요.
    #     3. 앞뒤 공백을 제거하고 모두 대문자로 변환하세요.
    
    #물 흐르듯 위에서 아래로 잘 읽히는 구조를 짜보도록 - 바로 안짜져서 for loop 버젼으로 먼저 써봄 
    # for data in departments:
    #     for name in data:
    #         print(name)
    # return [name.strip().upper() 
    #        for data in departments 
    #        for name in data 
    #         if "KIM" in name.upper()]
    
    # # 내가 짠 코드는 컴프리헨션 내부에 또 다른 컴프리헨션을 생성하는 구조로 메모리에 중간 리스트를 만들게 되어서 메모리 낭비와 가독성이 떨어짐. 
    # result =  [
    #     name for name in 
    #     [name.strip().upper() for name_list in departments 
    #      for name in name_list ]
    #       if 'KIM' in name ]

    # # 리팩토링: 중첩을 제거하고 그 리스트에서 바로 비교를 해서 공간 복잡도가 줄어든다. 읽기가 훨씬 쉽다.
    # result = [
    #     name.strip().upper()
    #     for name_list in departments
    #     for name in name_list
    #     if "KIM" in name.upper()
    # ]

    # print(f"1번 결과: {result}")
    # return result

print(question_1())