https://leetcode.com/problems/percentage-of-users-attended-a-contest

- 이 문제에서 각 콘테스트별로 참여하지 않은 유저들의 목록을 전부 뽑아봄 
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