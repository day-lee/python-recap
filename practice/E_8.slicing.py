"""
==============================================================================
[라이브 코딩 인터뷰 문제] 로그 데이터에서 에러 코드 및 날짜 추출기

[상황] 
서버 오류 로그가 다음과 같이 하나의 긴 문자열(String) 형태로 들어왔습니다. 
각 데이터는 슬래시(/)를 기준으로 [날짜/로그레벨/에러코드/발생위치] 순서로 묶여 있습니다.
 "2026-05-28/ERROR/ERR_404_NOT_FOUND/auth_service"

[문제] 
이 log_data 문자열을 쪼개고 분석해서 '연도(Year)'와 '에러코드(Error Code)'만 쏙 
골라내어 리스트(List) 형태로 반환하는 함수 extract_error_info를 작성하세요.

[제한 조건 및 필수 요구사항]
1. 문자열을 슬래시(/) 기준으로 쪼개기 위해 .split("/") 메서드를 사용해야 합니다.
2. 날짜 문자열("2026-05-28")에서 앞의 4글자인 연도만 잘라내기 위해 
   파이썬의 '슬라이싱(Slicing) [:4]' 문법을 활용해 주세요.
3. 최종 반환값은 ['2026', 'ERR_404_NOT_FOUND'] 모양의 리스트여야 합니다.

슬라이싱은 sequence 타입에서만 사용가능. index가 있을 때
str, list, tuple 
set, dict, zip은 안됨. 쓰고 싶다면 list()로 변환한 뒤에 사용 가능 
==============================================================================
1. separator로 스트링을 잘라서 리스트로 만들어준다. 
2. 0, 2번 인덱스에 날짜와 에러코드가 있다
3. 날짜는 또 쪼개서 연도만 뽑는다. 
4. 새로운 리스트에 넣어준다.  

"""
def extract_error_info(log_string):
    pass









# def extract_error_info(log_string):
#     # print(log_string) # 2026-05-28/ERROR/ERR_404_NOT_FOUND/auth_service 
#     date, _, error_code, _ = log_string.split("/")
#     # print(date, error_code)
#     return [date[:4], error_code]

# def extract_error_info(log_string):
#     log_list = log_string.split("/")
#     date, _, error_log, _ = log_list
#     return [ date[:4], error_log]


# def extract_error_info(log_string):
    """
    [1단계] 슬래시(/)를 기준으로 전체 문자열을 쪼개서 리스트로 만듭니다.
    힌트: log_string.split("/")을 사용해서 변수에 담아보세요.
    """
    # parts = log_string.split("/")
    # date, _, error_code, _ = parts 
    # print(date, error_code)
    # new_list = [date[:4], error_code]
    # return new_list

    """
    [2단계] 쪼개진 리스트(parts)에서 필요한 알맹이들을 가져옵니다.
    힌트: parts[0]은 날짜("2026-05-28")이고, 에러코드는 몇 번째 인덱스에 있나요?
    아까 배운 '리스트 언패킹'을 응용해서 한 번에 여러 변수에 쪼개 담아도 아주 좋습니다! 
    
    [3단계] 날짜 문자열에서 앞의 4글자(연도)만 슬라이싱[:4]으로 추출합니다.
    """



# ------------------------------------------------------------------------------
# 면접관의 채점 및 실행 코드 (수정하지 마세요)
# ------------------------------------------------------------------------------
log_data = "2026-05-28/ERROR/ERR_404_NOT_FOUND/auth_service"

result = extract_error_info(log_data)
print(f"추출된 정보: {result}")

# [정상 출력 예시]
# 추출된 정보: ['2026', 'ERR_404_NOT_FOUND']
