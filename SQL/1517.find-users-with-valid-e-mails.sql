https://leetcode.com/problems/find-users-with-valid-e-mails

- regexp_like()는 함수형태로 대소문자 옵션을 줄 수 있다. `regexp_like(컬럼, '정규식', 옵션)`
- 시작은 항상 알파벳이여야한다 ^[a-zA-Z]
- 그 뒤에는 여러개의 알파벳, 숫자, 점(period), 밑줄(underscore), 하이픈(dash)이 올 수 있다 [a-zA-Z0-9._-]* -> asterisk는 여러개 뜻함 
- 이메일의 . 이 \\ 백슬래시 두개를 붙여야 escape된다. 첫번째 백슬래시를 이용해 뒤의 백슬래시를 탈출시켜서 "\." 이게 인식되도록 함 
- 마지막의 달러사인은 꼭 이걸로 끝나야한다를 뜻함 
- 'c'옵션은 대소문자 엄격 구분 'case-sensitive', 'i' 는 insensitive

SELECT * 
FROM users
WHERE REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com$', 'c');


