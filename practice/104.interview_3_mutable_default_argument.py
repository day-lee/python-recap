""" Mutable Default Argument Anti-pattern 
Follow-up:
    1. default argument는 언제 평가되는가? 
    -> default argument는 함수 정의 시점에 딱 한번만 평가(생성)되어 메모리에 올라간다. 
       함수 호출시엔 이미 메모리에 올라간 동일 객체를 계속 공유하기 때문에 이전 데이터가 누적됨 

    2. list 대신 immutable object를 default argument로 사용하면 어떤 차이가 있는가? 
    -> str으로 디폴트 아규먼트를 items=''로 바꾸니까 이전의 데이터는 없어지네? 
       str, int, tuple 같은 불변 객체는 값 수정이 안되므로 새로 객체를 생성해서 items 변수에 할당함 

    3. 실무에서 이 버그를 발견했다면 어떻게 테스트할 것인가? 
    -> 의도하지 않게 데이터가 누적되면 정보가 섞일 수 있음 Mutable Default Argument Anti-pattern 
       여러번 호출했을 때 이전 호출이 다음 호출에 영향을 주지 않는지 유닛 테스트 해봄 
"""

def problem_02_mutable_default_argument():
    """
    [Mutable Default Argument]

    다음 함수의 동작을 분석하라.

        def add_item(item, items=[]):
            items.append(item)
            return items

    다음 코드의 출력 결과를 예측하라.

        print(add_item("A"))
        print(add_item("B"))
        print(add_item("C"))

    그리고 왜 이런 결과가 발생하는지 설명하라.
    append는 리스트에 덮어쓰는게 아니라 추가하는동작이다. 
    items는 default 아규먼트로 보내져서 메모리가 기억을 하고 있는상태인가보다. 

    그 다음, 함수가 다음과 같이 동작하도록 수정하라.

        print(add_item("A"))  # ["A"]
        print(add_item("B"))  # ["B"]
        print(add_item("C"))  # ["C"]
    
    """
    pass



# 멱등성이 깨진다. 호출을 여러번 하면 계속 이전 값이 누적되어 나온다. 
# 언제 호출하느냐에 따라 결과가 달라지는 예측 불가능한 함수
def add_item_antipattern(item, items=[]):
    items.append(item)
    return items

print(add_item_antipattern("A")) #['A']
print(add_item_antipattern("B")) #['A', 'B']
print(add_item_antipattern("C")) #['A', 'B', 'C']



# 함수 호출시 마다 배번 새로운 리스트를 생성하도록 만들려면 
# 기본값을 None으로 설정하고 함수 내부에서 리스트를 새로 할당해야함 
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("A"))
print(add_item("B"))
print(add_item("C"))