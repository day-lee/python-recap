"""
[실무형 데코레이터 문제: 사용자 권한 체크 및 인자 로깅]

요구사항:
1. `@check_permission` 데코레이터를 구현하세요.
2. 데코레이터 내부 `wrapper` 함수는 가변 인자(`*args`, `**kwargs`)를 모두 받아야 합니다.
3. 원본 함수가 실행되기 전에 키워드 인자(`kwargs`)에서 `user_role` 값을 꺼내오세요.
4. 만약 `user_role`이 "admin"이 아니라면, 원본 함수를 실행하지 않고 
   "권한 거부: 관리자만 접근 가능합니다."라는 문자열을 즉시 반환(return)하세요.
5. `user_role`이 "admin"이 맞다면, 원본 함수를 실행하고 그 결과를 반환하세요.
"""
def check_permission(func):
    # 가변 인자를 받을 수 있도록 내부 함수를 구성하세요.



# def check_permission(func):
#     # 가변 인자를 받을 수 있도록 내부 함수를 구성하세요.
#     def wrapper(*args, **kwargs):
#         # 1. kwargs에서 'user_role' 값을 꺼내 확인하는 로직을 작성하세요.
#         # user_role = kwargs["user_role"]
#         # dict.get()을 사용, guest를 기본값으로해 방어적 코드 작성 
#         user_role = kwargs.get("user_role", "guest")
#         # 2. 조건에 따라 원본 함수를 실행하거나 거부 메시지를 반환하세요.
#         if user_role != "admin":
#             return "권한 거부: 관리자만 접근 가능합니다."
#         return func(*args, **kwargs)
#     return wrapper


# ==============================================================================
# [테스트 실행 코드]
# ==============================================================================
@check_permission
def delete_database(user_id, user_role="guest"):
    return f"[성공] {user_id} 님이 데이터베이스를 완전히 삭제했습니다."

if __name__ == "__main__":
    # 1. 권한이 없는 유저가 접근할 때
    print(delete_database("user_01", user_role="guest"))
    # 예상 출력: 권한 거부: 관리자만 접근 가능합니다.

    # 2. 권한이 있는 관리자가 접근할 때
    print(delete_database("admin_master", user_role="admin"))
    # 예상 출력: [성공] admin_master 님이 데이터베이스를 완전히 삭제했습니다.

