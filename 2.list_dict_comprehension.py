my_list = [i for i in range(5)]
print(my_list)

my_even_list = [i for i in range(5) if i % 2 == 0]
print(my_even_list)

fruits = ["banana", "apple", "strawberry"]
fave = [fruit for fruit in fruits if fruit == "strawberry"]
print(fave)

my_dict = {"name": "misty", "type": "cat", "age": 12, "isFemale": True}
print(my_dict.get("name"))

for data in my_dict:
    print(my_dict.get(data))

info = [my_dict.get(data) for data in my_dict]
print(info)

my_dict["color"] = "black" # This is the correct way to add a key-value pair to a dictionary

info2 = {my_dict.get(data): data for data in my_dict}
print(info2)

fruits = ["banana", "apple", "strawberry"]
# result = [ "protein" if fruit == "banana" else "fruity" for fruit in fruits]

print(result)
if else 문으로 작성할 때는 표현식 expression과 if else가 for loop 앞에 위치한다.


words = ["apple", "banana", "kiwi", "grape", "melon", "plum"]
result = [word if len(word) >= 5 else "short" for word in words ]
print(result)

2차원 리스트 평탄화 - 중첩 루프이용 - 중첩일 때는 맨 마지막 줄만 맨 앞으로 보낸다. 
matrix = [[1, 2], [3, 4], [5, 6]]
result = [j for i in matrix for j in i]
print(result)

result = []
for i in matrix:
    for j in i:
        result.append(j)
print(result)

matrix = [[1, 2], [3, 4], [5, 6]]
result = [j for i in matrix for j in i if j % 2 == 0]
print(result)

matrix = [[1, 2], [3, 4], [5, 6]]
result = [j if j % 2 == 0 else "odd" for i in matrix for j in i ]
print(result)

실무 문졔: api에서 가져온 지저분한 데이터 정제, 에러 처리시 많이 씀
정제 조건:값이 비어있는 None이거나, 공백만 있는 문자열("   ")은 제외해야 합니다.한글이 포함된 잘못된 번호("공일공-일이삼사")도 제외해야 합니다.
(힌트: 문자열이 숫자로만 이루어져 있는지 확인하는 방법 혹은 하이픈 제거 후 숫자인지 확인하는 로직이 필요합니다.)살아남은 정상적인 번호는 양쪽 공백을 제거하고, 
하이픈(-)이 있다면 전부 제거하여 숫자로만 이루어진 깔끔한 문자열로 만들어야 합니다.

값이 None 이거나 len 0 인지 확인해서 제외
정규식이나 치환 함수로 하이픈 제거, str or int 확인하는 로직 type() 
strip() 

리스트 컴프리헨션은 공백, 하이픈 제거 상태로 만들고 .isdigit()로 검사 
공백도 개수를 세서 data.strip()을 먼저 적용해줘야함
일단 컴프리헨션의 앞부분에 공백과 하이픈을 지운 값을 만들어두고, 조건부에서 그 변환된 값을 한번 더 적어서 검사한다. 
이렇게 하면 뒤에선 조건에 걸린 값은 일단 걸러질거고, 충족하는 데이터도 정제가 되어 보여진다.
정제 단계를 두차례에 나눠서 실행하면 더 깔끔하게 보인다.

raw_phones = [" 010-1234-5678", None, "01099998888 ", "   ", "공일공-일이삼사"]
cleaned_steps = [data.strip().replace("-", "") for data in raw_phones if data is not None and len(data.strip()) > 0 and data.strip().replace("-", "")]
result = [data for data in cleaned_steps if data.isdigit()]
print(result)

raw_phones = [" 010-1234-5678", None, "01099998888 ", "   ", "공일공-일이삼사"]
cleaned_data = [data.strip().replace("-", "") for data in raw_phones if data and data.strip().replace("-", "") ]
result = [data  for data in cleaned_data if data.isdigit()]
print(cleaned_data)
print(result)

raw_phones = [" 010-1234-5678", None, "01099998888 ", "   ", "공일공-일이삼사"]
조건문에서 None이나 0, 빈 스트링, 리스트, 딕셔너리, 튜플, 집합세트는 False 취급 
len(list) == 0 처럼 길게 안써도 됨. 
cleaned_data = [phone.strip().replace("-", "") for phone in raw_phones if phone and phone.strip()]
result = [data for data in cleaned_data if data.isdigit()]
print(cleaned_data, result)


휴면 상태("status": "inactive")인 회원들의 이메일만 쏙 뽑아내는 리스트 컴프리헨션
users = [
    {"name": "Kim", "email": "kim@gmail.com", "status": "active"},
    {"name": "Lee", "email": "lee@naver.com", "status": "inactive"},
    {"name": "Park", "email": "park@daum.net", "status": "active"},
    {"name": "Choi", "email": "choi@gmail.com", "status": "inactive"}
]

result = [user["email"] for user in users if user["status"] == "inactive"]
print(result)

조건에 따라 다른 값을 넣는 if-else구조는 for 문 앞으로 이동한다. 
order_prices = [65000, 23000, 50000, 12000, 98000]
result = ["free shipping" if order >= 50000 else "fee 3000" for order in order_prices]
print(result)


📝 중급 실무 문제: 월별 매출 데이터에서 '흑자 분기'만 추출하기회사에서 1년 동안 벌어들인 매출(revenue)과 지출(expense) 데이터가 분기별로 묶인 2차원 리스트로 들어왔습니다.
이 데이터에서 각 달(Month)의 순이익(매출 - 지출)을 계산하여, 순이익이 0원 이상이면 "흑자", 0원 미만이면 "적자"로 분류한 뒤, 
오직 흑자인 달의 데이터만 리스트로 뽑아내세요.

출력 목표 결과:새로운 리스트에는 "월 이름: 상태" 형태의 문자열이 담겨야 합니다. (순이익이 0원인 6월도 흑자에 포함됩니다!)
1분기, 2분기, 3분기 데이터가 묶여 있는 2차원 리스트입니다.
yearly_data = [
    [{"month": "1월", "revenue": 500, "expense": 400}, {"month": "2월", "revenue": 300, "expense": 350}],
    [{"month": "3월", "revenue": 600, "expense": 500}, {"month": "4월", "revenue": 200, "expense": 250}],
    [{"month": "5월", "revenue": 700, "expense": 400}, {"month": "6월", "revenue": 800, "expense": 800}]
]

# nested for loop -> flatten
# for loop calculation revenue - expense and condition only when plus

flattened_data = [inner_data for data in yearly_data for inner_data in data]
# print(flattened_data)

result = [ f'{data["month"]}:흑자' for data in flattened_data if data["revenue"] - data["expense"] >= 0]
print(result)
