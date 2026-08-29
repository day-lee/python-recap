"""

    Follow-up:
    1. yield와 return의 차이는?
       return은 값을 반환하고 함수를 끝내지만, yield는 값을 하나 반환하고 freeze 된 상태에서 다음 호출을 기다린다. next()
    
    2. generator 함수가 호출될 때 함수 내부 코드는 즉시 실행되는가?
       함수를 호출하면 오직 generator 객체만 생성되어 반환된다. 내부 코드는 첫 번째 next()가 호출될 때 비로소 시작되어 첫 번째 yield를 만날 때 까지 진행된다. 
    
    3. generator가 메모리 측면에서 유리한 이유는? 
        메모리에 하나씩 올려두고 __next__로 하나씩 빼와서, 한번에 메모리에 전체 데이터를 올려놓고 작업하지 않기때문에 메모리 효용에서 유리하다. 
        리스트는 O(N)만큼 메모리를 차지하고, generator는 다음 값 생성할 상태만 기억하느라 O(1)로 일정하다. 
    
    4. generator를 두 번 순회하면 어떻게 되는가? 
        Iterator의 point가 StopIteration에 도달해서 exhausted 되어 더이상 꺼낼 값이 없다. 
   
    5. 10억 개의 데이터를 처리해야 한다면 왜 generator가 유용한가? 
        10억개의 데이터를 메모리에 올리려고 하면 OOM 에러가 나서 실행을 할 수 없다. 
        generator는 lazy evaluation으로 하나씩만 메모리에 올려서 처리하므로 메모리 에러가 나지 않는다. 
        대용량 파일 읽기나 스트리밍 데이터 처리 시, generator를 활용한 Stream Processing이 필수적이다. 

"""


def problem_05_generator():
    """
    [Generator / Yield]

    0부터 n-1까지 숫자를 하나씩 생성하는 generator 함수를 작성하라.

        numbers = generate_numbers(5)

    위 코드에서 numbers를 한 번에 list로 만들지 않고 다음과 같이
    하나씩 출력할 수 있어야 한다.

        for number in numbers:
            print(number)

    예상 출력:

        0
        1
        2
        3
        4

    조건:
    - yield를 사용하라.
    - list를 만들어 반환하지 마라.

    """
    pass


def problem_05_generator_1():
    def generate_numbers(input):
        for num in range(0, input):
            yield num
    # 작성한 함수 자체 반환 
    return generate_numbers

# problem_05_generator_1함수는 generator_numbers()함수를 반환한다. 
generator = problem_05_generator_1()
# 클로저 개념: 제너레이터 객체가 생성됨, 함수 내부에 yield 키워드를 보고 호출시 코드를 실행하지 않고, 하나씩 값을 꺼낼 수 있는 제너레이터 객체를 만들어 반환한다. 
numbers = generator(5)

# 호출해도 코드 바로 실행하지 말고, 제너레이터 객체만들어 리턴해라. 포룹에서 하나씩 메모리에 올리며 프린팅함
# for loop이나 next()함수 호출될 때만 다음 yield 만날때까지 코드 실행해! 신호보냄 
for num in numbers:
    print(num)