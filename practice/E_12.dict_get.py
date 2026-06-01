"""
[베이직 문제 2탄: 주소록 검색 및 예외 처리]

친구들의 연락처가 저장된 딕셔너리에서 특정 이름의 전화번호를 찾는 함수를 만드세요.
만약 존재하지 않는 이름을 검색하면 에러를 내지 않고 안내 메시지를 반환해야 합니다.

요구사항:
1. 이름을 딕셔너리에서 찾으면 그 전화번호를 반환하세요.
2. 없는 이름이라 KeyError가 발생하면 "존재하지 않는 연락처입니다."를 반환하세요.
dict.get(key, default_기본값) 메서드는 값을 안전하게 꺼낼 수 있다. dict[key]로 꺼낼 때 키가 존재하지 않으면 KeyError를 내고 프로그램이 멈춘다. 
"""

def find_phone_number(address_book: dict, name: str):
pass








# def find_phone_number(address_book: dict, name: str):
#     return address_book.get(name, "존재하지 않는 연착처입니다.")

# def find_phone_number(address_book: dict, name: str):
#     # 여기에 try-except 문을 완성해보세요!
#     try: 
#         result = address_book.get(name, "존재하지않는 연락처입니다.") 
#         return result
#     except KeyError as e:
#         print("존재하지않는 연락처입니다.")

# def find_phone_number(address_book:dict, name:str):
#     try: 
#         if name not in address_book:
#             raise KeyError("존재하지 않는 연락처입니다.")
#         return address_book[name]
#     except KeyError as e:
#         return e

# 다른점: 일단 try 문에서 시도를 해본뒤 만약 제너릭 KeyError(키 존재하지 않음)가 나면
# 메세지를 반환한다.
# def find_phone_number(address_book:dict, name:str):
#     try: 
#         return address_book[name]
#     except KeyError:
#         return "존재하지 않는 연락처입니다."    

# 다른점: dict.get(k, "error message")를 쓰면 try except문이 필요없다.
# def find_phone_number(address_book:dict, name:str):
#     return address_book.get(name, "존재하지 않는 연락처입니다.")
# ==============================================================================
# [테스트 실행 코드]
# ==============================================================================
if __name__ == "__main__":
    my_book = {
        "Kim": "010-1234-5678",
        "Park": "010-1111-2222"
    }

    # 1. 있는 이름을 검색할 때
    print(find_phone_number(my_book, "Kim"))  
    # 예상 출력: 010-1234-5678

    # 2. 없는 이름을 검색할 때
    print(find_phone_number(my_book, "Lee"))  
    # 예상 출력: 존재하지 않는 연락처입니다.
