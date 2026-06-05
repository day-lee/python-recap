# 클래스: 가공할 데이터와 함수들을 하나로 묶어놓은 설계도

# 객체(Object, Instance): 설계도로 실제 메모리에 만든 알맹이 

# __init__: 초기화 생성자. self는 지금 막 만든 나 자신 

# 메소드: 객체 전용 함수. 항상 첫번째 인자로 self를 받아서 객체 본인의 데이터에 접근함.

# isinstance(instance, Class): 이 객체가 이 설계도로 만든게 맞는지 혈통 확인하는 함수  

# 매직 메소드: 파이썬 시스템이 뒤에서 자동으로 호출해주는 __ 언더 스코어 두개 붙은 특수 메소드. 
#     __str__ 을 쓰면 print()로 출력할 때 어떻게 보여줄지 정의 할 수 있다. 안그러면 <__main__.Product object...> 이런 형태로 나옴 


# 클래스 변수: 모든 객체가 공동으로 소유하는 단 하나의 변수 
# 클래스 메소드: 클래스 전체를 대표해 일하는 함수 @ 데코레이터 붙임 

# 프라이빗 변수: 외부에서 함부로 데이터를 수정하지 못하도록 변수 이름을 숨기는 것 변수명 앞에 __ 더블언더바

# 게터/세터: 숨긴 프라이빗 변수를 조회(getter)하거나 수정(setter)할 때
# @property 데코레이터 문법을 사용함

# 상속 Inheritance: 기존에 만든 클래스를 그대로 물려받아서 새로운 기능 추가해서 자식을 만드는 것 



# class Product:
#     count = 0 #클래스 변수 

#     def __init__(self, name, price):
#         self.name = name 
#         self.__price = price  # private 프라이빗 변수 
    
#     def __str__(self):
#         return f"[상품] {self.name}"

#     def get_discounted_price(self, discount_rate):
#         return self.price * (1 - discount_rate)

#     @classmethod 
#     def get_total_count(cls): #cls 클래스 자체를 뜻함
#         return cls.count
    
#     @property # getter 게터
#     def price(self):
#         return self.__price 
    
#     @price.setter # setter 세터 
#     def price(self, new_price):
#         if new_price < 0:
#             raise ValueError("가격은 음수 일 수 없다.")
#         self.__price = new_price 


# # 상속 
# class DeliberyProduct(Product): # Product 상속받음 
#     def __init__(self, name, price, delivery_fee):
#         super().__init__(name, price) # 부모 생성자 호출해서 이름, 가격 세팅
#         self.delivery_fee = delivery_fee # 자식만의 데이터 추가 

# =========================================================

"""
[클래스 초급 미션: 배송 상태 관리 객체 만들기]

상황:
쇼핑몰의 배송 상태를 관리하는 `Delivery` 클래스를 작성하려고 합니다.
배송 아이템의 이름과 현재 상태를 저장하고, 배송 상태를 업데이트하는 기능을 구현하세요.

요구사항:
1. `Delivery` 클래스를 선언하세요.
2. 생성자 (`__init__`)를 구현하세요.
   - 인자로 `item_name`을 받아서 `self.item_name`에 저장하세요.
   - 배송 상태를 나타내는 `self.status` 변수도 만들고, 초기값은 무조건 "배송 준비 중"으로 설정하세요.
3. 메소드 (`update_status`)를 구현하세요.
   - 인자로 새로운 상태(`new_status`)를 받아서 `self.status`를 변경하는 기능을 합니다.
"""

# 1.여기에 Delivery 클래스를 작성해보세요.
class Delivery:
    def __init__(self, item_name, status="배송 준비 중"):
        self.item_name = item_name 
        self.status = status 

    def update_status(self, new_status):
        self.status = new_status
# ==============================================================================
# [테스트 실행 코드] - 아래 코드가 오류 없이 실행되어야 합니다.
# ==============================================================================
if __name__ == "__main__":
    # 객체 생성 (생성자 호출)
    my_delivery = Delivery("기계식 키보드")
    
    # 초기 상태 확인
    print(f"상품명: {my_delivery.item_name}") 
    print(f"현재 상태: {my_delivery.status}")  # 예상 출력: 배송 준비 중
    
    print("-" * 30)
    
    # 메소드를 호출하여 배송 상태 업데이트
    my_delivery.update_status("배송 중")
    print(f"업데이트 후 상태: {my_delivery.status}")  # 예상 출력: 배송 중

