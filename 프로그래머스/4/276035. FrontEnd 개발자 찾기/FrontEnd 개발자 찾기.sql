-- 코드를 작성해주세요

# skillcodes 테이블에서, category = Front end 인 것만 거르기

# Front End 스킬을 가진 개발자만 필터링하기 
# from developers 
# join frontend_skillcodes 
# on (skill_code & code) > 0


WITH FRONTEND_SKILLCODES AS (
    SELECT NAME, CODE
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
)

SELECT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME 
FROM DEVELOPERS D
JOIN FRONTEND_SKILLCODES F
ON (D.SKILL_CODE & F.CODE) > 0
GROUP BY D.ID
ORDER BY D.ID ASC;
