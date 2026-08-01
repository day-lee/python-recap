리스트의 단짝, 중복 데이터를 단 한 줄로 날려버리는 세트 set(list) 

- 중복을 허용하지 않음
- unordered, 순서 없음 -> index 못쓴다.
- 합집합(union) |
- 교집합(intersection) & 
- 차집합(difference) -
- 내부에 해시 테이블 구조를 써서 속도가 압도적으로 빠리다. list는 순서대로 훑어봐야해서 느리다. 
- 특정 데이터가 들어있는지 찾을 때 유용하다. 
- 리스트 형태라면 set()로 변경한 뒤 in 사용해야함. list in하면 병목생김.
    black_list_set = set(massive_black_list)
    if user_id in black_list_set:
        print("차단된 유저입니다.")
- 리스트는 O(n), 셋은 O(1)

- add()는 요소 하나만 추가할 때
- update()는 iterable을 한꺼번에 합칠 때 
    my_set = {"Kim", "Lee"}
    my_set.update(["Choi", "Jung"])  # 세트에 리스트 합침  
    # {'Kim', 'Lee', 'Choi', 'Jung'}

- 세트 컴프리헨션: { expression for item in iterables }
   딕셔너리와 비슷하게 생겼지만 콜론으로 키:벨류 구분이 되는 점에서 다르다. 

====================================================
user_ids = ["user1", "user2", "user1", "user3", "user2", "user4"]

print(set(user_ids)) # {'user2', 'user4', 'user1', 'user3'}
print(list(set(user_ids))) # ['user2', 'user4', 'user1', 'user3']

아래 목록은 set { }
# 서비스의 전체 유료 기능 목록
premium_features = {"VOD", "LIVE_CHAT", "HD_QUALITY", "DOWNLOAD"}

# 현재 로그인한 유저가 사용 가능한 기능 목록
user_permissions = {"VOD", "LIVE_CHAT", "FREE_EMOJI"}

print(premium_features & user_permissions)

print(premium_features - user_permissions)


