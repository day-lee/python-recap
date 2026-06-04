"""
[Senior's Code Review: 주니어 파이썬 개발자를 위한 실전 문법 다지기]

* 지침: 아래 함수들의 독스트링(주석)을 읽고, 요구사항에 맞게 코드를 구현하세요.
* 팁: 문법이 아직 어색하다면 에러 메시지를 두려워하지 말고 자주 실행해 보세요!
"""

# =====================================================================
# 문제 1. 회원 정보 정제하기
# 활용 토픽: str, list, dictionary, list_dict_comprehension
# =====================================================================
def clean_user_data(raw_users):
    """
    공백이 섞인 회원 이름 배열을 받아, 공백을 제거하고 대문자로 변환합니다.
    변환된 이름을 key로, 이름의 길이를 value로 가지는 딕셔너리를 리턴하세요.
    (반드시 dictionary comprehension을 사용하세요.)

    Args:
        raw_users (list): 공백이나 소문자가 섞인 문자열 리스트
        예: [" alice ", "bob  ", "  charlie"]

    Returns:
        예: {"ALICE": 5, "BOB": 3, "CHARLIE": 7}
    """
    pass 
    # 가독성을 위해 정제된 데이터를 만들고나서, dictionary comprehension을 적용하기. 







    # 중첩문에서 리스트를 만들어서 하나씩 꺼내옴 
    # return {   
    #     clean_name: len(clean_name)
    #     for name in raw_users
    #     for clean_name in [name.strip().upper()]
    # }

    # 1. Cleanse names using a generator expression to process items one by one and save memory. - memory efficiency, lazy evaluation
    # 2. Build the final dictionary using a dictionary comprehension  
    # return { name: len(name) for name in }

    # # generator 사용
    # cleaned_data = (name.strip().upper() for name in raw_users)
    # return {name: len(name) for name in cleaned_data}

    # # 메서드 중복 사용
    # return { name.strip().upper(): len(name.strip()) for name in raw_users }

    # AI 제안 제너레이터 이용한 메모리 적게 쓰고 중복 연산 발생하지 않는 버젼
    # 제너레이터 내부에서 이름 데이터 조작부터 해서 정제한 뒤에, 딕셔너리 컴프리헨션으로 만듬 
    # return { name: len(name) for name in (user.strip().upper() for user in raw_users)}

    # # strip() 연산을 두번 하므로 두번 일하게 됨. 성능상 좋지 않음 
    # return {user.strip().upper(): len(user.strip()) for user in raw_users }

    # # 처음에는 dict 내에서 strip().upper()를 두번 썼는데 함수로 바꾼다고 해도, 연산이 두번씩 실행되니 성능에 문제 생길 수 있어서 먼저 정제한 뒤에 딕트 컴프리헨션으로 바꿈 

    # cleaned_data = [name.strip().upper() for name in raw_users]
 
    # result = {item: len(item) for item in cleaned_data}
    # return result


print("--- Test 1: clean_user_data ---")
raw_data = [" alice ", "bob  ", "  charlie", "bob  "]
print(clean_user_data(raw_data)) 
# 예상 결과: {'ALICE': 5, 'BOB': 3, 'CHARLIE': 7}


# =====================================================================
# # 문제 2. 과일 재고 매칭하기
# # 활용 토픽: zip_unpacking, tuple, set
# # =====================================================================
def find_unique_fruits(names:list[str], counts:list[int]) -> set[str]:
    """
    과일 이름 리스트와 재고 수량 리스트를 zip으로 묶어 (이름, 수량) 튜플들을 만듭니다.
    그 중 재고 수량이 0인 과일은 제외하고, 재고가 있는 과일의 '이름'만 뽑아 
    중복이 없는 집합(set)으로 리턴하세요.

    Args:
        names (list): 과일 이름 리스트 (예: ["apple", "banana", "apple"])
        counts (list): 재고 수량 리스트 (예:)

    Returns:
        set: 재고가 1개 이상인 고유한 과일 이름 집합
        # 예상 결과: {'apple', 'orange'} (순서는 다를 수 있음)

    """
    pass


    # one liner
    # return { fruit for fruit, qty in zip(names, counts) if qty > 0 }

    # unique_fruits = set()
    # zipped = list(zip(names, counts))
    # print(zipped) # [('apple', 10), ('banana', 0), ('orange', 5), ('apple', 3)]
    # for fruit, qty in zipped:
    #     if qty > 0:
    #         unique_fruits.add(fruit)
    # return unique_fruits


#     zipped = zip(names, counts)
#     # set comprehension 으로 set(list) 하지 않고 한번에 만들 수도 있음 
#     return {name for name, count in zipped if count > 0}
#     # inventory = set([name for name, count in zipped if count > 0])
#     # return inventory
    

print("\n--- Test 3: find_unique_fruits ---")
fruits = ["apple", "banana", "orange", "apple"]
stocks = [10, 0, 5, 3]
print(find_unique_fruits(fruits, stocks))
