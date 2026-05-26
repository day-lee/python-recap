# 웹사이트 결제 시스템 로그에서 수집된 "지저분한 가격 문자열 리스트"가 있어.이 데이터들을 정제해서 진짜 계산이 가능한 정수(int) 리스트로 변환해야 해.

raw_prices = ["  1,500원 ", " 23,000원", "700원  ", "  120,500원 "]

# trim()
# replace()
# int() 

int_price = [int(price.strip().replace(",", "").replace("원", "")) for price in raw_prices] 
print(int_price)


# 서버에 저장된 회원 정보가 아래처럼 한 줄의 긴 문자열로 들어왔어. 각 회원 정보는 세미콜론(;)으로 구분되어 있고, 회원 이름과 나이는 슬래시(/)로 묶여 있는 상태야.

# 위 raw_data 문자열을 정제해서, 나이가 30세 미만인 유저들의 '이름'만 담긴 깨끗한 리스트를 만들어 봐!원하는 최종 출력 결과: ['Lee', 'Choi']
raw_data = "Kim/30;Lee/25;Park/35;Choi/28"

[['kim', 30], ['lee', 25]]
[{"name": "kim", "age": 30}]

splitted_data = raw_data.split(";")
splitted_data2 = [item.split("/") for item in splitted_data]
dict_data = [ {"name": item[0], "age": item[1]} for item in splitted_data2]
print(dict_data)
result = [item["name"] for item in dict_data if int(item["age"]) < 30]
print(result)

