가변 인자 variable arguments

사용자가 몇개의 인자를 보낼지 모를 때 사용 
여러개의 값을 받을 때...
*args: "튜플"로 묶어 받음 - 패킹 
      인자가 몇개 들어오던 하나의 튜플 보따리로 묶어라
**kwargs: "딕셔너리"로 묶어 받음 

get() 함수로 꺼내주거나 디폴트 값을 줌
    kwargs.get("email", "no email")
  
일반 인자 -> *args -> 기본값 인자 -> kwargs 순서 중요
def test_func(a, b, *args, option=True, **kwargs): 
  
데코레이터나 클래스 상속시 많이 사용함 
class CustomView(BaseView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_custom_attribute = True
==============================================

def sum_all(*args):
    print(f"args type: {type(args)}") 
    print(f"data: {args}")
    print(sum(args))

sum_all(1, 2, 3, 4)

# args type: <class 'tuple'>
# data: (1, 2, 3, 4)
# 10

def create_profile(name, **kwargs):
    print(f"required name: {name}")
    print(f"optional: {type(kwargs)}")
    print(f"optional: {kwargs}")

    email = kwargs.get("email", "no email")
    age = kwargs.get("age", "no age")

    print(f"{name} / {email} / {age}")


create_profile("kim", email="test@email.com", age=11)
create_profile("lee", email="test@email.com")
create_profile("park", age=10)

# required name: kim
# optional: <class 'dict'>
# optional: {'email': 'test@email.com', 'age': 11}

