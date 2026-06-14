# 문제 1
# 웹사이트 결제 시스템 로그에서 수집된 "지저분한 가격 문자열 리스트"가 있어.이 데이터들을 정제해서 진짜 계산이 가능한 정수(int) 리스트로 변환해야 해.

raw_prices = ["  1,500원 ", " 23,000원", "700원  ", "  120,500원 "]
raw_prices_2 = [""]
raw_prices_3 = "1500원" # Not a list

def clean_prices(raw_price):
    pass











"""
엣지 케이스를 고려해서 작성함

def clean_prices(raw_price):
    if not isinstance(raw_price, list):
        return "Not a list"
    result = []
    for price in raw_price:
        new_price = price.strip().replace(",", "").replace("원","")
        if new_price.isdigit():
            result.append(int(new_price))
    return result 

print(clean_prices(raw_prices))
print(clean_prices(raw_prices_2))
print(clean_prices(raw_prices_3))
"""
# , 와 원이 하드 코딩 되어 있어서 다른 문자가 섞이면 바로 고장남. 더 범용적인 코드를 고려해야함 -> regex 언급 
# return [int(data.strip().replace(",", "").replace("원", "")) for data in raw_prices]
        
#   return [int(price.strip().replace(",", "").replace("원", "")) for price in raw_prices]

# result = [int(data.strip().replace("원", "").replace(",", "")) for data in raw_prices]
# print(result)

# int_price = [int(price.strip().replace(",", "").replace("원", "")) for price in raw_prices] 
# print(int_price)






