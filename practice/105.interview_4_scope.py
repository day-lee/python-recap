   
""" scope
Follow-up:
    1. local / enclosing / global / built-in scope란? local scope는 함수 내부, global은 코드 베이스 전체, enclosing, built-in은 모르겠음 
        -> 파이썬 내부에서 LEGB규칙으로 변수를 찾음. Local -> Enclosing -> Global -> Built-in 
        * enclosing scope는 중첩 함수일 때 (outer - inner) 바깥쪽 부모 함수 스코프를 말함. 
        * built-in 스코프는 기본제공 예약어 공간 print(), len()등 

    2. nonlocal은 언제 사용하는가? ??
        -> 중첩 inner 함수에서 outer 지역 변수를 수정하고 싶을 때 사용함 

    3. 함수 내부에서 global 변수를 읽는 것은 가능한가? 가능함. 
        -> read-only 가능 

    4. global 변수를 직접 수정하는 것이 왜 유지보수에 좋지 않을 수 있는가? 그 변수를 사용하는 코드의 모든 함수들에 영향을 미치기 때문?
        -> 사이드 이펙트, 즉 예측 불가능한 부작용이 발생할 수 있기 때문에 
"""

def problem_03_scope():
    """
    [Scope]

    다음 코드가 있다고 하자.

        x = 10

        def outer():
            x = 20

            def inner():
                x = 30
                return x

            return inner()

        print(outer())
        print(x)

    출력 결과를 예측하고 설명하라. 
    첫 프린트는 30, 두번째는 10 
    x자체는 global scope 환경이고, outer() inner()는 x가 함수 내 local scope에서 서로 참조 가능하기때문 

    그 다음 다음 코드를 수정하여 outer() 안에서
    global x의 값을 100으로 변경하도록 만들어라.

        x = 10

        def outer():
            x = 20
            # 여기를 수정

        outer()

        print(x)


    """
    pass

x = 10
def outer():
    # x = 20
    def inner():
        # x = 30
        return x
    return inner()

print(outer())
print(x)


# 부작용 - side effect 유발하는 코드임: global 변수 직접 수정 하지 말기 
x = 10
def outer_global():
    global x 
    x = 100

print(outer_global())
print(x)


# 누가, 어디서 전역 변수를 수정했는지 흐름을 명확히 추적할 수 있습니다.
# 내부에서 전역 변수를 직접 건드리지 않고, 새로운 값을 계산하여 반환(return)만 합니다.
x = 10
def outer():
    return 100

# 외부에서 명시적으로 값을 받아서 업데이트합니다.
x = outer() 
print(x)  # 출력: 100
