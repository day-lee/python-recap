"""
    Follow-up:
        1. set을 사용하면 왜 순서 문제가 발생할 수 있는가? 
            - set는 unordered type으로 순서 보장 안됨 
            - 숫자가 작을 때는 정렬되는 것 처럼 보이나, 문자열, 큰 데이터는 순서 유지 안됨. 
        2. membership check를 빠르게 해야 한다면 어떤 자료구조를 사용할 것인가? 
            - seen = set() not in을 사용해 O(1) 첫번째는 룹을 돌더라도 두번째 체크에선 하이패스로 체크할 수 있게함 
        3. 데이터가 1억 개라면 이 방법의 메모리 문제는? 
            - Out Of Memory 발생 가능성 100M은 set, dict 모두 메모리 문제 생길 수 있다. -> pandas drop_duplicates()나 대용량 처리에 특화된 Numpy 배열을 활용하는것이 좋다. 
        4. dict.fromkeys()를 사용하면 어떻게 구현할 수 있는가? 
            - 3.7부터 dictionary Insertion Order 보장 특징을 이용한다. 
            - dict.fromkeys(iterable, value)는 처음 등장 순서대로 key로 등록함.
            - dict의 key는 중복을 허용하지 않으므로, 중복이 자연스럽게 제거됨 
"""

def problem_01_remove_duplicates(items):
    """
    [Data Structure: set / dict]

    리스트에서 중복된 값을 제거하되,
    최초 등장 순서는 유지하라.

    Example:

        input:
            [3, 1, 2, 3, 2, 4, 1]

        output:
            [3, 1, 2, 4]

    조건:
        - 원본 리스트를 변경하지 않는다.
        - 결과는 list여야 한다.

    """
    # 1. order 조건 x [1, 2, 3, 4]
    # print(list(set(items)))



    # 2-1. membership check 특정 값이 자료 구조 안에 존재하는지 확인하기 O(N2) 
    # make index: value dict 
    # create empty list 
    # if list not value, then append, if it is already there then continue 

    # result = []
    # for item in items:
    #     if item not in result:
    #         result.append(item)
    # print(result)

    # 2-2. membership check 특정 값이 자료 구조 안에 존재하는지 확인하기 O(N), O(1) -> O(N)
    # seen = set() 
    # result = []
    # for item in items:
    #     if item not in seen:
    #         result.append(item)
    #         seen.add(item)
    # print(result)



    #3. 
    dict_items = dict.fromkeys(items) #{3: None, 1: None, 2: None, 4: None} -> None을 value로 주지 않아도 기본값은 None으로 들어감 
    # # print([key for key in dict_items.keys()]) # 굳이 리스트도 바꾸지 않아도 됨. 
    print(list(dict_items))  # 키만 남음 


problem_01_remove_duplicates([3, 1, 2, 3, 2, 4, 1]) 

