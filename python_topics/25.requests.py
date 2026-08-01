
response.json()은 파이썬 객체로 파싱해줌 
csv 파일은 response.text 로 받아와야함



# ====================================================
import requests 

def fetch_data(url):

  params = {
    "key": "value"
  }
  try:
    # 서버가 5초안에 응답하지 않으면 연결을 끊어라. 시간이 지나면 requests.exceptions.Timeout 예외를 던짐. 
    # 에러 처리: 서버가 응답이 늦어 실패했습니다. -> 이 처리를 안하면 응답이 올 때까지 멈추게됨. 
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status() # 4xx, 5xx 대응 
    res_dict = response.json() # json python 객체로 파싱 후 반환 
    print(type(res_dict)) # dict
  
  except requests.exceptions.Timeout:
    print("request timed out")
  except requests.exceptions.HTTPError as http_err:
    print(f"request error: {http_err}")
  except requests.exceptions.RequestException as err:
    print(f"error: {err}")

  return None 

