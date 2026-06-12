def process_orders(order_data: str) -> dict:
    """
    You are working for a UK-based e-commerce platform. 
    Your task is to process a raw string containing a list of customer orders 
    and calculate the total quantity ordered for each unique item.

    Input format:
    - 'order_data' is a single string where individual item orders are separated by commas.
    - Each item order contains the item name and the quantity, separated by a colon (e.g., "apple:3").

    Requirements:
    1. Parse the string to extract each item and its corresponding quantity.
    2. Aggregate the quantities for each unique item and return the result as a dictionary.
    3. If the input string is empty, return an empty dictionary.
    4. Handle unexpected formatting errors gracefully:
       - If a specific order cannot be parsed correctly (e.g., missing a colon or invalid quantity type), 
         skip that specific order entirely and continue processing the rest.

    Example:
    >>> process_orders("apple:3,banana:2,apple:5,orange:one,grape")
    {'apple': 8, 'banana': 2}
    
    Constraints:
    - Do not use any external libraries.
    """
    # ETL 순서를 생각하면서 문제를 쪼개가면서 풀어보자. 슈도 단계 먼저 적기 
    pass





    # turn into list split() ["apple:3", ""...]
    # in, : , skip , qty not int, skip 
    # iterate, access each el, split(:), name, qty 
    # crate a dict and add amount 

    # order_data_list = order_data.split(",")
    # result = {}
    # for data in order_data_list:
    #     try: 
    #         if ":" not in data:
    #             continue
    #         name, qty = data.split(":")
    #         int_qty = int(qty)
    #         result[name] = result.get(name, 0) + int_qty
    #     except ValueError :
    #         continue
    # return result
    # print(result)

    # # str to list split(,)
    # order_data_list = order_data.split(",")
    # # print(order_data_list)
    # # iterate each of them [[apple:3], ]
    # result = {}
    # for data in order_data_list:
    #     if ":" not in data:
    #         continue 
    #     try: 
    #        name, qty = data.split(":")
    #        result[name] = result.get(name,0) + int(qty)

    #     except ValueError:
    #         continue 

    # print(result)
    """ 모범 답안 
    # ETL: Extract, Transform, Load

    # 스트링 정규화: 앞 뒤 공백제거, 대소문자 통일 
    # 토큰화: 다루기 쉬운 단위로 쪼개기 - 구분자로 리스트 만듦 

    # 정제 및 조작" : 토큰에서 필요한 정보 추출, 타입 변환, 집계
    # 방어적 코드: 예상치 못한 입력에 대비해서 예외처리

    # 결과 반환: 최종 집계를 타겟 데이터 형식으로 반환 


    # Write your solution here
    if not order_data.strip():
        return {}

    result = {}

    order_list = order_data.split(",")
    for data in order_list:
        try:
            if ":" not in data:
                continue 
            
            name, qty = data.split(":")
            result[name] = result.get(name, 0) + int(qty)

        except ValueError: # int("one"), unpacking error 처리 
            continue

    return result
    """


print(process_orders("apple:3,banana:2,apple:5,orange:one,grape")) #  {'apple': 8, 'banana': 2}
print(process_orders(" "))