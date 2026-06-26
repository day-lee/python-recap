- 이 문제는 쉬운 편이였어. select문에 이름이 필요한데 transactions에는 없으니 
- 레프트(이너 써도 됨) 조인해서 연결해주고, 유저"별" 잔고를 확인해야하니 그룹바이를 유저별로 묶었어.
- 어그리게이션 sum() 을 이용해서 모든 amount를 바로 계산했고. 

- 필터링 시 having을 쓴 이유는 group by로 묶은 후에 조건을 걸어야 하기 떄문이야. 
- where절은 having 뒤에 나오기 때문에 여기서는 쓸수 없음. 그룹으로 묶은 뒤 조건절은 having을 써야해.
- 집계 결과 값을 필터링할 때는 having
- logical query processing: FROM (+ JOIN) ➔ [2] WHERE ➔ [3] GROUP BY ➔ [4] HAVING ➔ [5] SELECT ➔ [6] ORDER BY
- 이 순서때문에 where 에서는 select alias를 쓸 수 없고, having에서는 쓸 수 있어. 


select u.name, sum(t.amount) as balance from 
transactions t
left join users u
on t.account = u.account
group by t.account
having sum(t.amount) > 10000