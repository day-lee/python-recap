https://leetcode.com/problems/percentage-of-users-attended-a-contest

- 유형: '구매 이력이 없는 고객 대상 마케팅', '수업을 듣지 않은 학생 추출'처럼 존재하지 않는 데이터(Missing Data)
    1. 이 유형은 전체 상품을 대상으로 구할 것인지: cross join 불가피, 대용량 마트 구축 후 모수 줄인 후에 작업
    2. 특정 타겟 상품 몇개에 대해서만 미 구매자를 찾을 것인지: not exists, not in 으로 필터링 
    두 가지 케이스에 따라 접근이 다름 

- 이 문제에서 각 콘테스트별로 참여하지 않은 유저들의 목록을 전부 뽑아봄 
-모든 유저와 모든 콘테스트의 가능한 조합(모든 경우의 수)을 먼저 만든 뒤, 실제 등록 내역이 없는 데이터를 찾아내는 접근법
- left join is null 패턴을 생각함 

1. 모든 유저와 모든 콘테스트 조합(경우의 수) 만들기 (cross join)
2. 전체 조합에서 실제 register에 없는 것만 골라내기 (left join is null) 

| user_id | user_name | contest_id | contest_id | user_id |
| ------- | --------- | ---------- | ---------- | ------- |
| 2       | Bob       | 215        | null       | null    |
| 7       | Alex      | 207        | null       | null    |
| 6       | Alice     | 207        | null       | null    |


with all_user_contest as (
    select u.user_id, u.user_name, c. contest_id
    from users u 
    cross join (select distinct contest_id from register) c
)

select *
from all_user_contest auc
left join register r on auc.contest_id = r.contest_id and auc.user_id = r.user_id
where r.user_id is null