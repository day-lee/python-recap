https://leetcode.com/problems/not-boring-movies

- 문자열 매칭에 not like 써도 되고, !=, <> 써도 된다. 
- not like '%boring%' 하면 와일드 카드로 'boring'이 들어간 모든 문자열을 제외한다. 
  이 문제는 'boring' 하나만 제외한다. != 정확한 매칭 
- 홀수를 나타내려고 id % 2 = 1 

select * from cinema where description != 'boring' and id % 2 = 1 