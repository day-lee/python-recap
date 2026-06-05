"""
[Senior's Code Review: 주니어 파이썬 개발자를 위한 실전 문법 다지기 - 2탄]

* 주제: 가변 인자(args, kwargs) 다루기 & 컬렉션 변환
* 지침: 아래 함수의 독스트링을 읽고 요구사항에 맞는 코드를 작성하세요.
"""

# =====================================================================
# 문제. VIP 회원 명부 작성하기
# 활용 토픽: args_kwargs_optional_arguments, tuple, list, str
# =====================================================================
def build_vip_list(prefix:str, *args, **kwargs):
    """
    여러 명의 회원 이름(*args)과 그들의 상세 정보(**kwargs)를 받아
    정제된 VIP 회원 정보 리스트를 만듭니다.

    회원 정보 중, key가 'status'이고 value가 'VIP'인 
    데이터가 있다면, 리스트의 가장 맨 앞에 매개변수 `prefix` 값을 추가하세요.

    Args:
        prefix (str): VIP 접두어 (예: "[우수회원]")
        *args: 가변 개수의 회원 이름 (문자열들)
        **kwargs: 키워드 가변 인자 (예: status="VIP", grade=1)

    Returns:
        list: 정제된 회원 명부 리스트

    예상 결과: ['[VVIP]', 'Alice', 'Bob'] or # 예상 결과: ['Charlie', 'David']
    """
    pass





    # # prefix를 리스트에 넣어 새 리스트를 만들고 + 오퍼레이터를 사용해 두 리스트를 extend해서 합쳐준다. 
    # user_list = list(args)
    # if kwargs.get("status") == "VIP":
    #     return [prefix] + user_list
    # return user_list

    # user_list = list(args)
    # status = []
    # if kwargs.get("status") == "VIP":
    #     status.append(prefix)
    #     return status + user_list
    # return user_list

    # # modify the original list 
    # user_list= list(args)
    # if kwargs.get("status") == "VIP":
    #     user_list.insert(0, prefix)
    # return user_list

    # 요구사항:
    # 1. args로 들어온 가변 인자(이름들)는 튜플 형태입니다. 
    #    이 이름들을 하나의 '리스트'로 변환하세요.
    # 2. kwargs로 들어온 회원 정보 중, key가 'status'이고 value가 'VIP'인 
    #    데이터가 있다면, 리스트의 가장 맨 앞에 매개변수 `prefix` 값을 추가하세요.
    # 3. 최종 완성된 리스트를 리턴하세요.

    # names = list(args)
    # result = []
    # if kwargs.get("status") == "VIP":
    #     result.insert(0, prefix)
    # return result + names

#     names = list(args)
#     if kwargs.get("status") == "VIP":
#         names = [prefix] + names
        
#     return names
# =====================================================================
# 검증용 테스트 코드 (아래 코드를 실행하여 정상 작동하는지 확인하세요)
# =====================================================================
if __name__ == "__main__":
    print("--- Test: build_vip_list ---")
    
    # 케이스 1: VIP 회원인 경우 (status가 VIP)
    result_vip = build_vip_list("[VVIP]", "Alice", "Bob", status="VIP", region="Seoul")
    print(result_vip)
    # 예상 결과: ['[VVIP]', 'Alice', 'Bob']

    # 케이스 2: 일반 회원인 경우 (status가 VIP가 아니거나 없음)
    result_normal = build_vip_list("[VVIP]", "Charlie", "David", status="General")
    print(result_normal)
    # 예상 결과: ['Charlie', 'David']
