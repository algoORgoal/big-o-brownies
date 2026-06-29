-- 코드를 작성해주세요


# 1. skillcodes 테이블에서 이름이 Python이거나 C인 것만 남기기
# 2. developer에서 (skill_code & code) = 1인 것만 남기기
# 3. developer의 id, 이메일, 이름, 성 선택하기


WITH REQUIRED_SKILLCODES AS (
    SELECT *
    FROM SKILLCODES
    WHERE NAME IN ('C#', 'Python')
)

SELECT DISTINCT d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
FROM DEVELOPERS d
JOIN REQUIRED_SKILLCODES r
ON (d.SKILL_CODE & r.CODE) > 0
ORDER BY d.ID ASC;

