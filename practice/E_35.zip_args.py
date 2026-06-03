"""
======================================================================
[묶음 3] 기본~중급 연습 문제 (Level 1.5) - zip, args, kwargs, function
======================================================================
"""


def question_16(*args, weights=None) -> list[float]:
    """
    [16번 문제] 엑셀 가중치 계산기 

    - 상황: 마케팅 부서에서 여러 채널의 원본 점수(args)들을 받아, 
           가중치(weights)를 곱한 최종 점수 리스트를 만들려고 합니다.
    - 요구사항:
        1. 위치 가변 인자 `*args`로 들어온 점수들과 키워드 인자 `weights` 리스트를 
           `zip`으로 1:1 매칭하여 순회하세요.
        2. 각 점수에 가중치를 곱한 결과(`score * weight`)를 소수점 첫째 자리까지 구하여 리스트에 담아 반환하세요.
    - 조건: `zip` 함수와 list comprehension 공식을 한 줄로 엮어서 완성해 보세요.
     원본 데이터 호출 예시: question_16(100, 90, 50, weights=[0.8, 0.2, 0.9])
    - 출력 예시: [80.0, 18.0, 45.0]
    """

    pass

    # # 방어적 코드로 만약 weights가 없을 경우 얼리 리턴 
    # if weights is None:
    #     return []
    # zipped = zip(args, weights, strict=True)
    # # round() 함수로 소수점 첫째자리 까지 표시, 오차가 있을 수 있음. 정확하려면 decimal 모듈 사용 필요  
    # result = [round(score * weight, 2) for score, weight in zipped]
    # print(f"16번 결과: {result}")
    # return result


if __name__ == "__main__":
    # 코드를 완성한 후 아래 테스트 셋으로 실행하여 결과를 확인해보세요!
    print("--- 16번 실행 ---")
    question_16(100, 90, 50, weights=[0.8, 0.2, 0.9])

