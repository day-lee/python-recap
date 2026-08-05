https://leetcode.com/problems/find-books-with-no-available-copies

-- 토털 카피 수랑 빌려가서 아직 리턴안된 수가 일치하면 리턴해준다.
-- return_date가 is null 이면 빌려간거다.
-- 카운트해준다. 그룹바이
-- library_books가 레코드 수가 적을테니 여기 기준 조인을 해준다. 토탈 카피랑 레코드 수가 같으면 만족 
-- 직관적인 편이라 easy 레벨 예외 처리가 들어가면 medium이 된다. 

with no_return as (select book_id, count(book_id) cnt
from borrowing_records
where return_date is null
group by book_id) 

select lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year,  nr.cnt current_borrowers
from library_books lb join no_return nr using(book_id)
where lb.total_copies = nr.cnt
order by current_borrowers desc, title asc


-- 다른 대안 쿼리
- 빌려간 기록에 책 정보를 조인해주고, 그룹바이에 나타나는 모든 정보를 기입해준다(어차피 책 한권은 유니크해서 오류안남)
- having 절에서 토탈 카피랑 빌려간 수가 같으면 만족

SELECT 
    lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year,
    COUNT(*) AS current_borrowers
FROM borrowing_records br
JOIN library_books lb USING (book_id)
WHERE br.return_date IS NULL
GROUP BY lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year, lb.total_copies
HAVING COUNT(*) = lb.total_copies
ORDER BY current_borrowers DESC, title ASC;
