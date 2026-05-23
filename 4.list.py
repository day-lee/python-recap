리스트 연산하기: 연결(+), 반복(*), len()	

리스트 요소/리스트 추가 방법 
1. list.append(x): 값 하나 추가
- 데이터 순차 누적 

2. list.insert(index, x): 특정 인덱스에 값 추가
- 다른 인덱스 한 칸씩 밀림 
- 긴급하게 첫줄에 노출해야하거나, 우선 순위 높은 무언가를 처리해야할 때

3. list.extend(iterable) 리스트 확장 list.extend([1, 2]) 
- 다른 리스트를 이어 붙임, 요소를 펼쳤다가 다시 리스트에 넣어준다. 

4. list += [x, y]: 리스트 확장
- 변수 이름에 더 해야지 성립. 
- assign하는거라, 변수가 아닌 리스트에 바로 더하면 [1, 2] += [3,4] 에러남
- extend와 내부 동작 같음 
my_list = [3, 4]
my_list += [1, 2]  iterable 만 더할 수 있음 

5. + 연산자: 리스트 합치기 새로운 리스트 생성
- [1, 2] + [3, 4]
- += 연산자와 다른 점은 기존 리스트 변수명에 더하는 거고, 이건 아예 새로운 리스트를 만든다.


리스트에 요소 제거하기	
list.remove(값): 찾아서 첫번재로 나오는 값 지움.
- 없는 값 지우려고 하면 ValueError 
- if value in list: 처럼 방어 코드 필수 작성. 

pop(인덱스): 특정 위치의 값을 지우고 그 지워진 값을 꺼내와서 반환
- 인덱스를 비우면 맨 뒤 값을 꺼냄   
- 작업 대기열에서 일을 하나씩 꺼내서 처리하는 작업에 적당
- 가장 오래된 작업 처리 queue.pop(0) -> 현재 처리중인 작업
- 맨 뒤에 있는 값 처리 queue.pop() -> 빈 값을 줘서 맨 뒤에 있는 값 꺼냄 
- 방어 코드로 리스트가 비어있는지 확인해야함. 비어있는데 pop() 호출하면 IndexError 

리스트 내부에 있는지 확인하기: in/not in 연산자	

리스트 정렬하기: sort(), sorted()
list.sort(): 원본을 직접 변경.
- 원본 순서 파괴됨
sorted(list, reverse=True): 원본 유지, 정렬된 새로운 리스트 복사해서 반환. 
- reverse=True 는 내림차순, 인기순 
- 안정성있어 더 자주쓰임

리스트에 적용할 수 있는 기본 함수: list.min(), list.max(), list.sum()	
__reversed(list) 함수로 리스트 뒤집기
- 원본은 그대로 두고
- 순서가 뒤에서부터로 바뀐 새로운 반복 객체를 반환함 
- 최신글부터 보여주기 기능

enumerate() 함수와 반복문 조합하기
- enumerate(list, start=1)
- 반복문 돌때 데이터와 인덱스 번호를 순서대로 보여줌 
- for index, data in enumerate(list, start=1): ...
- index, data 순서

============================================================

print("_".join(['banana', "apple", "pear"]))

weekday_banner = ["Sale"]       # 평일에는 이 배너를 매일 띄웁니다.
weekend_banners = ["Event", "Gift"] # 주말(토, 일)에는 이 배너들을 띄웁니다.

weekly_schedule 결과: ['Sale', 'Sale', 'Sale', 'Sale', 'Sale', 'Event', 'Gift']
총 배너 개수 결과: 7
result = weekday_banner * 5 + weekend_banners 
print(result, len(result))


trending = ["파이썬", "노트북", "키보드"]

trending.append("마우스")
trending.insert(1, "VS Code")

print(trending)

기존에 보던 콘텐츠 리스트 (0번 인덱스가 메인 화면 맨 앞에 노출됨)
now_watching = ["무빙", "오징어게임", "지옥"]

# 방금 새로 재생을 시작한 따끈따끈한 신작
new_show = "피지컬100"

now_watching.insert(0, new_show)
print(now_watching)

실무 문제: 구버전 회원 데이터를 신버전 시스템으로 통합하기
현재 가동 중인 신버전 회원 시스템의 ID 리스트
current_users = ["user_aaa", "user_bbb", "user_ccc"]

# 백업본에서 추출한 구버전 시스템의 회원 ID 리스트
legacy_users = ["old_111", "old_222", "old_333"]

current_users += legacy_users 
# current_users.extend(legacy_users)
print(current_users)


cart = ["맥북", "마우스", "키보드", "아이패드"]
cart.remove("마우스")
print(cart)
canceled_item = cart.pop()
print(canceled_item, cart)

banned_users = ["hacker99", "spammer_kim", "bot_user1"]
user = "hacker99"
# user = "just_user"

if user not in banned_users:
    print(f"{user} is logged in")
else:
    print("Not allowed")

l = [9, 1, 2, 3, 5, 8]
# l.sort()
new_l = sorted(l, reverse=True)
print(new_l)

'최고 매출', '최저 매출', '총 매출'을 계산해보세요.
daily_sales = [
    {"date": "월요일", "revenue": 500000},
    {"date": "화요일", "revenue": 320000},
    {"date": "수요일", "revenue": 640000},
    {"date": "목요일", "revenue": 210000},
    {"date": "금요일", "revenue": 850000}
]
r = [ data["revenue"] for data in daily_sales]

print(max(r), min(r), sum(r))


comments = ["안녕하세요!", "오늘 파이썬 공부 꿀잼이네요.", "마지막 문제 풀고 쉬러 갑니다!"]

for index, comment in enumerate(reversed(comments), start=1):
    print(f"[{index}]: {comment}")

 법적 기준에 따라 가장 나중에 신청한 사람부터 역순으로 처리하려고 합니다.reversed()와 enumerate()를 조합하여 "몇 번째로 처리되는지"와 "유저 ID"를 매칭하여 출력하는 코드를 작성해 보세요.
leave_requests = ["user_A", "user_B", "user_C"]

for index, user in enumerate(reversed(leave_requests), start=1):
    print(f"처리순서 {index}: {user}")
