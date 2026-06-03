튜플 tuple

- 리스트와 거의 같지만 불변형이다. immutable
- 요소를 변경, 삭제할 수 없다. read-only
- 절대 변하면 안되는 고정 데이터 묶음 
- dictionary에서 list는 키가 될 수 없지만, tuple은 가능
    location_map = {
        (19.2, 299.9): "london",
        (29.1, 993.2): "brighton"
    }
- 리스트의 index, +, *, slicing 모두 사용 가능
    my_tuple[1:2]

- 튜플 패킹: 괄호없이 쉼표로만 나열하매도 튜플로 처리
  "lee", 12, "student"  == ("lee", 12, "student")
   "kim", -> 쉼표가 붙어있으니 튜플 

- iterable unpacking 반복 가능 객체 언패킹
  튜플 언패킹 
   `a, b = b, a` (Tuple Unpacking) 문법

    def get_user_info():
        return "kim", 12, "student"
        # 파이썬에서 괄호 없이 쉼표로만 나열해도 튜플로 처리됨  
    name, age, job = get_user_info()
    print(name, age, job) # kim 12 student



언패킹 연산자 * 
* 튜플 보따리를 푸는 별표 언패킹 unpacking operator 
- zip(*zipped_data), func(*args) 
- iterable 반복 가능 객체를 묶고 있는 보따리 매듭을 풀어라.
- "튜플/리스트 보따리를 해체해서 알맹이를 순서대로(positional) 정렬해줌"
주의: def wrapper(*args) 함수 정의 시에는 패킹
    앞으로 인자가 몇개 들어올지 모르니 일단 튜플 보따리로 묶어라.

- args 변수는 이런 모양이다. 
  튜플로 묶여있음 args = ({"name": "Kim"}, "M4 맥북 프로") 
- *별표를 붙이면 언패킹되면서
   original_func({"name": "Kim"}, "M4 맥북 프로") 이렇게 포지셔널 인자 2개로 복원된다. 

- zipped_data = [("Kim", 85), ("Lee", 92), ("Park", 78)]
-  zip(*zipped_data)이렇게 호출하면 아래처럼 풀어서 독립적으로 넣어준다. 
   zip(("Kim", 85), ("Lee", 92), ("Park", 78))


=============================================================
visit_logs = [
    ("user1", "main"),
    ("user2", "cart"),
    ("user1", "main"),       # 중복
    ("user3", "order"),
    ("user2", "cart"),       # 중복
    ("user1", "product_detail")
]

clean = set(visit_logs)
print(clean)


# [동료의 문제 코드]
store_map = {}

point_a = (37.5, 126.9)  # A 지점 좌표
point_b = (37.6, 127.0)  # B 지점 좌표

# 딕셔너리에 좌표를 Key로, 매장 이름을 Value로 저장 시도
store_map[point_a] = "강남점"
store_map[point_b] = "홍대점"

# 딕셔너리에는 리스트는 키로 사용할 수 없고 튜플을 사용할 수 있음. 불변성 때문임. 

print(store_map)