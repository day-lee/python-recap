"""
[도전 문제: 사내 보안 이벤트 알림 시스템]

상황:
여러 팀에서 동시에 발생한 '보안 경고 이벤트(로그 데이터)'들을 수집하고 가공하는 시스템입니다.
당신은 이벤트 데이터를 안전하게 처리하고 앞뒤로 실행 로그를 남겨야 합니다.

미션:
1. 함수 실행 앞뒤로 "--- LOG START ---", "--- LOG END ---"를 출력하는 데코레이터 `log_decorator`를 만드세요.
2. 메인 함수 `process_security_events`를 설계하세요. 
   - 이 함수는 여러 개의 이벤트 데이터(딕셔너리 형태)를 한 번에(가변 인자로) 받습니다.
   - 각 이벤트 데이터는 `{'user': 'name', 'level': 'critical'}` 같은 형태입니다.
   - 단, 이벤트 데이터에 `level` 키가 아예 없거나, value가 비어있는 이상한 데이터가 들어오면 에러(KeyError, ValueError 등)를 안전하게 예외 처리(try-except)하고 넘어가야 합니다.
3. 결과물 반환:
   - 예외를 통과한 정상 데이터 중, level이 "critical"(심각)인 유저들의 이름만 모아서 중복이 없는 '세트(set)' 형태로 반환하세요.
"""

# # 1. 데코레이터 정의
# def log_decorator(func):
#     pass


# # 2. 메인 함수 정의 (위에서 만든 데코레이터를 적용하세요)
# def process_security_events(*args):
#     pass


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


# # 2. 메인 함수 정의 (위에서 만든 데코레이터를 적용하세요)
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
    print(r)
    # 위 5개 이벤트를 처리하는 함수를 호출하고 결과를 출력해보세요.
    # 결과는 {'alice'} 가 나와야 하며, 에러 데이터들에 대한 예외 처리 메시지가 출력되어야 합니다.
