__딕셔너리의 items() 함수와 반복문 조합하기	
# 딕셔너리에 키-벨류 페어를 추가할 떄 my_dict["color"] = "black" 처럼 추가한다. 

2. [중급 실무] 딕셔너리 리스트를 특정 Key 기준으로 정렬하기 (key 옵션)실무에서는 단순 숫자 리스트보다 딕셔너리가 담긴 리스트를 훨씬 많이 씁니다. 이때 "어떤 Key를 기준으로 줄 세울 것인가"를 지정을 해줘야 하는데, 파이썬의 lambda(람다) 함수와 조합해서 사용합니다.python# DB에서 가져온 상품 정보 데이터
products = [
    {"name": "키보드", "price": 45000, "stock": 12},
    {"name": "마우스", "price": 23000, "stock": 5},
    {"name": "모니터", "price": 280000, "stock": 2}
]

# 비즈니스 로직: '가격(price)이 낮은 순'으로 정렬하기
# lambda x: x["price"] 는 "리스트 안의 요소(x)에서 price 값을 기준으로 삼아라"라는 뜻입니다.
sorted_by_price = sorted(products, key=lambda x: x["price"])

print("⬇️ 가격 낮은 순 정렬 결과:")
for p in sorted_by_price:
    print(p)

# 출력 결과:
# {'name': '마우스', 'price': 23000, 'stock': 5}
# {'name': '키보드', 'price': 45000, 'stock': 12}
# {'name': '모니터', 'price': 280000, 'stock': 2}
Use code with caution.📝 바로 풀어보는 쇼핑몰 백엔드 실습 문제쇼핑몰에서 가장 중요한 비즈니스 로직인 재고 부족 경고 시스템을 정렬로 구현해 보세요.현재 물류창고에 남아있는 상품들의 재고 리스트가 있습니다. 재고(stock)가 가장 적게 남은 상품부터 순서대로 정렬된 새로운 리스트 low_stock_alerts를 만들어 보세요.주어진 데이터:pythoninventory = [
    {"item": "애플워치", "stock": 8},
    {"item": "아이패드", "stock": 3},
    {"item": "맥북프로", "stock": 15},
    {"item": "에어팟Pro", "stock": 1}
]
Use code with caution.조건:원본 데이터인 inventory 리스트는 순서가 변하지 않도록 그대로 유지해야 합니다. (sorted() 함수를 사용하세요!)key 옵션에 람다 함수를 사용해 각 딕셔너리의 "stock" 값을 기준으로 오름차순 정렬하세요.목표 결과 리스트:python# 정렬된 low_stock_alerts 결과:
# [
#     {"item": "에어팟Pro", "stock": 1},
#     {"item": "아이패드", "stock": 3},
#     {"item": "애플워치", "stock": 8},
#     {"item": "맥북프로", "stock": 15}
# ]
Use code with caution.중급 실무 유형이지만 위의 힌트 구조를 참고하면 한 줄로 멋지게 짜내실 수 있습니다. 코드를 완성해서 공유해 주세요!AI responses may include mistakes. Learn more