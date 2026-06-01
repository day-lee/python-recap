
def question_2():
    """
    [2번 문제] 텍스트 카운터 및 조건부 딕셔너리 (Dict Comprehension)

    - 상황: 소스코드나 문서에서 특정 단어들의 출현 빈도를 분석하려고 합니다.
    - 요구사항:
        1. 주어진 문자열을 단어 단위로 쪼갭니다.
           (대소문자 구분을 없애기 위해 모두 소문자로 먼저 변환하세요)
        2. 문자열에서 '3번 이상' 등장한 단어만 골라 {단어: 등장횟수} 형태의 딕셔너리를 만드세요.
    - 조건: 리스트의 list.count('str') 메소드와 dict comprehension을 조합하여 작성하세요.
    - 출력 예시: {'python': 3, 'is': 3}
    """
    text = "python code is clean python code is fast python is LIFE"

    pass





    # # list.count(str) 안쓰고 풀기
    # # from collections import Counter 카운터라는 모듈로 처리 가능 
    # text_list = text.split(" ")
    # lowered_list = [text.lower() for text in text_list]
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

question_2()

