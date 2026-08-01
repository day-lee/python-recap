
기본 매개변수 default parameters
def example(name, age=10)
- 기본값이 있으면 일반 매개 변수보다 뒤에 적어야함
- 기본 값으로 빈 리스트[], 빈 딕셔너리 {} 넣지않기 
  - 함수가 정의 되는 순간 기본 매개변수 객체를 딱 한번 생성해서 공유하므로 모든 함수 호출이 같은 리스트 객체를 돌려 쓴다. 
  - 기본값으로 리스트, 딕셔너리를 쓰고 싶다면 None으로 기본값을 준 뒤에 함수 내부에서 새로 생성해서 쓴다.

    def register_user(name, name_list=None):
        if name_list is None:
           name_list = []
        name_list.append(name)
        return name_list

키워드 매개변수 keyword arguments
- 명시적으로 지정해서 전달 
- 위치 기반(positional)으로 호출 할 수도 잇지만 순서가 뒤바뀔 수 있으니 
  키워드로 호출하기 


함수의 값 복사와 레퍼런스 복사	
call by object reference 
파이썬 변수는 변수에 값을 담을 때 메모리 주소(레퍼런스)를 가리킨다. 

불변 객체: tuple, int, float, str 
- 기존 메모리 값 수정이 아니라 새로운 공간에 값을 쓰고 주소 다르게 가리킴

가변 객체: 리스트, 딕셔너리, 세트 
- 변수 복사시 메모리 주소(레퍼런스)를 공유함. 
- 복사본 수정하면 원본도 수정됨 주의

얕은 복사 shallow copy - copy()
- 가장 바깥쪽 껍데기만 다른 주소이고, 내부 객체들은 주소 공유함 
깊은 복사 deep copy - copy.deepcopy() 
- 실무에서 JSON 데이터 등 복사시 
- import copy 
=================================================

def register_user(name, age, email, address):

register_user("kim", 12, "test@gmail.com", "blah")
register_user(name="kim", age=12, email="test@gmail.com", address="blah")


import copy

original_users = [
    {"name": "Kim", "grade": "Silver", "history": ["login", "buy"]},
    {"name": "Lee", "grade": "Silver", "history": ["login"]}
]

# upgraded_users = copy.deepcopy(original_users)
upgraded_users = original_users.copy()

for user in upgraded_users:
    user["grade"] = "Gold"
    user["history"].append("bonus_point")

print("original===")

for user in original_users:
    print(user)

print("upgraded===")
for user in upgraded_users:
    print(user)