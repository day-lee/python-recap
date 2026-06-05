"""
======================================================================
[묶음 3] 기본~중급 연습 문제 (Level 1.5) - zip, args, kwargs, function
======================================================================
"""


def question_17(currency_symbol: str, **kwargs) -> dict[str, str]:
    """
    [17번 문제] 글로벌 가격 포맷터 
    - 상황: 해외 지점별 제품 가격 데이터(kwargs)를 받아, 앞에 화폐 단위(currency_symbol)를 붙여서 보고서용 딕셔너리로 가공해야 합니다.
    - 요구사항:
        1. `**kwargs`로 들어온 상품명(Key)과 가격(Value)을 순회하세요.
        2. 가격을 문자열로 바꾼 뒤 앞에 `currency_symbol`을 붙여서 {상품명: '화폐가격'} 형태를 만드세요.
    - 원본 데이터 호출 예시: question_17("$", laptop=1200, monitor=300)
    - 출력 예시: {'laptop': '$1200', 'monitor': '$300'}
    """
    # f string이 + 연산자로 문자열 더하는 것보다 성능이 좋고, 가독성도 좋다. 
    pass




    print(f"17번 결과: {result_dict}")
    return result_dict

    # result_dict = {product: f"{currency_symbol}{price:,}" for product, price in kwargs.items()}


if __name__ == "__main__":
    # 코드를 완성한 후 아래 테스트 셋으로 실행하여 결과를 확인해보세요!

    print("\n--- 17번 실행 ---")
    question_17("$", laptop=1200, monitor=300)


