익명함수 람다 
- def 함수는 프로그램이 끝날 때 까지 메모리를 차지하는 반면, 
  람다 함수는 실행이 끝나는 순간 메모리에서 사라짐 
- 람다 함수는 일회용. 변수에 할당하지 말기 
- 코드가 두 줄 이상 길어질 것 같다면 def로 만들기 
- 딕셔너리, 튜플 리스트를 정렬할 때 많이 씀 sorted(), sort()

js 의 화살표 익명함수와 동일
(x) => x.stock
lambda x: x["stock"]

sorted(list, key=lambda: item:(-item["key"], item["key2"]))

map, filter, reduce()
- iterable을 다룰 때 필수
- 파이썬에서는 이 함수들 보다는 list comprehension을 선호함 
    map(lambda, list)
    filter(lambda, list)
    reduce(lambda, list)

- <filter object at 0x10479fcd0>, <map object at 0x102fffb50> 
- map, filter 이터러블 오브젝트들은 lazy calculation을 해서 연산을 뒤로 미루므로 주문서 역할을 할 객체 필요
- 이 포인터는 메모리를 적게 차지하고 list(iterable)로 변환해야만 연산이 되고 리스트로 메모리를 차지하게됨
- reduce의 목적은 지금 당장 값 축약이라 이터리블이 아닌 바로 최종 결과 값 만들어냄
- list()로 만들어야 재활용 가능 


===================================================

# 일반 함수
def add(x, y):
    return x + y

# 람다 함수
add_lambda = lambda x, y: x+y 

print(add_lambda(3, 5))  # 출력: 8


numbers = [1, 2, 3, 4]
# 모든 숫자를 제곱하기
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 출력: [1, 4, 9, 16]

# 짝수만 걸러내기
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))
even_no_list = filter(lambda x: x % 2 == 0, numbers)

print(even_no_list)

print(even)
numbers = [1,2,3,4]
squared = map(lambda x: x**2, numbers) 
print(squared) list() 없이 하면 <map object at 0x102fffb50> 이터레이터 객체 자체가 나옴 - 게으른 연산, 일단 준비만 해놓고 메모리에는 안올림. list() 하는 순간 연산. 주소값과 포인터(현위치)정보는 작은 용량의 메모리만 차지하고 있는 중임. 
squared = list(squared)
print(squared)


두 가지 이상의 조건으로 데이터를 정렬할 때 
예) 평점이 높은 순으로 보여주고, 평점이 같다면 가격이 낮은 순으로 정렬

products = [
    {"name": "스마트폰 케이스", "price": 15000, "rating": 4.5},
    {"name": "무선 이어폰", "price": 79000, "rating": 4.8},
    {"name": "블루투스 스피커", "price": 45000, "rating": 4.5},  # 케이스와 평점 같음, 가격은 더 비쌈
    {"name": "보조 배터리", "price": 25000, "rating": 4.8},  # 이어폰과 평점 같음, 가격은 더 저렴
]

# 1. 평점 높은 순, 그다음엔 가격 낮은 순
- 튜플 형태로 다중 조건 지정  
- sorted()는 기본적으로 오름차순이지만 숫자 데이터에서 - 붙여주면 내림차순으로 바꿀 수 있음

rating = sorted(products, key=lambda product: product["rating"], reverse=True)
rating = sorted(products, key=lambda product: -product["rating"])
rating_price = sorted(products, key=lambda product: (-product["rating"], product["price"]))
print(rating_price)

