# 자동차가 세단 또는 SUV
# 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능
# 30간의 대여 금액이 50만원 이상 200만원 미만
# 자동차 ID, 자동차 종류, 대여 금액 리스트를 출력하는 SQL문 작성하기
# 대여 금액을 기준으로 DESC, 자동차 종류를 기준으로 ASC, 자동차 ID DESC;

# 3, 23, 27, 18


WITH FILTERED_CAR_HISTORY AS (
    SELECT car.CAR_ID, car.CAR_TYPE, car.DAILY_FEE, history.START_DATE, history.END_DATE
    FROM CAR_RENTAL_COMPANY_CAR car
    LEFT OUTER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY history
    ON car.CAR_ID = history.CAR_ID
    WHERE car.CAR_TYPE IN ('세단', 'SUV')
),
AVAILABLE_CAR_INFO AS (
    SELECT CAR_ID, CAR_TYPE, DAILY_FEE
    FROM FILTERED_CAR_HISTORY
    GROUP BY CAR_ID, CAR_TYPE, DAILY_FEE
    HAVING
        COUNT(*) = COUNT(
            CASE
                WHEN START_DATE IS NULL THEN 1
                WHEN END_DATE IS NULL THEN 1
                WHEN END_DATE < '2022-11-01' THEN 1 
                WHEN '2022-11-30' < START_DATE THEN 1
            END
        )
),
ON_SALE_CAR_INFO AS (
    SELECT
        available.CAR_ID, available.CAR_TYPE,
        FLOOR(available.DAILY_FEE * (1 - 0.01 * discount.DISCOUNT_RATE) * 30) AS FEE
    FROM AVAILABLE_CAR_INFO available
    LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN discount
    ON available.CAR_TYPE = discount.CAR_TYPE AND discount.DURATION_TYPE = '30일 이상'
)

SELECT CAR_ID, CAR_TYPE, MIN(FEE) AS FEE
FROM ON_SALE_CAR_INFO
GROUP BY CAR_ID, CAR_TYPE
HAVING MIN(FEE) >= 500000 AND MIN(FEE) < 2000000
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC

# SELECT CAR_ID, CAR_TYPE, MIN(FEE) AS FEE
# FROM ON_SALE_CAR_INFO
# GROUP BY CAR_ID, CAR_TYPE
# HAVING MIN(FEE) >= 500000 AND MIN(FEE) < 2000000
# ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC

# SELECT * FROM AFFORDABLE_CAR_INFO


# GROUP BY car.CAR_ID
# HAVING NOT (
#     (history.START_DATE <= '2022-11-01' AND '2022-11-01' <= history.END_DATE)
#     AND
#     (history.START_DATE <= '2022-11-30' AND '2022-11-30' <= history.END_DATE)
# )


# start_date <= 2022-11-30 <= end_date

# ('2022-11-30 00:00:00' < history.START_DATE OR history.END_DATE < '2022-11-01 00:00:00')



# car type in ('세단', 'SUV')

# 대여 기록이 모두
#   2022년 11월 30일 < start_date
#   or
#   end_date < 2022년 11월 1일
# 인 차

# => join으로 계산

# 할인 금액 빼고 대여 금액 계산
# => join으로 계산
# 7일 이상, 30일 이상, 90일 이상
# 대여기간이 7일 미만인 경우 할인정책 없음

# 50만원 이상, 200만원 미만인 자동차
# ID, 종류, 대여 금액 리스트 출력하는 sql문 작성하기
# order by fee asc, car_type asc, car_id desc;


# 문제점: 전혀 대여되지 않았던 car는 history에 없어서 누락된다.
# 해결 방법: left outer join을 사용하고, null 처리를 해준다.

# 문제점: group by로 묶인 모든 행이 특정 조건을 만족하는지 확인하고 싶다.
# 해결 방법: HAVING COUNT(*) = COUNT(CASE)를 사용한다.

# 문제점: CASE 같은 경우에는 반환 값이 있는 경우 행을 만든다.
# 해결 방법: 행을 만들지 않기 위해 else clause를 빼버린다.




# start_date <= 2022-11-01 <= end_date
# start_date <= 2022-11-30 <= end_date