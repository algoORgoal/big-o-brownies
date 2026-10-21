-- 코드를 작성해주세요


# SKILLCODE에서 python과 c# 만 뽑기
# developers의 skill code에 대해 skillcode의 code와 & 연산했을 때 0보다 큰지 확인하기
# 0보다 크면 해당 개발자의 ID, 이메일, 이름, 성 조회하기

WITH REQUIRED_SKILLCODES AS (
SELECT *
FROM SKILLCODES
WHERE NAME IN ('Python', 'C#')
)

SELECT DISTINCT(D.ID), D.EMAIL, D.FIRST_NAME, D.LAST_NAME 
FROM DEVELOPERS D
JOIN REQUIRED_SKILLCODES R
ON D.SKILL_CODE & R.CODE > 0
ORDER BY D.ID ASC;





