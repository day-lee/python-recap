def process_london_sensor_data(log_data: list[str]) -> list[dict]:
    """런던 환경 센서에서 수집된 원본 로그 데이터를 정제하는 함수입니다.

    요구사항:
    1. 입력 데이터(log_data)는 공백문자가 섞인 '날짜,센서ID,측정값' 형태의 문자열 리스트입니다.
    2. 측정값이 비어있거나 무효한 데이터(None, 빈 문자열, 숫자가 아닌 값)는 제외해야 합니다.
    3. 측정값이 50.0을 초과하는 '위험(Critical)' 데이터만 필터링하세요.
    4. 최종 결과는 각 라인을 딕셔너리 형태로 변환한 리스트로 반환해야 합니다.

    * 시니어의 힌트: 
      - 리스트 전체를 복사하지 않고 대용량 데이터를 효율적으로 순회하는 방법은 무엇일까요? 
      - 문자열을 쪼개고 공백을 제거할 때 어떤 내장 메서드가 유용할까요?
      - 조건문과 데이터 변환을 한 줄로 깔끔하게 처리할 수 있는 파이썬 고유의 문법을 고민해보세요. 

      # [입력 데이터 예시]
      # '날짜, 센서ID, 측정값' 형태이며, 공백이나 잘못된 데이터가 포함되어 있습니다.
      london_logs = [
         "2026-03-01, SENSOR_A, 55.4 ",  # 정상 & 50 초과 (포함)
         "2026-03-01, SENSOR_B, 32.1",   # 정상 & 50 이하 (제외)
         " 2026-03-01, SENSOR_C, missing ", # 무효한 측정값 (제외)
         "2026-03-01, SENSOR_D, 72.8",   # 정상 & 50 초과 (포함)
         "2026-03-01, SENSOR_E, "        # 빈 측정값 (제외)
      ]

      # [기대하는 출력 데이터 예시]
      # process_london_sensor_data(london_logs) 호출 결과는 아래와 같아야 합니다.
      expected_output = [
         {
            "date": "2026-03-01",
            "sensor_id": "SENSOR_A",
            "value": 55.4
         },
         {
            "date": "2026-03-01",
            "sensor_id": "SENSOR_D",
            "value": 72.8
         }
      ]

    """
    pass











"""
   #2차 리팩토링 
   # 1.Extract: 클렌징된 제너레이터. 스트리밍 형태로 읽어오는 
    split_data = (line.replace(" ", "").split(",") for line in log_data)

   # 2.Transform: 유효성 검사, 타입 변환 헬퍼 함수를 만들어서 씀. 
    def parse_and_filter(parsed_line):
        if (len(parsed_line)) != 3:
            return None 
        try:
            date, sensor_id, raw_value = parsed_line
            value = float(raw_value)
            if value > 50.0:
                return {"date": date, "sensor": sensor_id, "value": value }
        except ValueError: 
            return None 
        return None 
    
    #3.Load: 제너레이터로 유효한 데이터만 걸러서 내보냄. 프린트해보면 <generator object ... 0x0393>로 객체로 나와서 메모리가 안전함 
    # 괄호 위치 중요. 잘못넣어서 boolean이 출력됐었음.. 제너레이터 객체를 리턴함  
    return  (item for line in split_data if (item := parse_and_filter(line)) is not None)

    # kafka 같은 실시간 스트리밍 처리를 위해 제너레이터를 사용해서 유연하게 대응함 

   # 1차 도전 
   # 스트링 하나를 어레이로 만들고 스트립으로 클렌징해준다. 
   # 길이가 3인지 확인하고, 타입이 맞는지를 확인해준다. 
   # 맞다면 계측치가 50인것만 추려서 딕셔너리를 만들어준다. 
    result = [] 
    data = {}
    for data in log_data:
      data = data.replace(" ", "").split(",")
      date, sensor_id, _ = data 
      try: 
         value = float(data[2])
      except ValueError:
         continue

      if (len(data) == 3 and value is not None and value > 50):
         result.append({"date": date, "sensor_id": sensor_id, "value": value})
    return result
"""
raw_data = [
         "2026-03-01, SENSOR_A, 55.4 ",  # 정상 & 50 초과 (포함)
         "2026-03-01, SENSOR_B, 32.1",   # 정상 & 50 이하 (제외)
         " 2026-03-01, SENSOR_C, missing ", # 무효한 측정값 (제외)
         "2026-03-01, SENSOR_D, 72.8",   # 정상 & 50 초과 (포함)
         "2026-03-01, SENSOR_E, "        # 빈 측정값 (제외)
      ]
# print(process_london_sensor_data(raw_data))

log_stream = process_london_sensor_data(raw_data)
print(log_stream) # <generator object..>
for clean_data in log_stream:
    print(clean_data)
# {'date': '2026-03-01', 'sensor': 'SENSOR_A', 'value': 55.4}
# {'date': '2026-03-01', 'sensor': 'SENSOR_D', 'value': 72.8}