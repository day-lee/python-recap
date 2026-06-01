"""
🛍️ 실무 상황 시나리오
쇼핑몰 관리자 페이지에는 "상품 등록 함수"와 "결제 취소 함수"가 있어. 이 함수들은 너무 중요해서, 로그인한 유저의 역할(Role)이 "ADMIN"(관리자)인 사람만 실행할 수 있어야 해.일반 "USER"가 접근하면 "접근 권한이 없습니다!"라는 에러 메시지를 뿜으며 차단해야 하지.
"""
# 1. 테스트용 유저 데이터 (딕셔너리 구조)
admin_user = {"name": "Kim", "role": "ADMIN"}
normal_user = {"name": "Lee", "role": "USER"}



# 2. 관리자 권한을 체크해 주는 데코레이터 함수 만들기
def admin_required(original_func):
    pass
    언패킹 하지 않고 안전하게 인자 꺼내와서 쓰기, 일반 유저 필터링 먼저  







#     def wrapper(*args, **kwargs):
#         user = args[0]      #안전한 방식으로 첫 번째 인자를 유저 정보로 꺼내오기 (args[0])
#         if user["role"] != "ADMIN":
#             print(f"{user['name']}님은 접근 권한이 없습니다.")
#             return None
#         result = original_func(*args, **kwargs)
#         return result
#     return wrapper 

    
    # # [Q1] 원본 함수에 어떤 인자가 들어올지 모르니 '만능 배달원 그릇'을 매개변수에 적어줘!
    # def wrapper(*args, **kwargs):
        
    #     # 첫 번째 인자로 무조건 '유저 딕셔너리(user)'가 들어온다고 가정할게.
    #     # args의 첫 번째 원소(args[0])를 꺼내서 유저 정보를 확인해.
    #     user = args[0]
        
    #     # [Q2] 유저의 role이 "ADMIN"인지 확인하는 조건문을 짜봐!
    #     if user["role"] == "ADMIN":
    #         # [Q3] 권한이 맞으면 알맹이(원본 함수)를 인자들과 함께 실행하고 그 결과를 리턴해줘!
    #         return original_func(*args, **kwargs)
    #     else:
    #         # 권한이 없으면 경고 메시지 출력 후 종료 (None 리턴)
    #         print(f"❌ [보안 경고] {user['name']}님은 접근 권한이 없습니다!")
    #         return None
            
    # return wrapper


# --------------------------------------------------
# 3. 데코레이터 적용

@admin_required
def add_product(user, product_name):
    print(f"📦 관리자 {user['name']}님이 신상품 [{product_name}]을 성공적으로 등록했습니다.")

@admin_required
def cancel_order(user, order_id):
    print(f"💳 관리자 {user['name']}님이 주문 번호 [{order_id}]를 취소했습니다.")


# 4. 테스트 실행 (시니어가 미리 짜둠)
print("--- 1. 관리자 Kim의 요청 ---")
add_product(admin_user, "M4 맥북 프로")

print("\n--- 2. 일반 유저 Lee의 요청 ---")
cancel_order(normal_user, "ORDER_12345")
