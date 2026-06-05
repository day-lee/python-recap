"""
[주소록 이름-전화번호 매핑]

두 개의 리스트(이름, 전화번호)를 합쳐서 하나의 딕셔너리로 만드세요.
단, 전화번호에 하이픈(-)이 들어간 정상적인 데이터만 골라내야 합니다.

# 예상 출력 결과 (하이픈이 없는 Lee는 제외되어야 합니다):
# {'Kim': '010-1234-5678', 'Park': '010-1111-2222'}

<zip 객체>는 iterator로 연산 결과를 메모리에 바로 올리지 않고,
준비만 해둔 상태로 요청시 결과 반환해준다. 
"""
def clean_address_book(names, phones):
    pass













#     zipped_list = list(zip(names, phones)) iterable이면 for loop 쓸 수 있으니 list(zip())으로 굳이 안바꿔도 됨. 
#     return {name: phone for name, phone in zipped_list if "-" in phone}

# 요구사항:
# 1. zip 함수를 사용해 이름과 전화번호 쌍을 묶으세요.
# 2. 딕셔너리 컴프리헨션을 사용해 결과를 만드세요.
# 3. 조건문(if)을 넣어 전화번호에 "-"이 포함된 경우만 딕셔너리에 추가하세요.


# def clean_address_book(names, phones):
#     zipped = zip(names, phones)
#     return {name: phone for name, phone in zipped if '-' in phone}

# def clean_address_book(names, phones):
#     zipped = zip(names, phones) # <zip object at 0x10505ba80> 결과를 메모리에 만들어 두지 않고 요청할 때 꺼내줄 준비만 해둔 상태. iterator 상태 
#     # print(list(zipped))

#     # result = {item[0]: item[1] for item in zipped if "-" in item[1] }
#     # 튜플 형태이므로 튜플 언패킹 가능 zip, tuple unpacking 
#     result = {name: phone for name, phone in zipped if "-" in phone}
#     return result
==============================================================================
# [테스트 실행 코드]
# ==============================================================================
if __name__ == "__main__":
    user_names = ["Kim", "Lee", "Park"]
    user_phones = ["010-1234-5678", "01098765432", "010-1111-2222"]

    result = clean_address_book(user_names, user_phones)
    print(result)
    
    # 예상 출력 결과 (하이픈이 없는 Lee는 제외되어야 합니다):
    # {'Kim': '010-1234-5678', 'Park': '010-1111-2222'}
