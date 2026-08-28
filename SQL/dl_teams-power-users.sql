https://datalemur.com/questions/teams-power-users

postgresql date function
1. extract(year from column)
- 만약 year, month를 모두 추출해서 비교하려면 extract(year from column) = '2022' and extract(month from column) = '8' 
이렇게 and로 연결함 

2. to_char(column, 'YYYY-MM')


-- to_char(col, 'YYYY-MM')
SELECT sender_id, count(sender_id) messages_count
FROM messages 
where to_char(sent_date, 'YYYY-MM') = '2022-08'
group by sender_id
order by messages_count desc 
limit 2


-- extract(month from col))
SELECT sender_id, count(sender_id) messages_count
FROM messages 
where extract(month from sent_date) = '8' and extract(year from sent_date) = '2022'
group by sender_id
order by messages_count desc 
limit 2