
"""
dict.get(): 조회용
dict.setdefault(): 수정용  

    1. (x) + 연산은 느림 
    inverted_dict[stack] = inverted_dict.get(stack, []) + [name]
    
    2. (x) 이미 존재하는데 또 덮어씀. 비효율. 대입 연산자 없이 쓰는게 setdefault()의 목적 
    inverted_dict[stack] = inverted_dict.setdefault(stack, []) + [name]
    
    3. (x) get은 조회 전용, 딕셔너리 수정하지 않음, 따라서 공중분해 되어 [] 리턴  
    inverted_dict.get(stack, []).append(name) 
    
    4. (O) 원본 리스트 바로 수정  
    inverted_dict.setdefault(stack, []).append(name) 
    # 변형: 실제로 빈 리스트 저장한 뒤 리턴함. 데이터 누적됨. 대입할 필요가 없음. 
"""
from collections import defaultdict 
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

   


    # inverted_dict = {}

    # TODO: user_preferences를 순회하며 데이터를 역변환하고 정렬하세요.

    # dict.setdefault()나 collections.defaultdict를 사용

    pass 







    # 1. dict.get() : doesn't update dictionary. returned data doesn't change the original data. have to assign it to a variable to keep the value
    # 2. dict.setdefault(key, default): returning an actual data in the memory, can modify directly 
    # 3. collections library defaultdict(list): starting by assigning the default data type, modify data directly 

    # Start with sorted data. use items() for dict key sorting. sorted(user_preferences.items())
    # sorted_dict = sorted(user_preferences.items())


    # 1.inverted_dict = {}
    # for name, lang in sorted_dict:
    #     inverted_dict[lang] = inverted_dict.get(lang, []) + [name]
    # print(inverted_dict)

    # 2.inverted_dict = {}
    # for name, lang in sorted_dict:
    #     inverted_dict.setdefault(lang, []).append(name)
    # print(inverted_dict)

    # 3.from collections import defaultdict 

    # inverted_dict = defaultdict(list)

    # for name, lang in sorted_dict:
    #     inverted_dict[lang].append(name)
    # print(inverted_dict)

    """ 모범 답안
    미리 정렬해놓고 순회하기. 

    0. defaultdict() -> 실무 대용량 데이터에서 많이 쓰는 표준 
    inverted_dict = defaultdict(list)
    for name, stack in sorted(user_preferences.items()):
        inverted_dict[stack].append(name)
    final_dict = dict(inverted_dict) # defaultdict 클래스 출력하지 않고 딕셔너리 형태로 변환 

    
    0. dict.setdefault(key, default_value)
    inverted_dict = {}
    for name, stack in sorted(user_preferences.items()):
        inverted_dict.setdefault(stack, []).append(name)

        
    1. dict.get(key, default_value)
    dict에 items()를 붙인뒤 sorted를 만들면 키를 기준으로 정렬한다. 튜플 첫번째 요소 
    [('Alice', 'Python'), ('Bob', 'Java'), ('Charlie', 'Python'), ('Daniel', 'Java')]
    dict.get()으로 디폴트 값 추가, append() 대신 리스트 더하기 처리 

    sorted_user_preferences = sorted(user_preferences.items())
    for name, stack in sorted_user_preferences:
        inverted_dict[stack] = inverted_dict.get(stack, []) + [name]

    2.
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




    # print(f"15번 결과: {inverted_dict}")
    # return inverted_dict


if __name__ == "__main__":
    # 코드를 완성한 후 실행하여 결과를 확인해보세요!
    question_15()
