"""
[문제]이 user_data를 분석하여 등급(grade)이 "vip"인 유저들만 쏙 골라내고, 그 유저들의 이메일 주소를 모두 '대문자(Uppercase)'로 변환한 새로운 딕셔너리를 반환하는 함수 filter_vip_emails를 작성하세요.

[제한 조건 (필수 요구사항)]일반적인 for문과 if문을 길게 쓰지 말고, 

파이썬의 핵심 문법인 딕셔너리 컴프리헨션(Dictionary Comprehension)을 사용하여 단 한 줄(혹은 하나의 표현식)로 결과 딕셔너리를 만들어내야 합니다.

문자열을 대문자로 바꿀 때는 파이썬 문자열 내장 메서드인 .upper()를 사용하세요

# 'kim'과 'park'만 남고, 이메일은 대문자로 변환되어야 합니다.
{
    'kim': 'KIM@GMAIL.COM', 
    'park': 'PARK@DAUM.NET'
}

note
if grate is vip 
convert email upper
make a new dict 
"""

# def filter_vip_emails(users):
#     # 이 공간에 코드를 작성하세요.
#     # 힌트 1: 딕셔너리의 key와 value를 동시에 꺼내려면 users.items()를 활용해야 합니다.
#     # 힌트 2: { key: value for ... in ... if 조건 } 구조를 떠올려보세요!
#     r = {name: data["email"].upper() for name, data in users.items() if data["grade"] == "vip"}
#     print(r)

def filter_vip_emails(users):
    pass
# --- 면접관의 채점 및 실행 코드 ---
user_data = {
    "kim": {"email": "kim@gmail.com", "grade": "vip"},
    "lee": {"email": "lee@naver.com", "grade": "gold"},
    "park": {"email": "park@daum.net", "grade": "vip"},
    "choi": {"email": "choi@outlook.com", "grade": "silver"}
}

result = filter_vip_emails(user_data)
print(result)
