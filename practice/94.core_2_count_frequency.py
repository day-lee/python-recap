""" Follow-up:
        1. dictionary를 이용한 counting pattern을 설명하라. 
            - get method를 사용하면 missing key에도 default 값을 줄 수 있어서 KeyError 없이 카운팅을 할 수 있다. 

        2. Counter의 장점은?
            - 속도가 빠르다. 내부 최적화 루프돈다. 
            - built-in method가 많다. most_common(), +, - 연산 등 
            - dict(counter)) # Counter는 Dict의 서브클래스(자식)이라서 그대로 써도 되지만 명시적 형변환해서 써줘도 된다. 

        3. 가장 많이 등장한 값 3개를 가져오려면?
            - counter.most_common(3) 메소드를 쓴다. 

        4. 데이터가 generator로 들어온다면?
            - generator는 lazy evaluation을 한다. 소괄호 형태의 generator expression이나 yield로 만든다. 
            - Counter는 generator를 인자로 바로 받아서 쓸 수 있다. 내부적으로 제너레이터가 끝날 때 까지 하나씩 값을 꺼내오며 빈도수를 누적하기 때문에 메모리를 거의 쓰지 않고 대용량 빈도 계산 최강 조합임. 
"""
# 메모리 폭발 없이 하나씩 꺼내며 카운팅 가능!
# 결과 Counter({'A': 100000000, 'B': 100000000})
"""
이 코드에서 next()가 명시적으로 보이지 않는데도 값이 잘 계산되는 이유는 다음과 같습니다.
1. 객체 생성 단계: huge_data_generator()를 호출하는 순간에는 내부 코드가 실행되지 않고, 오직 값을 생산할 준비가 된 '제너레이터 객체만 생성'되어 반환됩니다

2. 자동 호출 단계: 이 제너레이터 객체를 Counter()에 전달하면, 'Counter가 내부적으로 루프를 돌며 제너레이터의 __next__를 자동으로 계속 호출하여 값을 하나씩 빼옵니다'

3. 지연 평가(Lazy Evaluation): 2억 개(1억 * 2)의 문자열을 한 번에 메모리에 적재하는 대신, 'Counter가 다음 값을 요청할 때마다 메모리에 딱 하나씩만 올려서 전달합니다'
덕분에 대규모 데이터임에도 불구하고 메모리 에러(OOM) 없이 안전하게 스트리밍 처리가 가능합니다

4. 소진: 제너레이터가 모든 값을 다 내어주고 StopIteration에 도달하면 소진(exhausted) 상태가 되어 루프가 자연스럽게 종료되고 최종 카운트 결과가 화면에 출력됩니다
"""
def huge_data_generator():
    for _ in range(100000000):
        yield "A"
        yield "B"

from collections import Counter
my_counter = Counter(huge_data_generator()) 
print(my_counter)


""" from collections import defaultdict
    - defaultdict()는 초기값 데이터 형태를 미리 지정해놓고, 키가 없으면 자동으로 초기값을 만들어준다. 
    - defaultdict(datatype)는 인자로 데이터 타입 이름을 받는다. int는 0, list는 [], set은 set() 빈세트를 만든다. e.g. inverted_dict = defaultdict(list)
    - 변수 정의 없이, 바로 manipulation할 수 있다. e.g. new_dict[lang].append(name) 
"""

# ============================================================
# 02. 빈도수 계산
# ============================================================

def problem_02_count_frequency(items):
    """
    [Dictionary / Counter]

    리스트에 각 값이 몇 번 등장하는지 계산하라.

    Example:

        input:
            ["A", "B", "A", "C", "B", "A"]

        output:
            {
                "A": 3,
                "B": 2,
                "C": 1
            }

    조건:
        - 먼저 일반 dictionary를 사용해서 구현한다.
        - 그 다음 collections.Counter를 사용해서 다시 구현한다.


    """

    # 1. 일반 딕셔너리
def problem_02_count_frequency_1(items):
    result = {}
    for item in items:
        result[item] = result.get(item, 0) + 1 
    print(result)



    # 2. collections.Counter 
def problem_02_count_frequency_2(items):
    from collections import Counter

    counter = Counter(items)
    print(dict(counter)) # Counter는 Dict의 서브클래스(자식)이라서 그대로 써도 되지만 명시적 형변환해서 써줘도 된다. 
    print(counter.most_common(2))



    # 3. defaultdict 
def problem_02_count_frequency_3(items):
    from collections import defaultdict 

    result = defaultdict(int)
    for item in items:
        result[item] += 1 
    print(f"result========: {dict(result)}")


    
    



problem_02_count_frequency_1(["A", "B", "A", "C", "B", "A"])
problem_02_count_frequency_2(["A", "B", "A", "C", "B", "A"])
problem_02_count_frequency_3(["A", "B", "A", "C", "B", "A"])
 