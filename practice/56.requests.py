import requests
# API 호출 결과(JSON)를 파이썬 리스트/딕셔너리로 변환했을 때와 동일한 데이터 구조입니다.
MOCK_USERS_DATA = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874"
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org"
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv",
        "address": {
            "street": "Victor Plains",
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771"
        },
        "phone": "010-692-6593 x09125",
        "website": "anastasia.net"
    },
    {
        "id": 3,
        "name": "Clementine Bauch",
        "username": "Samantha",
        "email": "Nathan@yesenia.net",
        "address": {
            "street": "Douglas Extension",
            "suite": "Suite 847",
            "city": "McKenziehaven",
            "zipcode": "59590-4157"
        },
        "phone": "1-463-123-4447",
        "website": "ramiro.info"
    }
]


def get_user_email_by_id(user_id: int) -> str:
    """
    [Problem Statement]
    You are given a free public API endpoint that returns a list of mock users:
    URL: https://typicode.com
    
    Your task is to write a function that fetches the data from this endpoint 
    and returns the email address of the user with the given 'user_id'.
    
    [Requirements]
    1. Send a HTTP GET request to the URL.
    2. Parse the JSON response into a Python list of dictionaries.
    3. Find the user dictionary where the "id" matches the 'user_id' parameter.
    4. Return that user's "email" as a string.
    5. If the user_id does not exist, return an empty string "".
    
    [Example]
    If user_id is 1, the function should return "Sincere@april.biz".

    [Notes]: 가짜 url이라 mock 데이터 이용해서 처리해야함  
    """
    pass








    """ exception handling하고 mock data로 필터링하기 모범 답안
    url = "https://typicode.com"
    res_data = []
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() 
        res_data = response.json()
    # raise_for_status()는 상태코드가 4xx, 5xx일 때 HTTPError 예외를 발생시킴 
    except (requests.exceptions.Timeout, requests.exceptions.HTTPError, requests.exceptions.RequestException):
        print("Error happened: we will use mock data instead!!!!") 
        res_data = MOCK_USERS_DATA
    for data in res_data:
      if data.get("id") == user_id:
        return data.get("email", "")
    return ""
    
    print(res_data)
    """
# Test your code below
if __name__ == "__main__":
    print(f"Result for ID 1: {get_user_email_by_id(1)}")  # Expected: Sincere@april.biz
    print(f"Result for ID 999: {get_user_email_by_id(999)}")  # Expected: ""


"""
상태 코드 확인 언급 
데이터 구조 파악: api 결과가 배열 형태이니 for loop으로 하나씩 검사하겠습니다. 
예외 케이스: 존재하지 않는 id가 나오면 에러가 나지 않도록 기본값 반환 처리를 하겠습니다. 
"""