
def question_3():
    """
    [3번 문제] 컴프리헨션 안의 조건문 분기 (If-Else List Comprehension)

    - 상황: 쇼핑몰 리뷰 데이터에서 욕설이나 비속어를 마스킹(Masking) 처리하려고 합니다.
    글자수가 4글자를 초과하는 단어는 앞 2글자만 남기고 나머지는 '**'로 마스킹하세요.
    글자 수와 상관없이 마스킹 결과는 뒤에 무조건 '**' 두 개로 통일합니다)
    - 출력 예시: ['good', 'pe**', 'nice', 'aw**', 'bad']
    """
    words = ["good", "perfect", "nice", "awesome", "bad"]
    pass 






    
    """ f string 사용 모범 답안
    result = [f"{word[:2]}**" if len(word) > 4 else word for word in words ]
    print(result)
    """
    # print([ f"{word[:2]}**" if len(word) > 4 else word for word in words ])
    
    # - 요구사항:
    #     1. 주어진 단어 리스트에서 글자 수가 4글자를 초과(> 4)하는 단어는
    #        앞 2글자만 남기고 나머지는 '**'로 마스킹하세요. (예: "perfect" -> "pe**")
    #     2. 4글자 이하인 단어는 그대로 유지하세요.
    # - 조건: 컴프리헨션 내부에 'if-else 분기문'을 사용해야 합니다.

    # return [word[:2] + "**" if len(word) > 4 else word for word in words  ]

    # result = [ f"{word[:2]}**" if len(word) > 4 else word
    #            for word in words ]


print(question_3())
