zip()
- 여러개의 리스트를 묶어서 한 번에 반복문 돌릴 때
- 같은 인덱스 원소끼리 짝을 맞춰 묶어줌 
- list(), dict() 로 이터레이터 객체를 감싸야 결과를 볼 수 있음 
zip(*(Packed data)) 
- 묶인 데이터 앞에 * 별표를 붙여준다
- 언패킹

- 주의: 길이가 다른 두 리스트를 zip() 하면 데이터 누락됨
- 가장 짧은 길이 리스트에 맞춰서 연산을 끝냄
- 만약 데이터 누락 방지하려면 itertools 내장 모듈 사용해야함. 
- None, 0 등으로 채워 줌 


all(조건)
- 리스트 안 모든 요소가 True 일 때 True 반환
any(조건)
- 리스트안에 단 하나라도 True가 있으면 True 반환
-short-circuit 이라서 all()은 False 하나 만나면 바로 종료, any()는 첫번째 True를 만나면 바로 종료 - 성능이 좋음 

- all(), any()는 zip()과 자주 쓰임 


=====================================================

name = ["kim", "lee", "park"]
score = [100, 20, 85]

print(list(zip(name, score)))
# [('kim', 100), ('lee', 20), ('park', 85)]
print(dict(zip(name, score)))
# {'kim': 100, 'lee': 20, 'park': 85} 

for name, score in zip(name, score):
    print(f"{name.title()} got {score}")

묶인 리스트를 풀고싶을 때
zipped_data = [("Kim", 85), ("Lee", 92), ("Park", 78)]

r = zip(*zipped_data)
# [('Kim', 'Lee', 'Park'), (85, 92, 78)]
names, scores = r
print(names, scores)

names = ["Kim", "Lee", "Park", "Choi"]
scores = [85, 92, 78]

# r = list(zip(names, scores))
# print(r)

from itertools import zip_longest
result = list(zip_longest(names, scores, fillvalue=0))
print(result)

[('Kim', 85), ('Lee', 92), ('Park', 78), ('Choi', 0)]

names, scores = zip(*result)
print(names, scores)

midterm = [80, 92, 75, 88]
final   = [85, 95, 70, 90]

all_improved = all(f > m for m, f in zip(midterm, final))
print(all_improved)