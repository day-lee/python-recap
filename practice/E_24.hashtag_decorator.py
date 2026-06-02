"""
[Senior's Challenge: 문자열 가공 데코레이터 직접 설계하기]

* 토픽: decorator, args_kwargs, str, function
* 목표: 데코레이터의 기본 구조(*args, **kwargs)를 이해하고, 
        함수의 리턴값(문자열)을 가로채서 변형하는 미들웨어를 구축합니다.
"""

# =====================================================================
# 문제. 해시태그 생성 데코레이터 구현하기
# =====================================================================

def make_hashtag(func):
   """
    이 데코레이터는 대상 함수가 리턴한 일반 문자열을 가로채서
    앞에 '#'을 붙이고, 모든 공백을 제거하여 '해시태그 포맷'으로 변경합니다.
    
    [인스트럭션 / 요구사항]
    1. 데코레이터 내부에 가변 인자(*args, **kwargs)를 안전하게 전달받는 
       내부 함수(wrapper)를 만드세요.
    2. 내부 함수 안에서 원본 함수 `func`를 인자들과 함께 실행하여 
       원래의 문자열 리턴값을 받아오세요.
    3. 받아온 문자열에서 모든 공백을 제거(replace 활용)하고, 맨 앞에 '#'을 붙이세요.
       예: "Python is fun" -> "#Pythonisfun"
    4. 변형된 최종 문자열을 리턴하세요.
   """

   pass





   # def wrapper(*args, **kwargs):
   #    try:
   #        result = func(*args, **kwargs)
   #        return result
   #    except Exception as e:
   #        print(f"error: {e}")
   #        return ""
   # return wrapper

   # def wrapper(*args, **kwargs):
   #    try:
   #        result = func(*args, **kwargs)
   #        return result
   #    except Exception as e:
   #        print(f"error: {e}")
   #        return ""     
   # return wrapper

   # def wrapper(*args, **kwargs):
   #    try:
   #        result = func(*args, **kwargs)
   #        return result
   #    except Exception as e:
   #        print(f"error: {e}")
   #        return ""
   # return wrapper

   # def wrapper(*args, **kwargs):
   #    try: 
   #       result = func(*args, **kwargs)
   #       return "#" + result.replace(" ", "")
   #    except (KeyError, TypeError) as e:
   #       print(e)
   #       return ""
   # return wrapper

# 1. 첫번째 시도
# def make_hashtag(func):
#    def wrapper(*args, **kwargs):
#       if "level" in kwargs and not isinstance(kwargs["level"], int):
#          return "Not a right type"
#       new_str = func(*args, **kwargs)
#       return f"#{new_str.replace(" ", "")}"
#    return wrapper

# =====================================================================
# 테스트용 함수 (여기는 수정하지 마세요)
# =====================================================================
@make_hashtag
def generate_title(topic, category="Coding", level=1):
    """
    입력받은 토픽과 카테고리를 조합하여 하나의 제목 문자열을 만듭니다.
    """
    return f"{topic} in {category} {level}"


# =====================================================================
# 검증용 테스트 코드 (IDE에서 실행하여 결과를 확인하세요)
# =====================================================================
if __name__ == "__main__":
    print("=== 데코레이터 테스트 ===")
    
    # 케이스 1: 기본 인자만 사용
    result_1 = generate_title("Python Study")
    print(result_1)  
    # 예상 결과: #PythonStudyinCoding1
    
    # 케이스 2: 키워드 인자(kwargs) 변경
    result_2 = generate_title("Data Science", category="Analysis")
    print(result_2)  
    # 예상 결과: #DataScienceinAnalysis1

   # 케이스 3: 키워드 인자(kwargs) 변경
    result_3 = generate_title("Data Structure", category="CS", level=2)
    print(result_3)  
    # 예상 결과: #DataStructureinCS2

   # 케이스 4: 키워드 인자(kwargs) 변경, TypeError
    result_4 = generate_title("Data Structure", category="CS", level='easy')
    print(result_4)  
    # 예상 결과: DataStructureinCS