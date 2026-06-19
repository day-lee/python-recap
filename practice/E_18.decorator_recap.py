"""
[복습 미션: 쿠폰 적용 및 유저 정제 시스템]

상황:
장바구니에 담긴 상품 튜플 리스트와 유저의 쿠폰 정보(딕셔너리)가 있습니다.
총 결제 금액을 계산하고, 쿠폰 적용 여부를 로그로 남기는 시스템을 완성하세요.

미션:
1. 데코레이터 구현 (`@coupon_logger`)
   - 원본 함수가 계산해서 반환한 [최종 금액]을 중간에 받으세요.
   - "--- 적용 후 금액: {최종금액}원 ---"을 출력한 뒤, 그 [최종 금액]을 안전하게 다시 반환(return)하세요.

2. 메인 함수 구현 (`calculate_checkout`)
   - 이 함수는 여러 개의 (상품명, 가격) 튜플들을 가변 인자(`*args`)로 받습니다.
   - 함수 정의 시 `user_coupon`이라는 키워드 인자(딕셔너리 형태)도 함께 받습니다.
   - 복습 포인트 ①: `for`문 내부가 아닌, `for`문 시작할 때 바로 튜플 언패킹을 사용해 가격을 더하세요.
   - 복습 포인트 ②: `user_coupon` 딕셔너리에서 `.get()`을 사용하여 "discount" 키의 값을 가져오세요.
     * 만약 "discount" 키가 없거나 빈 값(0 등)이라면 할인 금액을 0으로 처리하세요.
   - 최종 계산된 금액(총 상품 금액 - 할인 금액)을 반환(return)하세요.
"""
   pass
















# def coupon_logger(func):
#    def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"--- 적용 후 금액: {result}원 ---")
#         return result
#    return wrapper

# @coupon_logger
# def calculate_checkout(*args, user_coupon=None):
#    total = 0
#    # underscore for ignoring the variable 
#    for _, price in args:
#        total += price 
#    # in case, user_coupon is None, 디폴트로 정해놓음 
#    if user_coupon is None: 
#        user_coupon = {}
#    discount = user_coupon.get("discount", 0)
#    return total - discount

"""
# 1. 데코레이터 (값 전달 복습)
def coupon_logger(func):
    def wrapper(*args, **kwargs):
        # 여기에 원본 함수 결과를 받고, 출력 후 다시 반환하는 로직을 짜보세요.
        result = func(*args, **kwargs)
        print(f"--- 적용 후 금액: {result}원 ---")
        return result
    return wrapper

# 2. 메인 함수 (튜플 언패킹 & dict.get 복습)
@coupon_logger
def calculate_checkout(*args, user_coupon=None):
    if user_coupon is None:
        user_coupon = {}
        
    total_price = 0
    # 2-1. for문 라인에서 바로 튜플 언패킹을 사용해 total_price를 구하세요.
    for _, price in args:
        total_price += price
    
    # 2-2. dict.get()을 활용해 "discount" 값을 안전하게 가져오세요 (없으면 0).
    discount = 0
    discount = user_coupon.get("discount", 0)
    
    return total_price - discount
"""

# ==============================================================================
# [테스트 실행 코드]
# ==============================================================================
if __name__ == "__main__":
    item1 = ("맥북", 2000000)
    item2 = ("마우스", 100000)
    
    # 케이스 A: 쿠폰이 정상적으로 있는 유저
    coupon_a = {"coupon_name": "신규가입쿠폰", "discount": 50000}
    res_a = calculate_checkout(item1, item2, user_coupon=coupon_a)
    print(f"결과 A: {res_a}\n") # 예상 결과: 2050000
    
    # 케이스 B: 쿠폰 정보에 할인 금액(discount) 키가 누락된 유저
    coupon_b = {"coupon_name": "멤버십쿠폰"} 
    res_b = calculate_checkout(item1, item2, user_coupon=coupon_b)
    print(f"결과 B: {res_b}\n") # 예상 결과: 2100000

    # 케이스 C: 쿠폰 정보가 아예 없음 
    res_b = calculate_checkout(item1, item2)
    print(f"결과 C: {res_b}\n") # 예상 결과: 2100000
