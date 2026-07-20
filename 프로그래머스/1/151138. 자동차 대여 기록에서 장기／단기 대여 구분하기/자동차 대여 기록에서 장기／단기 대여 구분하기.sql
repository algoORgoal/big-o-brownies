-- 코드를 입력하세요

# 대여 시작일이 2022년 9월에 속하는 대여 기록
# 30일 이상 => 장기 대여, 그렇지 않으면 '단기 대여'로 표시


# 1. 대여 시작일 필터링, 대여기간 포함하는 cte 생성
# 2. 장기 대여 / 단기 대여 표시


WITH RENTAL_DURATION_INFO AS (
    SELECT 
        HISTORY_ID,
        CAR_ID, 
        START_DATE,
        END_DATE,
        DATEDIFF(END_DATE, START_DATE) + 1 AS DURATION
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE YEAR(START_DATE) = 2022 && MONTH(START_DATE) = 9
)

SELECT
    HISTORY_ID,
    CAR_ID,
    START_DATE,
    END_DATE,
    CASE 
        WHEN DURATION >= 30 THEN '장기 대여'
        ELSE '단기 대여'
    END AS 'RENT_TYPE'
FROM RENTAL_DURATION_INFO
ORDER BY HISTORY_ID DESC;