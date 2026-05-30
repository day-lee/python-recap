"""
[실무형 프로필 정제 문제: 키워드 인자 텍스트 다듬기]

회원가입 시 입력된 유저 프로필 데이터들이 딕셔너리 형태로 들어옵니다.
이때 이메일이나 이름 앞뒤에 실수로 들어간 공백을 제거하고, 
전부 소문자로 통일하여 정제된 딕셔너리를 반환하는 함수를 작성하세요.

요구사항:
1. `**kwargs`를 사용하여 키워드 인자 형태로 유저 데이터를 받으세요.
2. 딕셔너리 컴프리헨션을 사용하여 전달받은 데이터를 정제하세요.
3. 정제 규칙:
   - 모든 데이터(Value)의 앞뒤 공백을 제거해야 합니다. (힌트: .strip())
   - 모든 데이터(Value)를 소문자로 변경해야 합니다. (힌트: .lower())
"""
# def clean_user_profile(**kwargs):
#     # kwargs.items()와 딕셔너리 컴프리헨션을 활용해 정제된 결과를 반환하세요.
#     pass

def clean_user_profile(**kwargs):
    # kwargs.items()와 딕셔너리 컴프리헨션을 활용해 정제된 결과를 반환하세요.
    # kwargs는 개별 인자들이 딕셔너리 형태로 들어옴. 
    # strip 공백 제거, 로워() 컴프리헨션으로 돌아가며 정제 
    # return { key: value.strip().lower() for key, value in kwargs.items()}
    # 아규먼트가 str일 때는 괜찮음 -> 숫자가 들어오는 순간 AttributeError: 'int' object has no attribute 'strip' 
    # strip은 str에만 적용됨. str 타입인지 확인해서 적용하고 아니면 else로 씀. isinstance

    # 방어적 코드로 짜려면 입력값이 str이 아닌 경우도 고려해야함. 
    # return { key: (value.strip().lower()) if isinstance(value, str) else value for key, value in kwargs.items()}

# ==============================================================================
# [테스트 실행 코드]
# ==============================================================================
if __name__ == "__main__":
    # 유저가 실수로 공백을 넣거나 대문자로 입력한 상황
    result = clean_user_profile(
        name="  JohnDoe  ",
        email=" USER01@EMAIL.COM   ",
        city="  SEOUL ",
        age = 12
    )
    
    print(result)
    
    # 예상 출력 결과 (앞뒤 공백이 사라지고 모두 소문자로 변경되어야 합니다):
    # {'name': 'johndoe', 'email': 'user01@email.com', 'city': 'seoul'}
