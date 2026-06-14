
# ================================================

# 문제 2
# Problem Description
# You are given a single string raw_data representing user profiles retrieved from a server log.
# Individual user profiles are delimited by a semicolon (;).
# Within each profile, the user's name and age are separated by a forward slash (/).
# Write a function that parses this string and returns a list of names for all users who are strictly under 30 years old.

# 서버에 저장된 회원 정보가 아래처럼 한 줄의 긴 문자열로 들어왔어. 각 회원 정보는 세미콜론(;)으로 구분되어 있고, 회원 이름과 나이는 슬래시(/)로 묶여 있는 상태야.
# 위 raw_data 문자열을 정제해서, 나이가 30세 미만인 유저들의 '이름'만 담긴 깨끗한 리스트를 만들어 봐!
# 원하는 최종 출력 결과: ['Lee', 'Choi']

raw_data = "Kim/30;Lee/25;Park/35;Choi/28"
def clean_user_data(raw_data):
    pass -> 엣지 케이스 고려해서 짜보기 



















""" 모범 답안 1, 2
# 1. strip(): 공백 제거 습관 
def clean_user_data(raw_data):
    if not raw_data:
        return []
    
    user_list = raw_data.split(";")
    result = []

    for data in user_list:
        # 데이터 공백 제거 습관 들이기 
        data = data.strip() 
        # 데이터가 비어있거나, 슬래시(/)가 없는 경우는 건너뛰기 엣지 케이스 처리 
        if not data or "/" not in data:
            continue

        name, age = data.split("/")
        # str 에서 int로 바꿀 때 strip()으로 공백 제거 습관 들이기  
        if int(age.strip()) < 30:
            result.append(name.strip())

    return result
print(clean_user_data(raw_data))


# 2 nested list comprehension
def clean_user_data(raw_data):
    if not raw_data:
        return []
    # 가독성은 떨어지지만 list comprehension 쓸 수 있는 것 보여줄 수 있음 
    return [name for data in raw_data.split(";") 
            for [name, age] in [data.split("/")] 
            if int(age.strip()) < 30]
"""
    # name_list = raw_data.split(";") [ "Kim/30", "Lee/25", ...]
    # clean_list = []
    # result = []
    # for user in name_list:
    #     clean_list.append(user.split("/"))
    # for name, age in clean_list:
    #     if int(age) < 30:
    #         result.append(name)
    # return result

    # print(raw_data.split(";")) 
    # 순회하는 요소에서 뽑아올 때 또 split()을 적용해서 중첩 리스트를 만듦
   
    # 풀어서 쓴 뒤 다시 줄여봄. 두 줄로 줄이는게 나한테는 가독성이 좋음. [data.split("/")] 이 부분이 직관적으로 이해는 안됨. 
    # r =[ data.split("/") for data in raw_data.split(";") ]
    # r2 =[ name for name, age in r if int(age) < 30]
    # return r2

# # AI 제안 원라이너 
# result = [ name for data in raw_data.split(";") 
#             for name, age in [data.split("/")]
#             if int(age) < 30 ]
# print(result)

# splitted_data = raw_data.split(";")
# print(splitted_data)
# splitted_data_2 = [data.split("/") for data in splitted_data ]
# print(splitted_data_2)
# # result = [data[0] for data in splitted_data_2 if int(data[1]) < 30]
# # 언패킹 
# result = [name for name, age in splitted_data_2 if int(age) < 30]
# print(result)

# splitted_data = raw_data.split(";")
# splitted_data2 = [item.split("/") for item in splitted_data]
# dict_data = [ {"name": item[0], "age": item[1]} for item in splitted_data2]
# print(dict_data)
# result = [item["name"] for item in dict_data if int(item["age"]) < 30]
# print(result)

