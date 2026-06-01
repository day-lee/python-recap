def double_up_age(original_func):
    def wrapper(args):
        args *= 2 
        return original_func(args)
    return wrapper

@double_up_age
def func(age:int):
    print(f"Hi, my age is {age}")

r = func(11)  
print(r)

=================================

def double_age(original_func):
    def wrapper(*args): # * asterisk pack into tuple 함수정의시에는 인자 몇개 올지모르니 보따리로 일단 패킹 
        args_list = list(args) # tuple unpacking, under-bar is used for 사용하지 않는 변수 명시 
        args_list[0] *= 2 # 나이 두배
        print(f"verify the arg: {args_list[0]}")
        original_func(*args_list)
        return "Done"
    return wrapper #we don't want to execute the function here, just return the function as a variable 함수 객체 자체를 참조 변수로 반환 

@double_age
def greet_and_age(age:int, name:str):
    print(f"Hi, I am {name}, {age} years old. ")

r = greet_and_age(11, "kim")
print(r)

=================================
키워드 args도 포함하려면?
실무에서는 안쓴다고 한다

def double_age(original_func):
    def wrapper(*args, **kwargs):
        args_list = list(args)
        if len(args_list) != 0:
            args_list[1] *= 2
            original_func(*args_list)
        else:
            kwargs["age"] *= 2
            original_func(**kwargs) # 딕셔너리 보따리 풀기
        return "Done"
    return wrapper


@double_age
def greet(name:str, age:int):
    print(f"Hi, I am {name}, {age} years old.")

greet("park", 12)
greet(age=13, name="kim")

=================================

import inspect

def double_age(original_func):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(original_func)
        print(f"sig========= {sig}")
        bound_args = sig.bind(*args, **kwargs)
        print(f"bound_args =========== {bound_args}")
        bound_args.apply_defaults()
        bound_args.arguments["age"] *= 2 
        return original_func(*bound_args.args, **bound_args.kwargs)
    return wrapper

@double_age
def complex_profile(name, age, job, city, hobby="programming"):
    print(f"[{name}/{age}] {city}에 사는 {job}입니다. 취미는 {hobby}예요.")

complex_profile("park", 12, "student", hobby="golf", city="bucheon") 
complex_profile(age=20, name="kim", job="developer", city="Busan", hobby="gaming")

===================================

# @wraps
from functools import wraps

def log_execution(original_func):
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] {original_func.__name__} 함수가 실행됩니다.")
        return original_func(*args, **kwargs)
    return wrapper

def greet(name):
    print(f"{name} hihihi")

greet("kim")