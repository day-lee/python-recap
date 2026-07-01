"""
[도전 문제: 사내 보안 이벤트 알림 시스템]

상황:
여러 팀에서 동시에 발생한 '보안 경고 이벤트(로그 데이터)'들을 수집하고 가공하는 시스템입니다.
당신은 이벤트 데이터를 안전하게 처리하고 앞뒤로 실행 로그를 남겨야 합니다.

미션:
1. 함수 실행 앞뒤로 "--- LOG START ---", "--- LOG END ---"를 출력하는 데코레이터 `log_decorator`를 만드세요.
2. 메인 함수 `process_security_events`를 설계하세요. 
3. 결과물 반환:
   - 예외를 통과한 정상 데이터 중, level이 "critical"(심각)인 유저들의 이름만 모아서 중복이 없는 '세트(set)' 형태로 반환하세요.
   -> 어떤 예외가 있을 지 생각해보세요. 키, 값, 인자 수 

출력예시: 
--- LOG START ---
[경고] 필수 데이터(user 또는 level)가 누락되었습니다.
[경고] 'david' 유저의 level 값이 비어있습니다.
--- LOG END ---
{'alice'}
"""
def log_decorator():
    pass

def process_security_events():
    pass


















""" 모범답안
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("--- LOG START ---")
        r = func(*args, **kwargs)
        print("--- LOG END ---")
        return r
    return wrapper

@log_decorator
def process_security_events(*args):
    # 아예 데이터 없는 경우
    if not args:
        return set() 
    new_set =set()
    for data in args:

        try: 
            # Guard Clause: 키가 없거나 벨류가 없는 경우 걸러내기, 그다음 핵심 조건 검사하기. 
            # 1 키 없거나 벨류 없는것 부터 걸러내기 
            # 이미 여기서 에러 나옴 KeyError 
            user = data['user']
            level = data['level']

            # if 'user' not in data or 'level' not in data:
            #     print("[경고] 필수 데이터(user 또는 level)가 누락되었습니다.")
            #     continue 
            if not data['user'] or not data['level']:
                user_name = data.get('user', '알 수 없는 유저')
                print(f"[경고] '{user_name}' 유저의 level 값이 비어있습니다.")
                continue 
            # 2 1단계에서 필터링된 것 중에 조건 맞는 것만
            if level == 'critical':
                new_set.add(data['user'])

            # 원래 만든 조건문 
            # if data['user'] is not None and data['level'] == 'critical':
            #     new_set.add(data['user'])

        except (ValueError, TypeError, KeyError) as e:
            print(e)
            continue
    return new_set
"""

#    - 이 함수는 여러 개의 이벤트 데이터(딕셔너리 형태)를 한 번에(가변 인자로) 받습니다.
#    - 각 이벤트 데이터는 `{'user': 'name', 'level': 'critical'}` 같은 형태입니다.
#    - 단, 이벤트 데이터에 `level` 키가 아예 없거나, value가 비어있는 이상한 데이터가 들어오면 에러(KeyError, ValueError 등)를 안전하게 예외 처리(try-except)하고 넘어가야 합니다.
# def log_decorator(original_func):
#     def wrapper(*args):
#         print("--- LOG START ---")
#         result = original_func(*args)
#         print("--- LOG END ---")
#         return result
#     return wrapper

# @log_decorator
# def process_security_events(*args):
#     users = []
#     for data in args:
#         try:
#             level = data["level"]
#             user = data["user"]
#             # 빈 문자열 검사 
#             if not level:
#                 raise ValueError(f"'{user}'")
#             if level == "critical":
#                 users.append(user)

#         except KeyError:
#             print("[경고] 필수 데이터(user 또는 level)가 누락되었습니다.")
#             # 컨티뉴 없어도 포문안에서 다음 차례로 넘아가지만 명시적으로 적어둠.  
#             continue

#         except ValueError:
#             print(f"[경고] {user} 유저의 level 값이 비어있습니다.")
#             continue 

#     return set(users)


# # 1. 데코레이터 정의
# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("--- LOG START ---")
#         result = func(*args, **kwargs)
#         print("--- LOG END ---")
#         return result
#     return wrapper

# # 2. 메인 함수 정의 (위에서 만든 데코레이터를 적용하세요)
# @log_decorator
# def process_security_events(*args):
#     user = []
#     for data in args:
#         try: 
#             # 수동으로 에러 발생시키는 것 보다 data["level"] 하면 알아서 에러 발생 시킴 
#             level = data.get("level")
#             if level is None:
#                 raise KeyError("level 키가 없습니다.")
#             if len(level) == 0:
#                 raise ValueError("값이 없습니다.")
#             if level == "critical":
#                 name = data.get("user")
#                 user.append(name)
#         except (KeyError, ValueError) as e:
#             print(e)
#             continue
#     return set(user)

#    - 단, 이벤트 데이터에 `level` 키가 아예 없거나, value가 비어있는 이상한 데이터가 들어오면 에러(KeyError, ValueError 등)를 안전하게 예외 처리(try-except)하고 넘어가야 합니다.
# 3. 결과물 반환:
#    - 예외를 통과한 정상 데이터 중, level이 "critical"(심각)인 유저들의 이름만 모아서 중복이 없는 '세트(set)' 형태로 반환하세요.

# # 1. 데코레이터 정의
# def log_decorator(func):
#     def wrapper(*args):
#         print("--- LOG START ---")
#         # 함수 실행 결과를 변수에 담에서 리턴해준다. 그래야 로그 끝나는 시점에 결과를 리턴할 수 있다.
#         # 프린트문 만으로 연습을 해서 return 결과가 있는 함수들에서 헷갈린듯. return 이 무조건 있다는 가정으로 연습해야겠다. 
#         result = func(*args)
#         print("--- LOG END ---")
#         return result # 함수 결과를 배달해줘야한다. 
#     return wrapper

# 2. 메인 함수 정의 (위에서 만든 데코레이터를 적용하세요)
# @log_decorator
# def process_security_events(*args):
#     # args getting tuple iterable 
#     user_level_critical = set()
#     for item in args:
#         try:
#             # 레벨 키가 없거나 빈 문자열인지 검증 
#             level = item.get("level")
#             if not level:
#                 raise ValueError("데이터 빈 값")
#             # 레벨이 critical인 유저 추가 
#             if level == "critical":
#                 user_level_critical.add(item["user"])
#         except (KeyError, ValueError) as e:
#             print(f"오류 발생: {e}")
#     return user_level_critical

# ==============================================================================
# [테스트 실행 코드] - 코드 구조에 맞게 인자 전달 방식을 직접 고민해보세요!

# ==============================================================================
if __name__ == "__main__":
    event1 = {"user": "alice", "level": "critical"}
    event2 = {"user": "bob", "level": "info"}
    event3 = {"user": "alice", "level": "critical"} # 중복 데이터
    event4 = {"user": "charlie"} # level 키가 없는 에러 데이터
    event5 = {"user": "david", "level": ""} # level이 비어있는 에러 데이터
    
    r = process_security_events(event1, event2, event3, event4, event5)
    # r = process_security_events(event5)
    
    print(r)
    # 위 5개 이벤트를 처리하는 함수를 호출하고 결과를 출력해보세요.
    # 결과는 {'alice'} 가 나와야 하며, 에러 데이터들에 대한 예외 처리 메시지가 출력되어야 합니다.
