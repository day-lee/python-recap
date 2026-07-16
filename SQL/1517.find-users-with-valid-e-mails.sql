https://leetcode.com/problems/find-users-with-valid-e-mails

- 시작은 항상 알파벳이여야한다 ^[a-zA-Z]
- 그 뒤에는 여러개의 알파벳, 숫자, 점, 밑줄, 하이픈이 올 수 있다 [a-zA-Z0-9._-]* -> 여러개 뜻함 
- 이메일의 . 이 \\ 백슬래시 두개를 붙여야 escape된다. 
- 마지막의 달러사인은 꼭 이걸로 끝나야한다를 뜻함 
- 'c'옵션은 대소문자 엄격 구분 

SELECT * 
FROM users
WHERE REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com$', 'c');
