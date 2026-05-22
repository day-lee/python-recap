동적 언어와 정적 언어
파이썬은 동적 언어 (내부에 컴파일러를 내장하고 있는 인터프리터 언어)
변수 타입을 언제 검사하느냐가 차이점

동적언어 JS, python
코드 실행전에는 변수 타입 검사하지않고 런타임(실행중)에 알아서 판단
개발 속도가 빠르지만 실행 전에는 에러를 찾기 어려워 프로그램을 쓰다가 갑자기 버그가 발생하기 쉬움 
정적 언어 처럼 개발자가 컴파일 버튼을 누를 필요는 없지만
인터프리터 실행되는 순간 .py -> .pyc(바이트 코드, 가상머신 중간 언어) -> 인터프리터가 한줄씩 실행하며 0, 1 머신 언어로 변환
__pycache__에 .pyc파일들이 바이트코드 이진 데이터임

정적언어 자바, C++, Go
코드 실행전(컴파일 타임)에 변수 타입을 엄격하게 검사함
이 변수는 무조건 문자열만 허용한다고 컴퓨터랑 약속함. 다른 타입 넣으면 컴파일 에러가 난다. 
안정성이 높은 장점, 코드 작성이 까다롭고 길어지는 단점


사실 파이썬은 내부에 컴파일러를 내장하고 있는 인터프리터 언어이다.
컴파일 시점이 프로그램을 실행하는 순간이고, 내부에서 알아서 실행한다.
동적언어는 개발자가 직접 프로그램을 실행하기 전에 컴파일을 한다. 
파이썬 컴파일 결과물은 가상 머신이 읽는 중간 언어로 바이트 코드이고
정적 언어는 바로 .exe 머신언어이다. 



파이썬 타입 어노테이션

mypy library for type checking 
pip3 install mypy
mypy filename.py
 ========================================================================================
name: str = "misty"
age: int = 12
colour: str = "black"

def greeting(name: str) -> str:
    return f"Hello {name}"

print(greeting("misty"))

numbers: list[int] = [1, 2, 3]
user_info: dict[str, str] = {"name": "misty", "role": "cat"}

from typing import Optional, Union
middle_name: Optional[str] = None

id_value: Union[int, str] = 111

[연습 미션] 아래 함수의 매개변수와 리턴값에 타입을 적어보세요.
조건: users는 딕셔너리 리스트입니다. (예: [{"name": "Alice", "age": 25}])
def register_user(users: list[dict[str, str | int]], new_user_name: str, new_user_age: int) -> list[dict[str, str | int]]:
    new_user: dict[str, str | int] = {"name": new_user_name, "age": new_user_age}
    users.append(new_user)
    return users

dict[str, str | int]
첫번째 str은 모든 key의 타입 - 키는 불변 타입만 사용가능 str, int, tuple 
두번째 str | int는 모든 벨류의 타입 한꺼번에 



아래 함수의 매개변수와 리턴값에 타입을 적어보세요.
힌트: 리턴값은 float일 수도 있고, None일 수도 있습니다!
def calculate_average_rating(product_name:str, ratings:list[int]) -> float | None:
    if not ratings:
        return None
        
    total:int = sum(ratings)
    average: float = total / len(ratings)
    return average




