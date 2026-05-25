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
- 튜플 언패킹
    def get_user_info():
        return "kim", 12, "student"
    name, age, job = get_user_info()
    print(name, age, job) # kim 12 student


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