https://leetcode.com/problems/confirmation-rate

- 사인업에 사인을 한 유저이지만 컨펌메이션을 아예 안보낼 수도 있으니 레프트 조인 

- count(col)은 NULL은 제외하고 숫자를 센다!! 로우가 존재해도 null 이면 0이 리턴됨 
- 집계 함수는 null을 계산에서 제외한다. 
- coalesce()는 가장 마지막에 감싸줘야한다. 연산 결과로 null이 나올 수도 있으니 (zero division) 가장 마지막에 대응해줌 
- SUM() / COUNT() 이 구조는 AVG()로 바꿀 수 있다. 
- SUM(action='confirmation')은 MySQL에서만 작동하므로 표준인 CASE 구문을 활용하는 방법도 머릿속에 넣어놓자. 

SELECT 
    s.user_id,
    -- AVG()방식
    ROUND(
        COALESCE(AVG(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END), 0), 
        2
    ) AS confirmation_rate

    -- SUM() / COUNT() 방식 
    -- ROUND(
    --     coalesce(SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(c.user_id), 0), 
    --     2
    -- ) AS confirmation_rate
FROM signups s
LEFT JOIN confirmations c USING (user_id)
GROUP BY s.user_id;

-- 
mysql 방식
- sum(action = 'confirmed')가 mysql에서는 작동하지만 표준은 아니므로 
  case when c.action = 'confirmed' then 1 else 0 end 으로 바꿔서 쓰는게 좋음 

select user_id,  coalesce((round((sum(action = 'confirmed') / count(c.user_id)), 2)), 0) as confirmation_rate
from signups s left join confirmations c 
using (user_id)
group by user_id


인덱스 
- 기본키(PK)는 그 자체로 인덱스 역할. 단일 인덱스
- 복합 인덱스는 user_id, action을 묶어서 커버링 인덱스로 만든다. 순서 중요. 
- 조인의 연결 고리가 되거나, where, group by 기준이 되는 컬럼이 앞자리에 온다. 

- confirmations 테이블: type: ref (인덱스를 통해 필요한 유저 데이터만 쏙쏙 골라냄)
- 결정적 힌트: confirmations 테이블의 Extra 항목에 Using index라는 문구가 표시됩니다. 
  (실제 테이블을 안 읽고 인덱스로만 쿼리를 처리했다는 뜻!)


EXPLAIN
① type (데이터를 어떻게 찾았는가? - 가장 중요!)
뒤로 갈수록 성능이 안 좋은 지뢰밭입니다. 우리 목표는 ALL을 피하는 것입니다.
🚀 const / eq_ref: 대박. 딱 1건만 바로 찾음 (PK로 조회할 때 나옴).

🏃‍♂️ ref: 훌륭함. 인덱스를 타고 특정 조건의 데이터 '무리'를 한 번에 슥 찾아냄. (우리가 원하는 confirmations 테이블의 상태)

🐢 index: 보통. 테이블 전체를 읽진 않았지만, 인덱스 전체를 처음부터 끝까지 훑음. (우리가 원하는 signups 테이블의 상태)

💥 ALL: 최악 (Full Table Scan). 인덱스를 전혀 못 타고 쌩 디스크를 처음부터 끝까지 다 뒤짐. 데이터 많으면 서버 멈춤.

② key (실제로 어떤 인덱스를 썼는가?)
여기에 우리가 만든 복합 인덱스 이름(예: idx_confirmations_user_on_action)이 찍혀 있어야 정상.
만약 NULL이라고 적혀 있다면 인덱스를 안 타고 ALL(풀스캔)을 하고 있다는 뜻입니다.

③ Extra (부가적인 꿀정보)컴퓨터가 쿼리를 처리하면서 낸 "속마음 한마디"라고 보시면 됩니다. 
아래 문구가 보이면 성공입니다.
✨ Using index (최고): "나 실제 테이블(디스크) 안 가고, 인덱스(메모리) 안에서만 계산 다 끝냈어!" -> 이게 바로 앞에서 말한 커버링 인덱스입니다.
⚠️ Using filesort / Using temporary (주의): "정렬하거나 그룹화하려는데 인덱스가 안 도와줘서 내가 메모리에 임시 판 짜서 노가다로 정렬했어." -> 데이터가 많으면 느려지므로 인덱스 구조를 개선해야 할 신호입니다.




--
내 방식
- zero division 에러가 나서 null 나옴. coalesce()로 대응함
- c.action is not null 안하고 그냥 컬럼 명만 넣었었음 

with confirmed as (select 
s.user_id, 
(case when c.action is not null then 1 else 0 end) as signup,
(case when c.action = 'confirmed' then 1 else 0 end) as confirmed
from signups s
left join confirmations c
using(user_id))

select user_id, coalesce(round((sum(confirmed) / sum(signup)), 2),0) as confirmation_rate
from confirmed
group by user_id