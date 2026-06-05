"""
======================================================================
[묶음 3] 기본~중급 연습 문제 (Level 1.5) - zip, args, kwargs, function
======================================================================
"""


def question_18(base_url: str, *args, **kwargs) -> list[str]:
    """
    [18번 문제] API 요청 URL 빌더 (복합 인자 처리)

    - 상황: 백엔드 서버에서 외부 API를 찌르기 위한 여러 개의 URL 주소를 다이내믹하게 생성해야 합니다.
    - 요구사항:
        1. `*args`에는 엔드포인트 경로들이 들어옵니다. (예: "users", "products")
        2. `**kwargs`에는 공통으로 붙을 쿼리 스트링 매개변수들이 들어옵니다. (예: api_key="secret", lang="ko")
        3. 쿼리 스트링 파트(`?api_key=secret&lang=ko`)를 먼저 딕셔너리를 활용해 예쁘게 조립하세요.
        4. 각 엔드포인트 뒤에 쿼리 스트링을 붙여서 ['base_url/엔드포인트?쿼리스트링', ...] 형태의 리스트를 만드세요.
    - 조건: `args` 순회와 `kwargs.items()`를 활용한 문자열 결합 논리를 구현하세요.

    - 원본 데이터 호출 예시: 
        question_18("https://test.com", "users", "products", api_key="abc", lang="ko")
    - 출력 예시: 
        ['https://test.com', 'https://test.com']
    """
    # 가장 마지막의 쿼리 스트링부터 만들고나서(쿼리 스트링이 없는 경우도 고려하면서), 각 엔드포인트별로 url을 돌면서 조립해준다. 불필요한 반복 계산 줄이기가 목표. 











    # url = ""
    # url_list = []
    # for endpoint in args:
    #     url = f"{base_url}/{endpoint}?"
    #     for key, value in kwargs.items():
    #         url += f"{key}={value}&"
    #     url_list.append(url[0:-1])
    # print(url_list)

if __name__ == "__main__":
    # 코드를 완성한 후 아래 테스트 셋으로 실행하여 결과를 확인해보세요!

    print("\n--- 18번 실행 ---")
    question_18("https://test.com", "users", "products", api_key="abc", lang="ko")


    # # 1. 쿼리 스트링 문자열 만들기 (예: "api_key=abc&lang=ko")
    # # 힌트: [f"{k}={v}" for k, v in kwargs.items()] 로 리스트를 만든 뒤, "&".join(...)을 쓰면 편합니다.
    # query_parts = [f"{k}={v}" for k, v in kwargs.items()]
    # query_string = "&".join(query_parts)

    # 2. base_url, endpoint(args), query_string을 조합하여 최종 URL 리스트 완성하기
    # # TODO: 아래에 코드를 완성하세요. (list comprehension 추천)