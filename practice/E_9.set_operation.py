"""
==============================================================================
[라이브 코딩 인터뷰 문제] 신규 서비스 가입 이벤트 대상자 추출기

[상황] 
우리 회사에서 신규 서비스를 출시하면서 마케팅 이벤트를 진행하려고 합니다.
기존에 'A 서비스'를 이용하던 회원 명단과 'B 서비스'를 이용하던 회원 명단이 
각각 리스트 형태로 들어왔습니다.

A_service_users = ["kim", "lee", "park", "choi"]
B_service_users = ["park", "choi", "jung", "kang"]

[문제] 
두 서비스의 유저 명단을 분석하여 다음 3가지 결과 집합(Set)을 반환하는 
함수 extract_event_targets(list_a, list_b)를 작성하세요.

1. 두 서비스를 '모두' 이용하고 있는 충성 고객 명단 
2. 두 서비스 중 '적어도 하나'를 이용하고 있는 전체 고객 명단 
3. 'A 서비스만' 이용하고 있는 고객 명단 


==============================================================================
"""
def extract_event_targets(list_a, list_b):
    pass 












    # 1. 두 서비스를 '모두' 이용하고 있는 충성 고객 명단 (교집합)
    # 2. 두 서비스 중 '적어도 하나'를 이용하고 있는 전체 고객 명단 (합집합)
    # 3. 'A 서비스만' 이용하고 있는 고객 명단 (차집합)


    # user_set_a = set(list_a)
    # user_set_b = set(list_b)

    # both = user_set_a & user_set_b 
    # either = user_set_a | user_set_b  
    # only_a = user_set_a - user_set_b 

    # return both, either, only_a

    # a_user_set = set(list_a)
    # b_user_set = set(list_b)
    # both, either, only_a = a_user_set & b_user_set, a_user_set | b_user_set, a_user_set - b_user_set
    # return both, either, only_a

# [제한 조건 및 필수 요구사항]
# 1. 일반적인 for문이나 if문을 쓰지 말고, 파이썬 집합(Set)의 고유 연산자 기호
#    (&, |, -)를 반드시 활용하여 한 줄씩 깔끔하게 풀어내야 합니다.
# 2. 최종 반환값은 (교집합, 합집합, 차집합) 형태의 '튜플'로 한 번에 리턴하세요.

    # set_a = set(list_a)
    # set_b = set(list_b)
    # both, either, only_a = set_a & set_b, set_a | set_b, set_a - set_b 
    # return both, either, only_a

    # set_a = set(list_a)
    # set_b = set(list_b) 
    # both_users, either_users, a_only_users = set_a &  set_b, set_a |  set_b, set_a - set_b
    # return (both_users, either_users, a_only_users)

#     # [1단계] 우선 들어온 리스트 두 개를 집합(Set) 보따리로 변환합니다.
#     # 힌트: set(list_a) 문법을 사용해서 각각 set_a, set_b라는 변수에 담아보세요.
#     set_a = set(list_a)
#     set_b = set(list_b)
    
#     # [2단계] 집합 연산자 기호를 사용하여 각각의 타겟을 추출합니다.
#     # 힌트 1 (교집합): set_a & set_b
#     # 힌트 2 (합집합): set_a | set_b
#     # 힌트 3 (차집합): set_a - set_b
#     both_users, either_users, only_a_users = set_a & set_b, set_a | set_b, set_a - set_b 
#     return both_users, either_users, only_a_users 
    
    # [3단계] 구한 3개의 집합을 한 보따리로 묶어서 리턴합니다.
    # 힌트: 파이썬 함수에서 return 변수1, 변수2, 변수3 구조로 쓰면 자동으로 튜플 패킹이 됩니다!
    

# ------------------------------------------------------------------------------
# 면접관의 채점 및 실행 코드 (수정하지 마세요)
# ------------------------------------------------------------------------------
A_service_users = ["kim", "lee", "park", "choi"]
B_service_users = ["park", "choi", "jung", "kang"]

# 함수 실행 (3개의 결과가 튜플로 한 보따리에 묶여서 나옵니다)
both, either, only_a = extract_event_targets(A_service_users, B_service_users)

print(f"1. 모두 이용 (교집합): {both}")
print(f"2. 적어도 하나 이용 (합집합): {either}")
print(f"3. A만 이용 (차집합): {only_a}")

"""
[정상 출력 예시]
1. 모두 이용 (교집합): {'park', 'choi'}
2. 적어도 하나 이용 (합집합): {'kim', 'lee', 'park', 'choi', 'jung', 'kang'}
3. A만 이용 (차집합): {'kim', 'lee'}
(※ 집합의 특성상 내부 원소들의 출력 순서는 바뀔 수 있습니다.)
"""
