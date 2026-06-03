# 괄호가 없이 콤마만 있어도 튜플이었지. 
# my_tuple = 1, "hi"
# num, greet = my_tuple
# print(num, greet)

# 리스트 언패킹
# my_list = [1, "hey"]
# num2, greet2 = my_list
# print(num2, greet2)

# 안쓸 값은 언더스코어로 만들어서 리스트 언패킹 
# my_list = [1, "k", 3]
# _, name, num = my_list
# print(name, num)


"""
[문제]이 orders 데이터를 받아서 각 상품의 '총 금액(수량 * 가격)'을 계산하고, 아래 [출력 예시]와 같이 멋지게 출력하는 함수 process_orders를 작성하세요.
[제한 조건 (필수 요구사항)]함수 정의 시 가변 인자(*args)를 활용하여 인자를 받아야 합니다.
함수 내부에서 데이터를 처리할 때, 인덱스 접근(예: item[0], item[1])을 쓰지 말고 오늘 배운 '튜플 언패킹(Tuple Unpacking)'을 활용하여 변수명을 명확히 지정해 주세요.
출력예시
# [주문 확인] M4 맥북 프로 총 금액: 3500000원
# [주문 확인] 아이폰 17 총 금액: 2800000원
# [주문 확인] 에어팟 프로 총 금액: 900000원
"""
# 가변 인자
# 함수 정의시에 *args는 튜플로 패킹 묶음으로 모아줌 
# 함수 호출시에 *args는 언패킹해서 포지셔널 인자로 보내줌 


def process_orders(*args):
    pass





# --- 면접관의 채점 및 실행 코드 ---
orders = [
    ("M4 맥북 프로", 1, 3500000),
    ("아이폰 17", 2, 1400000),
    ("에어팟 프로", 3, 300000)
]

함수 호출 here


# ============================================

#    for product, qty, price in args:
#       print(f"주문 확인 {product} 총 금액: {qty * price}")
# process_orders(*orders)

# def process_orders(*orders):
#     print(orders)
#     for product, quantity, price in orders:
#         print(f"[주문 확인] {product} 총 금액: {quantity * price}" )
 
# # --- 면접관의 채점 및 실행 코드 ---
# orders = [
#     ("M4 맥북 프로", 1, 3500000),
#     ("아이폰 17", 2, 1400000),
#     ("에어팟 프로", 3, 300000)
# ]
# process_orders(*orders)

# def process_orders(*args):
#     for product, amount, price in args: 
#         print(f"[주문 확인] {product} 총 금액: {amount*price}")

# 가변인자 variable length argument
# 함수 정의할때 패킹
# 호출할때는 언패킹 

# def process_orders(*orders):
#     print(orders)
#     for product, amount, price in orders:
#         print(f"[주문 확인] {product} 총 금액: {price * amount}")


# # --- 면접관의 채점 및 실행 코드 ---
# # orders = [
# #     ("M4 맥북 프로", 1, 3500000),
# #     ("아이폰 17", 2, 1400000),
# #     ("에어팟 프로", 3, 300000)
# # ]
# orders = (("M4 맥북 프로", 1, 3500000),
#     ("아이폰 17", 2, 1400000),
#     ("에어팟 프로", 3, 300000))

# # 함수를 호출할 때도 '별표 언패킹(*)'을 활용해서 보따리를 풀어서 던져야 합니다!
# process_orders(*orders)


