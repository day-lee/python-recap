"""
======================================================================
[묶음 2] 중급 연습 문제 (Level 2) - dictionary, set, tuple
======================================================================
"""

def question_13():
    """
    [13번 문제] 가맹점 데이터 병합 및 다중 그룹화 (dict + tuple)

    - 상황: 마케팅 부서에서 서로 다른 두 지점의 매출 데이터를 받았습니다.
    - 요구사항:
        1. 두 지점의 데이터를 합산하여 전체 가맹점의 '상품별 총 매출액 및 총 판매량'을 계산하세요.
        2. 최종 결과는 {상품명: (총매출액, 총판매량)} 형태로, value가 '튜플'이어야 합니다.
    - 조건: 앞서 배운 `dict.get(key, (0, 0))` 공식의 확장판을 고민해 보세요.
    - 출력 예시: {'A': (450000, 15), 'B': (200000, 4), 'C': (150000, 5)}
    """
    # 데이터 구조: (상품명, 매출액, 판매량)
    branch_1 = [("A", 150000, 5), ("B", 200000, 4)]
    branch_2 = [("A", 300000, 10), ("C", 150000, 5)]

    total_report = {}

    # TODO: 

    # 튜플은 불변성을 가지고 있어서 튜플 자체를 조작할 순 없다. 튜플 값 업데이트는 새로운 튜플을 만들어서 덮어쓰는 방식 
    # 불변성 제약을 우회하기 위한 방식임 
    # total_report["A"] = (15000, 3) 
    # total_report["A"][0] += 30000 -> TypeError, tuple object does not support item assignment, 기존 튜플을 직접 수정하려고함.

    # 리스트 + 리스트하면 새로운 리스트 생성 
    for product, sales, qty in branch_1 + branch_2:
        old_sales, old_qty =  total_report.get(product, (0 ,0))

        new_sales = old_sales + sales 
        new_qty = old_qty + qty 

        total_report[product] = (new_sales, new_qty)

    print(f"13번 결과: {total_report}")
    return total_report


if __name__ == "__main__":
    # 코드를 완성한 후 실행하여 결과를 확인해보세요!
    question_13()
