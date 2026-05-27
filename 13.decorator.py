함수 데코레이터	
- 기존 함수를 수정하지 않고 앞뒤로 원하는 기능 추가하는 문법
- 일급 객체(함수 주고받기)과 클로저(남의 변수 기억하기) 개념을 이용함
- @데코레이터 문법 
- 실무 예시: 모든 API가 실행되는 데 걸리는 시간 측정 로그 남기기, 로그인 안한 유저 차단하기
- 디자인 패턴에서는 wrapper 래퍼 함수로 부름 
- 알맹이를 포장지로 감싸서 알맹이 실행 전후에 포장지가 추가 기능을 얹어 줌 


일급 객체(First-class object)
- 함수를 변수에 담을 수 있다.
- 다른 함수의 인자로 넘길 수있다.
- 함수가 함수를 리턴할 수 있다.
- 다른 프로그래밍 언어에서 함수는 위의 기능이 제한된다. 

클로저(Closure)
- 함수 안에 함수를 만드는 중첩구조
- 내부 함수가 외부 함수의 변수를 기억하고 보존하여 사용함
- 주변 환경을 내부에 묶어서 내부에 기억하고 있다고해서 클로저로 불림 

==============================================================

시간 측정 데코레이터 작성해보기
- 함수를 인자로 받아서 내부에서 실행한다.
- 클로저로 함수 주소 기억하고있다.
- 데코레이터 작성 후, 실제 함수에 적용해봐서 작동을 실험한다.

데코레이터 작성
import time
def record_time(original_func):
    def wrapper():
        start = time.time()
        original_func()
        end = time.time()
        print(f"Execution time: {end-start:.4f} seconds")
    return wrapper # 실수1: 함수 자체를 리턴해야함. 나는 wrapper() 로 괄호를 붙여서 바로 실행해버림. wrapper 함수 자체가 리턴값이 없어서 None을 뱉은 것임. 일급 객체 성질로 변수에 함수를 인자로 담아서 보내야함. 
            
@record_time
def process_big_traffic():
    print("Processing starts...takes time...")
    time.sleep(2)
    print("End of process")
    
process_big_traffic()
record_time함수의 내부 wrapper를 실행한 것()과 같은것임

*args, **kwarg를 설정하면 인자가 몇 개든 다 받아줄 수 있는 그릇이 생김

import time
def record_time(original_func):
    # 인자 그릇 준비
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print(f"time: {end-start:.4f} sec")
        # 원본 함수 결과값 돌려주기 변수에 담아 프린트 해주면 DONE
        return result
    return wrapper

@record_time
def greet(name="Lee", msg="Hi"):
    time.sleep(2)
    print(f"{name}, {msg}!!!")
    return "DONE"

status = greet(name="Kim")
print(f"func result: {status}")

