빈도 높게 쓰이는 그룹
print(): 디버깅 필수 
len(): 리스트, 문자열 길이 반환
type(x): 객체 데이터 타입 확인
str(x), int(x): 형변환
list(x), tuple(x): 이터레이터를 리스트나 튜플로 변환  
range(5): 0 부터 4까지 
enumerate(list, start=1): 하나하나 세어보다. index, value 동시에 줌 
zip(): 여러 리스트를 쌍으로 묶어줌
sorted(); 원본은 두고 정렬된 새 리스트 반환. 람다와 짝꿍
with open(): 텍스트, 로그 파일 읽고 쓸 때
reversed(iterable): 리스트를 원본 훼손 없이 역순으로 꺼내줌. 주소값만 가지고 게으른 연산을한다.
dict.setdefault(key, default_value): 딕셔너리에 특정 key가 없다면 기본값을 넣어서 가져옴. 
callable(obj): 실행 가능한 함수인지 참거짓으로 판별해줘 방어적 코드 
getattr(obj, name): 클래스나 객체 내부 변수, 메서드를 문자열 이름으로 가져올 때 사용. 다이나믹하게 사용가능 

자주 씀 그룹 
isinstance(obj, class): 이 변수가 특정 클래스 인스턴스가 맞는지 검사. 타입 체크용
sum(iterable): 리스트 안 모든 숫자를 더함
max(), min(): 최댓값, 최솟값
any(), all(): 하나라도, 모두가 참, 거짓
map(), filter(): 일괄 변환, 필터링 - 리스트 컴프리헨션 더 자주 씀
id(x): 객체 고유 메모리 주소 반환
abs(x): 숫자 절대값
round(x): 숫자 반올림 


특수 목적 그룹
dir(x): 이 객체가 어떤 메서드와 변수 가지고 있는지 목록 보여줌
divmod(a, b): 몫과 나머지를 튜플로 반환 
pow(x, y): 2**3 8 거듭제곱 계산
chr(97) -> 'a', ord('a') -> 97: 아스키 코드나 유니코드 변환
hex(x), oct(x): 16진수, 8진수 문자열로 변환.
input(): 사용자 입력받음 
eval(expression): 문자열로 된 파이썬 코드를 그대로 실행. 보안 취약점 생기므로 사용 금지 

Faker: 테스트용 가짜 데이터 생성기. 
sympy: 수학 기호 연산 라이브러리 
