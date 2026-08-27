
# ============================================================
# 03. None / Empty / Falsy
# ============================================================
"""
    Follow-up:
        1. Python에서 falsy한 값에는 무엇이 있는가? False, 0, "", [], {}, (), set()  

        2. `if value`가 위험할 수 있는 데이터 처리 상황은? falsy 값은 무시되므로, 0 이나 False 값을 계산해야한다거나 하면 일괄적으로 제거될 수 있다. 

        3. 0을 유효한 값으로 취급해야 한다면? 명시적으로 if value is not None and value != "" 로 제외 대상을 명확하게 선언한다. 

        4. False와 None을 구분해야 하는 상황은? None은 아예 값이 없을 때, 미입력, False는 boolean으로 논리가 거짓일때(실패, 종료, 미충족 등)

"""


def problem_03_filter_valid_values(values):
    """
    [None / Truthy / Falsy]

    다음 데이터에서 "실제로 값이 없는 데이터"만 제거하라.

        values = [
            "Alice",
            "",
            None,
            "Bob",
            0,
            False,
            "valuelie"
        ]

    단순히 `if value`를 사용하는 것과
    `if value is not None`을 사용하는 것의 차이를 설명하라.

    요구사항:
        - None만 제거하는 버전을 작성한다.
        - 빈 문자열까지 제거하는 버전을 작성한다.

    """
    pass

values = [
            "Alice",
            "",
            None,
            "Bob",
            0,
            False,
            "charlie"]

# None 제거 버전
def problem_03_filter_valid_values_1(values):
    print([value for value in values if value is not None])



# None, "" 제거
def problem_03_filter_valid_values_2(values):
    print([value for value in values if value is not None and value != ""])



# 모든 falsy값 제거 
def problem_03_filter_valid_values_3(values):
    r = [] 
    for value in values:
        if value:
            r.append(value)
    print(r)



problem_03_filter_valid_values_1(values) # ['Alice', '', 'Bob', 0, False, 'valuelie']
problem_03_filter_valid_values_2(values) # ['Alice', 'Bob', 0, False, 'valuelie']
problem_03_filter_valid_values_3(values) # ['Alice', 'Bob', 'valuelie']
