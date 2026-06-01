"""
[Senior's Code Review: 실무형 데이터 파이프라인 정제 - Easy-Medium]

* 토픽: list, dictionary, set, exception, function, list/dict comprehension
* 상황: 외부 API로부터 받은 정제되지 않은 '주문 데이터'를 분석 가능한 형태로 가공해야 합니다.
"""

def process_orders(orders: list, target_categories: set) -> dict:
    """
    전체 주문 리스트에서 특정 카테고리에 속한 주문만 필터링하고, 
    데이터 오류를 안전하게 처리하여 카테고리별 '총 매출'과 '고객 명단'을 집계합니다.

    [요구사항]
    1. 예외 처리 (Exception): 
       주문 데이터 중 일부는 누락되거나 잘못된 타입으로 들어옵니다.
       - 데이터에 'price'나 'quantity' 키가 없거나(KeyError), 
       - 가격/수량이 숫자가 아니어서 계산 시 에러(TypeError, ValueError)가 발생하면,
       해당 주문 한 건만 조용히 건너뛰고(skip) 다음 주문을 계속 처리하세요.
       
    2. 필터링 및 집계:
       - 'category'가 매개변수 `target_categories` 집합에 포함된 주문만 처리합니다.
       - 매출 계산 공식: price * quantity
       
    3. 결과 포맷 (Dictionary & Set):
       - 리턴할 딕셔너리의 키는 `target_categories`에 존재하는 카테고리 이름이어야 합니다.
       - 각 카테고리 내 value는 또 다른 딕셔너리로, 아래 두 가지 정보를 가집니다:
         * 'total_revenue': 해당 카테고리의 총 매출액 (int 또는 float)
         * 'buyers': 해당 카테고리 상품을 구매한 고유한 고객 이름들의 '집합(set)'

    Args:
        orders (list): 딕셔너리 구조의 주문 데이터 리스트
        target_categories (set): 필터링할 대상 카테고리 이름 집합

    Returns:
        dict: 카테고리별 집계 결과
    """
    pass

    # 1. 논리가 중간에 꼬임. dict 방 있는지 없는지 알아보는 구조 
    # # if 문으로 조건을 쳐내는 것보다 예외가 만을 때는 try except continue 해주는게 범용적임 
    # cleansed_orders = {}
    # result = {}
    # for data in orders:
    #     price = data.get("price")
    #     quantity = data.get("quantity")
    #     category = data.get("category")
    #     buyer = data.get("buyer")

    #     if price and quantity and isinstance(price, (int, float)) and isinstance(quantity, (int, float)):
          
    #         if category in target_categories:
    #             revenue = price * quantity
    #             # result가 빈 딕셔너리이니까 초기화를 먼저 해주고 나서, 이미 존재할 때는 키값으로 접근해서 합해주거나 누적해줌 
    #             if category not in result:
    #                 result[category] = {
    #                     "total_revenue": 0,
    #                     "buyer": set()
    #                 }
    #             result[category]["total_revenue"] += revenue
    #             result[category]["buyer"].add(buyer)
    # return result
    # if 문으로 조건을 쳐내는 것보다 예외가 만을 때는 try except continue 해주는게 범용적임 


    #  try-except continue, dict 초기화, dict.add(요소), set()초기화 
    #  먼저 키-값에 접근한 뒤 dict 가 없으면 데이터 모양 잡아서 초기화 해주고, 이미 존재하면 값 더해주거나 누적해줘서 모양 잡음 
    # setdefault() 메소드는 방이 없으면 딕셔너리를 사용해 새로 만들고 있으면 기존 방 통채로 가져옴 
    # 나는 데이터를 모아뒀다가 나중에 분류하는 map-reduce 스타일 
    # setdefault()는 데이터 확인 즉시 바로 카테고리에 분류해서 넣는 스타일 - 임시 리스트 만들 필요없고 논리가 단순함. 

    # 2. ai 도움으로 try-except
    # cleansed_orders = {}
    # result = {}
    # for data in orders:
    #     try: 
    #         price = data.get("price")
    #         quantity = data.get("quantity")
    #         category = data.get("category")
    #         buyer = data.get("buyer")
    #         # 만약 price, quantity가 타입 에러나 빈값이면 ValueError 
    #         revenue = price * quantity

    #         if category in target_categories:
    #             # result가 빈 딕셔너리이니까 초기화를 먼저 해주고 나서, 이미 존재할 때는 키값으로 접근해서 합해주거나 누적해줌 
    #             if category not in result:
    #                 result[category] = {
    #                     "total_revenue": 0,
    #                     "buyer": set()
    #                 }
    #             result[category]["total_revenue"] += revenue
    #             result[category]["buyer"].add(buyer)
    #     except (KeyError, TypeError, ValueError):
    #             continue # 에러 발생하면 조용히 건너뜀 
    # return result

    # 3. 주석 적으며 다시 시도 
    #     # 포 룹으로 orders 데이터 하나씩 체크하기 
    # # 예외처리시 .get()으로 값이 있으면 가져오기 keyerror 방지하는 장치 
    # # try except continue로 건너뛰기
    # result = {}
    # for order in orders: 
    #     try:
    #         buyer = order.get("buyer")
    #         category = order.get("category")
    #         price = order.get("price") 
    #         quantity = order.get("quantity")
    # # if statement, in operator 사용해서 target_categories 집합 포함만 처리하기 
    #         # type check를 변수로 만들어버림 
    #         # valid_number = isinstance(price, (int, float)) and isinstance(quantity, (int, float))
    #         # if category in target_categories and valid_number
            
    #         if category in target_categories and isinstance(price, (int, float)):
    # # if 카테고리 키가 result 딕셔너리에 있는지 확인해서 없으면 새 딕셔너리의 디폴트 세팅 사용, 있으면 누적 
    #             if category not in result:
    #                 # result.update({category: {"total_revenue":0, "buyers": set()}})
    #                 result[category] = {"total_revenue":0, "buyers": set()}
    #             result[category]["total_revenue"] += price * quantity
    #             result[category]["buyers"].add(buyer)
    #     except (KeyError, ValueError, TypeError):
    #         continue 
    # return result
# =====================================================================
# 검증용 테스트 코드 (실제 복잡한 실무형 데이터 세트)
# =====================================================================
if __name__ == "__main__":
    # 외부에서 들어온 로우(Raw) 데이터
    raw_orders = [
        {"order_id": 1, "buyer": "Alice", "category": "Electronics", "price": 1000, "quantity": 2},
        {"order_id": 2, "buyer": "Bob", "category": "Books", "price": 20, "quantity": 5},
        {"order_id": 3, "buyer": "Charlie", "category": "Electronics", "price": 500, "quantity": 1},
        # 에러 데이터 1: price 키 누락 (KeyError 대응 필요)
        {"order_id": 4, "buyer": "David", "category": "Electronics", "quantity": 3}, 
        {"order_id": 5, "buyer": "Alice", "category": "Electronics", "price": 1000, "quantity": 1}, # 중복 구매자
        # 에러 데이터 2: 가격이 문자열 (TypeError/ValueError 대응 필요)
        {"order_id": 6, "buyer": "Eve", "category": "Books", "price": "free", "quantity": 1}, 
        {"order_id": 7, "buyer": "Frank", "category": "Clothing", "price": 50, "quantity": 2} # 대상 외 카테고리
    ]

    # 우리가 관심 있는 카테고리
    categories = {"Electronics", "Books"}

    result = process_orders(raw_orders, categories)
    print("=== 최종 정제 결과 ===")
    import pprint
    pprint.pprint(result)
    
    """
    [예상 출력 결과]
    {
        'Books': {
            'buyers': {'Bob'}, 
            'total_revenue': 100
        },
        'Electronics': {
            'buyers': {'Alice', 'Charlie'}, 
            'total_revenue': 3500
        }
    }
    """
