and는 깐깐해서 하나라도 False면 False 를 반환한다.
or은 제너러스해서 하나라도 True면 True 를 반환한다. 

Short-circuit evalation
파이썬은 효율성을 중요시함
왼쪽에서 결과가 결정되면 오른쪽은 보지도 않음 

가독성을 위해 괄호 사용하기
(O) not (4 <= len <= 25)
(X) not 4 <= len <= 25

우선순위: () -> not -> and -> or
if not is_letter and is_number:
    not is_letter를 먼저 보고, is_number를 판단함 

드모르간 법칙 (De Morgan's Laws)
조건문 뒤집기 마법 
- 괄호를 풀 때 not을 골고루 나눠주고, 가운데 기호도 뒤집는다. 

예시 
사과랑 바나나 둘다 사와라. 
사과나 바나나 하나라도 없으면 실패 
not (사과 and 바나나)
(not 사과) or (not 바나나)

not (A and B) => not A or not B (A가 아니거나, B가 아니다)
not (A or B) => not A and not B (A도 아니고 동시에 B도 아님)


나이가 20보다 많거나 같다. 미성년이 아니다 
age >= 20 == not(age < 20)
키가 180보다 작다. 키가 180보다 크거나 같지 않다. 
height < 180 == not(height >= 180) 


if - elif - else
독립 if: 여러 조건이 동시에 일어날 수 있거나 연달아 처리 되야할 떄 (동시 진행)
if,elif,else: 여러 조건중 무조건 딱 하나만 선택해서 실행해야 할 때 (양자 택일, 상호 배타적 - mutually exclusive)
    -> 신호등이 빨간불이면서 초록불일 수 없음. 딱 하나 정해야 

======================================================