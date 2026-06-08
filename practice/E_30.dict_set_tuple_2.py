"""
======================================================================
[묶음 2] 기본~중급 연습 문제 (Level 1.5) - dictionary, set, tuple
======================================================================
"""

def question_11():
    """
    [11번 문제] 튜플 데이터 필터링과 새로운 데이터 생성 (tuple + list)

    - 상황: 회사 직원들의 [이름, 부서, 근속연수] 정보가 변경 불가능한 튜플의 리스트로 저장되어 있습니다.
    직원들 중 '근속연수가 3년 이상인' 베테랑 직원의 '이름'만 골라내어 변경 불가능한 '튜플(tuple)' 형태로 반환하세요.

    - 출력 예시: ('Alice', 'Charlie')
    """
    # 각 튜플은 (이름, 부서, 근속연수) 입니다.
    employees = [
        ("Alice", "HR", 5),
        ("Bob", "DEV", 2),
        ("Charlie", "MKT", 4),
        ("David", "DEV", 1),
    ]

    print(tuple([name for name, _, year in employees if year >= 3]))

    # result = []
    # for name, _, years in employees:
    #     if years >= 3:
    #         # 리스트로 먼저 만든 뒤 튜플 변환이 성능적으로 나음 
    #         result.append(name) # trailing comma is required! 
    # result = tuple(result)
    # return result

    # - 조건: 튜플 인덱싱(직원[0], 직원[2] 등)과 list comprehension을 엮은 뒤 최종 변환하세요.

    # 튜플 메서드 tuple()로 리스트 컴프리헨션을 넘겨준다. 괄호를 바로 씌워서 만들수가 없음. 그건 제너레이터 문법임. 
    # result = tuple([name for name, department, years in employees if years >= 3])
    # print(f"11번 결과: {result}")
    # return result


if __name__ == "__main__":
    # 코드를 완성한 후 실행하여 결과를 확인해보세요!
    print(question_11())
