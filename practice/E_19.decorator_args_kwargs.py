"""
[미니 프로젝트: 커머스 주문 데이터 정제 파이프라인]

상황:
여러 마케팅 채널에서 들어온 대용량 주문 로그 데이터를 정제하여 
실제 결제 시스템으로 넘겨주는 함수를 작성해야 합니다.

미션:
1. 데코레이터 구현 (`@performance_tracker`)
   - 함수가 시작될 때 "--- 파이프라인 가동 ---"을 출력하세요.
   - 함수가 끝날 때 "--- 파이프라인 종료 ---"를 출력하세요.
   - 원본 함수의 반환값을 가로채지 않고 안전하게 최종 반환하세요.

2. 메인 함수 구현 (`process_order_pipeline`)
   - 이 함수는 여러 개의 주문 데이터(튜플 형태)를 가변 인자(`*args`)로 받습니다.
   - 각 주문 데이터는 `(주문ID, 회원등급, 주문금액)` 형태의 튜플입니다.
   - 데이터 검증 (try-except 필수):
     * 만약 주문금액이 `0` 이하이거나 숫자가 아닌 경우 `ValueError`를 발생시키고, 
       "[_오류_] {주문ID}: 올바르지 않은 금액"을 출력한 뒤 다음 주문으로 넘어가세요.
   - 결과물 반환:
     * 정상적으로 통과한 주문자들의 '회원등급'만 모아서 **중복이 없는 세트(set)** 형태로 반환하세요.
"""
# 핵심은 우리가 원본 함수를 호출한다고 생각하지만, 실제로는 wrapper 함수를 호출하고 있다는 점을 이해 
# 함수를 리턴하고, 이름을 바꿔치기하는 파이썬의 동작 원리

# 1. 데코레이터 구현
def performance_tracker():
    pass
# 2. 파이프라인 메인 함수 구현 (데코레이터를 적용하세요)
@performance_tracker
def process_order_pipeline():
    pass









# # 1. 데코레이터 구현
# def performance_tracker(func):
#     def wrapper(*args, **kwargs):
#         print("--- 파이프라인 가동 ---")
#         result = func(*args, **kwargs)
#         print("--- 파이프라인 종료 ---")
#         return result 
#     return wrapper


# try-except는 For 문 내부에 위치해야한다. 외부에 있으면 한번만 적용이 되니까. 
# # 2. 파이프라인 메인 함수 구현 (데코레이터를 적용하세요)
# @performance_tracker
# def process_order_pipeline(*args):
#     result = set()
#     for id, status, amount in args:
#         try:
#             if not isinstance(amount, int) or amount <= 0 :
#                 raise ValueError(f"[_오류_] {id}: 올바르지 않은 금액")
#             result.add(status)
#         except (ValueError) as e:
#             print(e)
#     return result 

# # 1. 데코레이터 구현
# def performance_tracker(func):
#     # wrapper 보따리에 인자들 다 받아서 오리지널 함수에 보내준다. 
#     # *args, **kwarg를 설정하면 인자가 몇 개든 다 받아줄 수 있는 그릇이 생김
#     # 습관적으로 *args, **kwargs 넣어주기 
#     def wrapper(*args, **kwargs):
#         print("--- 파이프라인 가동 ---")
#         result = func(*args, **kwargs)
#         print("--- 파이프라인 종료 ---")
#         return result
#     return wrapper


# # 2. 파이프라인 메인 함수 구현 (데코레이터를 적용하세요)
# @performance_tracker
# def process_order_pipeline(*args):
#     result_user_level = set()
#     for id, level, order_amount in args:
#         try:
#             if not isinstance(order_amount, int) or order_amount <= 0 :
#                 raise ValueError(f"[_오류_] {id}: 올바르지 않은 금액")
#             result_user_level.add(level)
#         except ValueError as e:
#             print(e)
#     return result_user_level
# ==============================================================================
# [테스트 실행 코드]
# ==============================================================================
if __name__ == "__main__":
    # (주문ID, 회원등급, 주문금액)
    order1 = ("ORD_01", "VIP", 150000)
    order2 = ("ORD_02", "SILVER", -500)      # 금액 에러 (음수)
    order3 = ("ORD_03", "GOLD", 80000)
    order4 = ("ORD_04", "SILVER", "10000원") # 금액 에러 (문자열 소속)
    order5 = ("ORD_05", "VIP", 200000)       # 등급 중복
    
    # 파이프라인 함수를 호출하여 결과를 확인해보세요.
    result_grades = process_order_pipeline(order1, order2, order3, order4, order5)
    
    print("\n[최종 추출된 회원 등급 리스트]")
    print(result_grades)
    
    # 예상 출력 결과:
    # --- 파이프라인 가동 ---
    # [_오류_] ORD_02: 올바르지 않은 금액
    # [_오류_] ORD_04: 올바르지 않은 금액
    # --- 파이프라인 종료 ---
    # 
    # [최종 추출된 회원 등급 리스트]
    # {'GOLD', 'VIP'}  (또는 {'VIP', 'GOLD'} 순서 상관없음)
