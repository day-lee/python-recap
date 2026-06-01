"""
==============================================================================
[라이브 코딩 인터뷰 문제] 안전한 은행 계좌 정보 업데이트 시스템

[상황] 
우리 은행 시스템에서 고객의 계좌 정보(고객명, 계좌번호, 잔액)를 
안전하게 보관하기 위해 수정이 불가능한 '튜플(Tuple)' 형태로 관리하고 있습니다.

account_info = ("Kim", "123-456-789", 50000)

신입 개발자가 고객의 잔액을 업데이트하겠다며 이 튜플의 값을 직접 수정하는 
코드를 작성하여 시스템에 에러가 발생할 위기에 처했습니다.

[문제] 
튜플의 값을 강제로 변경하려고 할 때 파이썬이 던지는 에러를 안전하게 포획(try-except)하고,
대신 튜플을 새로 안전하게 갱신하여 반환하는 함수 update_balance를 완성하세요.

[제한 조건 및 필수 요구사항]
1. try 블록 안에서 `account_info[2] = new_balance`를 직접 실행하여 
   파이썬이 일부러 에러를 터트리게 만드세요.
2. 튜플 수정 시 발생하는 파이썬 내장 에러인 'TypeError'를 except 문으로 정확히 잡으세요.
3. except 블록 안에서 에러 메시지를 출력한 뒤, 튜플의 '불변성'을 우회하기 위해
   기존 튜플의 정보와 새 잔액을 조합한 '새로운 튜플'을 만들어 return 하세요.

==============================================================================
"""
def update_balance(account_info, new_balance):
    pass







# def update_balance(account_info, new_balance):
#     try:
#         account_info[2] = new_balance
#     except TypeError as e:
#         print("error!")
#     name, account, __name__ = account_info 
#     return name, account, new_balance

# def update_balance(account_info, new_balance):
#     try:
#         account_info[2] = new_balance
#     except TypeError as e:
#         print(f"에러 포획 성공 {e}")
#     name, account, _ = account_info 
#     return (name, account, new_balance)

# def update_balance(account_info, new_balance):
#     """
#     [1단계] try 블록을 만들고 튜플 변경을 시도합니다.
#     힌트: account_info[2] = new_balance 코드를 여기에 넣으면 TypeError가 발생합니다.
#     [2단계] 튜플 수정 실패 에러(TypeError)를 안전하게 잡습니다.
#     힌트: except TypeError as e: 구조를 사용하세요.
#     """
#     try:
#         account_info[2] = new_balance        

#     except TypeError as e: 
#         # 에러 메시지를 화면에 출력(print)해줍니다.
#         print(e)
        
#         # [3단계] 튜플은 수정이 안 되므로, 기존 데이터와 새 잔액을 엮어 '새 튜플'을 만들어 리턴합니다.
#         # 힌트: account_info[0], account_info[1] 정보와 new_balance를 한 보따리로 묶으세요.
#         # (괄호를 써서 묶어 리턴하면 명시적인 튜플이 됩니다!)
#         return (account_info[0], account_info[1], new_balance)



# ------------------------------------------------------------------------------
# 면접관의 채점 및 실행 코드 (수정하지 마세요)
# ------------------------------------------------------------------------------
# (고객명, 계좌번호, 현재잔액)
old_account = ("Kim", "123-456-789", 50000)

# 잔액을 70,000원으로 업데이트 시도
updated_account = update_balance(old_account, 70000)
print(f"최종 계좌 정보: {updated_account}")

"""
[정상 출력 예시]
[에러 포획 성공] 튜플은 수정할 수 없습니다. 원본 에러: 'tuple' object does not support item assignment
최종 계좌 정보: ('Kim', '123-456-789', 70000)
"""
