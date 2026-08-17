# JSON parsing 
* 형태가 예쁘다 (1, 2번): `pd.read_json()` 또는 `pd.json_normalize()`
* 형태가 복잡, Dirty, 대용량 (3, 4번): Python 반복문, items(), 조건문을 활용해 직접 List of List로 정제 후 DataFrame화 

-------------------------------------------------------------------------------
## 1. Level 1: 완전 깔끔하고 단순한 구조 (기본 Load)
구조가 평면적(Flat)이고, Key-Value Pair 
Key가 Column이 되고, Value가 값으로 매핑 

* 해결법: pd.read_json()을 쓰거나, Python 내장 json.loads() 후 pd.DataFrame()으로 바로 변환
* 예시: List of Dictionaries, JSON Array
[ 
  {"id": 1, "name": "Alice", "city": "Seoul"},
  {"id": 2, "name": "Bob", "city": "Busan"}
]


## 2. Level 2: 약간 복잡한 중첩 구조 (Pandas 내장 기능 활용)
딕셔너리 안에 또 다른 딕셔너리가 들어있는 standard nested 구조입니다. 
굳이 Loop을 돌지 않아도 Pandas의 내장 함수로 해결이 가능합니다.

* 특징: 구조는 중첩되어 있지만, 모든 레코드의 형태가 일정하고 규칙적임.
* 해결법: pd.json_normalize() 함수. 이 함수는 중첩된 Key를 user.name, user.age처럼 점(. ) 표기법을 써서 평면적인 테이블로 자동으로 펼쳐줍니다.
* 예시: pd.json_normalize(data)를 쓰면 info.name, info.age 컬럼이 자동으로 생깁니다. 

[
  {"id": 1, "info": {"name": "Alice", "age": 25}},
  {"id": 2, "info": {"name": "Bob", "age": 30}}
]


## 3. Level 3: 아주 복잡하거나 Dirty한 구조 (Loop + List of List 방식)
"dict.items()로 Loop을 돌며 List of List 형태로 만드는 단계"
실무 파이프라인에서 가장 손이 많이 가는 파트

* 특징:
* 어떤 데이터에는 Key가 있고, 어떤 데이터에는 Key가 없음 (비정형).
   * Value 자리에 단순 값이 아니라 딕셔너리와 리스트가 무작위로 섞여 있음.
   * 데이터가 오염되어 형식이 일정하지 않음 (Dirty Data).
* 해결법: Python 코드로 한 줄 한 줄 직접 파싱(Custom Parsing)해야 합니다.
1. 빈 리스트(matrix = [])를 생성합니다.
   2. .items()나 for row in data로 반복문을 돕니다.
   3. if, try-except 문, get(key, default)을 사용해 "Key가 없으면 None 대입", "리스트면 첫 번째 원소만 추출" 같은 예외 처리를 합니다.
   4. 정제된 값만 추출해 하나의 행(Row)을 [value1, value2, value3] 형태로 만듭니다.
   5. 이를 matrix.append(row) 하여 최종적으로 List of Lists를 만든 후, 
   pd.DataFrame(matrix, columns=[...])로 변환합니다.


## 4. Level 4: 대용량 + 중첩 데이터 (Json Lines / 분산 처리)
* 특징: 파일 하나가 몇 GB가 넘어가서 read_json을 쓰면 메모리가 터지는 경우(OOM). 
 혹은 줄바꿈으로 구분된 JSON (JSON Lines, .jsonl).
* 해결법:
* 파일을 한 줄씩 읽는 Generator(open('file.json', 'r') 후 for line in f)를 사용하여 메모리 아낀다. 
   * 데이터 규모가 더 커지면 Pandas 대신 PySpark의 spark.read.json()을 사용하여 분산 환경에서 스키마를 정의(Ddl/StructType)하고 변환합니다.

