"""
[상황]서버에 가입을 요청한 유저들의 이메일 리스트가 들어왔습니다. 그런데 이 리스트에는 가입 형식이 잘못된 불량 데이터(형식 오류)와 이미 가입된 기존 회원(중복 데이터)이 섞여 있습니다.

[문제]이 리스트를 순서대로 검사하여 올바른 이메일만 골라내고, 중복을 제거한 최종 가입 대상자들의 집합(Set)을 반환하는 함수 process_signups를 작성하세요.


[제한 조건 및 예외 규칙 (필수 요구사항)]
이메일에 골뱅이 기호(@)가 포함되어 있지 않으면 올바르지 않은 이메일입니다. @가 없는 이메일을 만났을 때는 파이썬 내장 에러인 ValueError를 의도적으로 발생(raise) 시키세요.

루프 내부에서 이 ValueError가 발생했을 때 프로그램이 멈추지 않도록 try-except 문으로 에러를 안전하게 포획(catch)하고, 화면에 에러 로그를 출력한 뒤 다음 이메일로 넘어가야 합니다.

최종 결과물은 중복이 없는 집합(Set) 형태여야 합니다.

[경고] 잘못된 이메일 형식입니다: invalid_email_1
[경고] 잘못된 이메일 형식입니다: invalid_email_2

최종 가입 대상자: {'alex@gmail.com', 'bob@naver.com', 'charlie@daum.net'}
(※ 집합의 특성상 순서는 바뀔 수 있습니다.)
 
"""
def process_signups(email_list):
    pass














    # # pass 새로운 set를 만들기, 세트에 요소하나를 추가할 때 쓰는 메서드 
    # new_email_list = set()
    # for email in email_list:
    #     try:
    #         if "@" not in email:
    #             raise ValueError(f"[경고] 잘못된 이메일 형식입니다: {email}")
    #         new_email_list.add(email)
    #     except ValueError as e:
    #         print(e)

    # return new_email_list

#     signup_set = set()
#     for email in email_list:
#         try: 
#             if '@' not in email:
#                 raise ValueError(f"올바르지 않은 이메일 입니다.: {email}")
#             signup_set.add(email)
#         except ValueError as e:
#             print(e)
#     return signup_set

# def process_signups(email_list):
#     result = set()
#     for email in email_list:
#         try:
#             if '@' not in email:
#                 raise ValueError(f"[경고] 잘못된 이메일 형식입니다: {email}")
#             result.add(email)
#         except ValueError as e:
#             print(e) 
#     return result

# def process_signups(email_list):
#     valid_emails = set()
#     for email in email_list: 
#         try:
#             if '@' not in email:
#                 raise ValueError(f"잘못된 이메일 형식입니다:{email}")   
#             valid_emails.add(email)
#         except ValueError as e:
#             print(e)
#     return valid_emails

"""
def process_signups(email_list):
    # 1. 결과를 담을 빈 집합(Set)을 만듭니다. (힌트: set() 사용)
    valid_emails = set()
    for email in email_list:
        # 이 공간에 코드를 작성하세요.
        # 힌트 1: try-except 구조를 만드세요.
        # 힌트 2: if "@" not in email: 상황일 때 raise ValueError("에러메시지")를 실행하세요.
        # 힌트 3: 집합에 요소를 추가할 때는 .add() 메서드를 씁니다.
        try:
            if "@" not in email:
                raise ValueError(f"잘못된 이메일 형식입니다: {email}")
            
            valid_emails.add(email)
        except ValueError as e:
            print(e)
    return valid_emails
"""

# --- 면접관의 채점 및 실행 코드 ---
signup_requests = ["alex@gmail.com", "invalid_email_1", "bob@naver.com", "alex@gmail.com", "invalid_email_2", "charlie@daum.net"]

result = process_signups(signup_requests)
print(f"\n최종 가입 대상자: {result}")
