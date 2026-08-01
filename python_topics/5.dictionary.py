
dict.items()와 for loop
- for문에서는 dict를 돌리면 key만 나온다. 
- dict.items()와 for문을 사용하면 key, value를 한번에 뽑아올 수 있다.
- for key, value in dict.items():

dict.keys(): dict에서 키만 모아서 돌려준다.
dict.values(): dict에서 값만 모아서 돌려준다.
- 이 함수들은 파이썬 객체, 이터러블 - iterable을 리턴해준다. 
- 리스트처럼 다루려면 list(data_dict.keys()) 처럼 리스트 형태로 변환해줘야한다.

딕셔너리에 키-벨류 페어를 추가할 떄 my_dict["color"] = "black" 처럼 추가한다. 

dict.get()
dict.get(key, default_value_when_no_key)
get()은 "절대 에러를 던지지 않는 안전장치" - KeyError 방지
키가 있으면 진짜 값을 돌려줌
키가 없으면 에러 대신 기본값 메세지 반환 

if key in dict:
    키 존재 여부 확인할 수 있음
    내부적으로 해시 테이블 조회해서 빠름 

딕셔너리 합치기
dict.update(another_dict)
- 원본 수정된다. 

새 딕셔너리 만들기 | 파이프 연산자
new_dict = original_dict | adding_dict
- 오른쪽이 우선하여 양쪽에 같은 키가 있다면 오른쪽 것으로 override 덮어쓴다. 
- 우측(user_input)이 우선권을 가지므로 기본값에 유저 입력이 덮어씌워짐
  final_profile = default_profile | user_input
- 얕은 복사로 참조형 데이터는 복사가 되지 않는다. 

key 옵션: 딕셔너리 리스트를 특정 key 기준으로 정렬하기 
- lambda 함수와 조합 
- sorted(list, key=lambda x: x["price"])
==========================================================

user = {"name": "Kim", "role": "admin"}
for key in user:
    print(key)

for key, value in user.items():
    print(key, value)

sales_summary = {
    "맥북 프로": 3,
    "로지텍 마우스": 12,
    "기계식 키보드": 7
}

for item, count in sales_summary.items():
    print(f"{item} -> {count} 판매 완료")


서버 이름과 현재 CPU 사용량(%) 데이터입니다.
server_status = {
    "Auth-Server": 45,
    "DB-Server": 88,
    "Payment-API": 12,
    "Chat-Bot": 35
}

key = [ key for key in server_status.keys()]
print(key)  

max_usage = max([data for data in server_status.values()])
print(max_usage)

dict.keys(), dict.values() 는 iterable 을 반환하고,
list(), max()는 이터러블을 받아서 연산하므로 if 문 같은 복잡한게 없다면 
바로 사용가능하다. 

key = list(server_status.keys())
max = max(server_status.values())
print(key, max)


==============================================
2. [중급 실무] 딕셔너리 리스트를 특정 Key 기준으로 정렬하기 (key 옵션)실무에서는 단순 숫자 리스트보다 딕셔너리가 담긴 리스트를 훨씬 많이 씁니다. 이때 "어떤 Key를 기준으로 줄 세울 것인가"를 지정을 해줘야 하는데, 파이썬의 lambda(람다) 함수와 조합해서 사용합니다.python# DB에서 가져온 상품 정보 데이터
products = [
    {"name": "키보드", "price": 45000, "stock": 12},
    {"name": "마우스", "price": 23000, "stock": 5},
    {"name": "모니터", "price": 280000, "stock": 2}
]

비즈니스 로직: '가격(price)이 낮은 순'으로 정렬하기
lambda x: x["price"] 는 "리스트 안의 요소(x)에서 price 값을 기준으로 삼아라"라는 뜻입니다.
sorted_by_price = sorted(products, key=lambda x: x["price"])

print("⬇️ 가격 낮은 순 정렬 결과:")
for p in sorted_by_price:
    print(p)

출력 결과:
{'name': '마우스', 'price': 23000, 'stock': 5}
{'name': '키보드', 'price': 45000, 'stock': 12}
{'name': '모니터', 'price': 280000, 'stock': 2}

📝 바로 풀어보는 쇼핑몰 백엔드 실습 문제쇼핑몰에서 가장 중요한 비즈니스 로직인 재고 부족 경고 시스템을 정렬로 구현해 보세요.현재 물류창고에 남아있는 상품들의 재고 리스트가 있습니다. 재고(stock)가 가장 적게 남은 상품부터 순서대로 정렬된 새로운 리스트 low_stock_alerts를 만들어 보세요.주어진 데이터:
pythoninventory = [
    {"item": "애플워치", "stock": 8},
    {"item": "아이패드", "stock": 3},
    {"item": "맥북프로", "stock": 15},
    {"item": "에어팟Pro", "stock": 1}
]
조건:원본 데이터인 inventory 리스트는 순서가 변하지 않도록 그대로 유지해야 합니다. (sorted() 함수를 사용하세요!)
key 옵션에 람다 함수를 사용해 각 딕셔너리의 "stock" 값을 기준으로 오름차순 정렬하세요.

low_stock_alerts = sorted(pythoninventory, key=lambda x: x["stock"])

print(low_stock_alerts)


 정렬된 low_stock_alerts 결과:
[
    {"item": "에어팟Pro", "stock": 1},
    {"item": "아이패드", "stock": 3},
    {"item": "애플워치", "stock": 8},
    {"item": "맥북프로", "stock": 15}
]

# 정렬 기준은 "누적 구매 금액(cash)이 가장 높은 회원부터 내림차순(큰 값부터)" 정렬하는 것
users = [
    {"name": "김철수", "level": "GOLD", "cash": 500000},
    {"name": "이영희", "level": "VIP", "cash": 1200000},
    {"name": "박민수", "level": "SILVER", "cash": 80000},
    {"name": "최수연", "level": "VIP", "cash": 2500000}
]

# 여기에 코드를 작성해 보세요!
vip_lineup = sorted(users, key=lambda user: user["cash"], reverse=True)

print(vip_lineup)

default_setting = {"theme": "light", "alarm": True}
user_setting = {"theme": "dark"}

# 두 딕셔너리를 합친 새로운 객체 생성
final_setting = default_setting | user_setting
print(final_setting)  # {'theme': 'dark', 'alarm': True}
print(default_setting)
print(user_setting)

