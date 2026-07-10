https://leetcode.com/problems/patients-with-a-condition

- 네가 푼 방식(%DIAB1%): "글자 중간에 DIAB1이 끼어있는 엉뚱한 병명"까지 다 찾음. SVDIAB1 DIAB1S 이런게 다 걸림
- 문제의 의도: 공백을 기준으로 단어의 시작점을 정확히 인지하고 조건을 분기할 수 있는지 체크하는 것.
- separator가 공백이므로 
  - 첫 단어: 'DIAB1%' 
  - 두 번째 이후 단어: '% DIAB1%' 
  이렇게 두 가지 조건으로 나눠서 검색해야 함.
  만약 콤마였으면 "%, DIAB1%" 이렇게 두 번째 이후 단어 조건을 바꿔야 함.

SELECT patient_id, patient_name, conditions 
FROM patients 
WHERE conditions LIKE 'DIAB1%' 
   OR conditions LIKE '% DIAB1%';