
def question_2():
    """
    [2번 문제] 텍스트 카운터 및 조건부 딕셔너리 (Dict Comprehension)

    - 상황: 소스코드나 문서에서 특정 단어들의 출현 빈도를 분석하려고 합니다. 
      문자열에서 '3번 이상' 등장한 단어만 골라 {단어: 등장횟수} 형태의 딕셔너리를 만드세요.

    - 출력 예시: {'python': 3, 'is': 3}
    1. hashmap counter 
    2. Counter 
    """
    text = "PYTHON code is clean python code is fast python is LIFE"
      
    pass 

















    """ built-in Counter 모범 답안
    # ====================================================================
    #PEP 8 가이드에 따라 임포트 문은 최상단에 써야함
    from collections import Counter 

    clean_lower_list = text.lower().split()
    # Counter는 내부적으로 C로 구현, 기본 dict를 상속받은 subclass이다. 
    counter = Counter(clean_lower_list) # created  Counter({'python': 3, 'is': 3, 'code': 2, 'clean': 1, 'fast': 1, 'life': 1})
    result = { key: value for key, value in counter.items() if value >= 3 }
    return result
    """

    """hashmap counter 모범 답안 
    # text = "PYTHON code is clean python code is fast python is LIFE"
    # counter = {} 
    # # 현재는 " " 화이트 스페이스 하나만 걸르지만 아예 인자를 안주면 str.split() 공백, 탭, 줄바꿈도 모두 처리해줌. 인자 없이 쓰는게 나음. 
    # clean_text_list = text.lower().split()
    # # clean_text_list = text.lower().split(" ") 

    # # 해시맵을 이용한 빈도수 계산 get method로 pythonic 하게 만듬 : dictionary has hash map property for Big O of one O(1) lookups 
    # for word in clean_text_list:
    #     counter[word] = counter.get(word, 0) + 1

    # result = {key: value for key, value in counter.items() if value >= 3}
    # return result
    # ====================================================================
    """
    # - 요구사항:
    #     1. 주어진 문자열을 단어 단위로 쪼갭니다.
    #        (대소문자 구분을 없애기 위해 모두 소문자로 먼저 변환하세요)
    #     2. 문자열에서 '3번 이상' 등장한 단어만 골라 {단어: 등장횟수} 형태의 딕셔너리를 만드세요.
    # - 조건: 리스트의 list.count('str') 메소드와 dict comprehension을 조합하여 작성하세요.

    # text_list = text.lower().split(" ")
    # return {text: text_list.count(text) for text in text_list if text_list.count(text) >= 3}


    # list.count(str) 안쓰고 풀기
    # from collections import Counter 카운터라는 모듈로 처리 가능 
    # text_list = text.split(" ")
    # lowered_list = [text.lower() for text in text_list] # text_list는 이미 리스트 형태라서 굳이 한번더 리스트 컴프리헨션으로 만들어줄 필요가 없음. lower()을 위해서라면 앞에서 text일 때 먼저 lower() 붙여주면 됨. 
    # count_dict = {}
    # for data in lowered_list:
    #     if not count_dict.get(data):
    #         count_dict[data] = 0
    #     count_dict[data] += 1
    # result = { word: count for word, count in count_dict.items() if count >= 3}
    # print(result)

    # # using list.count(str) 사용해서 풀기 
    # splitted_list = text.lower().split(" ")
    # print(splitted_list)
    # r = {word: word.count(word) for word in splitted_list if splitted_list.count(word) >= 3}
    # print(r)

print(question_2())

