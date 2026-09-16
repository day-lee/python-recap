""" Iterable vs. Iterator 
    Follow-up:
    1. iterable과 iterator의 차이는? 
        Iterable
        - 반복가능한 객체 (list, set, dict) - repeatable 
        - for loop넣어서 요소에 하나씩 접근할 수 있는 모든 객체 
            -> for loop 내부적으로 iter()호출해서 자동으로 next() 반복 호출하며 작동한다. 
        - 데이터 저장소의 역할에 집중하고, 여러 번 반복 사용하기 위해 iterable로 존재한다. 

        Iterator 
        - next()를 사용해야 다음 값을 반환할 수 있다. 
        - generator는 이터레이터의 일종으로 실제로 값을 요청할 때만 메모리에 올린다. (lazy evaluation)
        - iterator는 일회용. 한번 쓰고나면 exhausted 된다. 

    2. iter()는 무엇을 반환하는가? 
        -> 이터레이터 객체를 반환

    3. next()는 무엇을 하는가?
        -> 이터레이터의 다음 요소를 반환, 내부 포인터 위치를 다음으로 이동 

    4. list는 왜 iterator 자체가 아닌가? 
        -> list는 데이터 저장소의 역할에 집중하느라 iterable이다. 
        list가 이터레이터가 되면 for loop 한번 돌리고 나면 소비되어 재사용이 불가함. 여러 번 반복문을 돌릴 수 있게 하려고 리스트는 이터러블로만 존재. 

    5. iterator를 모두 소비한 뒤 next()를 호출하면 어떤 일이 발생하는가?
        -> StopIteration exception이 발생하고, exhausted되어서 한번 사용하면 끝남. 루프 종료 

"""

def problem_04_iterable_vs_iterator():
    """
    [Iterable / Iterator]

    다음 객체들을 보고 각각 iterable인지, iterator인지 설명하라.

        numbers = [1, 2, 3] -> iterable 룹에서 하나씩 접근할 수 있는 객체
        numbers_iterator = iter(numbers) -> iterator iter 객체로만들어서 객체의 method, property에 모두 접근 가능한 상태 

    다음 코드가 왜 동작하는지도 설명하라. 
        -> for 루프가 내부적으로 iter(numbers)를 호출하여 자동으로 iterator를 만들고 next()를 반복 호출해줌.  

        for number in numbers:
            print(number)

    그리고 다음 코드의 차이를 설명하라. 
        -> numbers_iterator는 현재 어디까지 읽었는지 위치 상태를 기억해서 next() 호출 시마다 한칸씩 앞으로 이동하며 요소를 꺼내온다. 

        print(next(numbers_iterator))
        print(next(numbers_iterator))
        print(next(numbers_iterator))

    """
    pass
