-- 코드를 입력하세요

WITH SUMMER_FREQUENT_RENTS AS (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE >= '2022-08-01 00:00:00' AND START_DATE < '2022-11-01 00:00:00'
    GROUP BY CAR_ID
    HAVING COUNT(HISTORY_ID) >= 5
)

SELECT MONTH(history.START_DATE) AS MONTH, history.CAR_ID, COUNT(history.HISTORY_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY history
WHERE EXISTS (
    SELECT 1
    FROM SUMMER_FREQUENT_RENTS rents
    WHERE history.CAR_ID = rents.CAR_ID
) AND START_DATE >= '2022-08-01 00:00:00' AND START_DATE < '2022-11-01 00:00:00'
GROUP BY MONTH(START_DATE), CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC;





# SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(HISTORY_ID) AS RECORDS
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE EXISTS (
#     SELECT CAR_ID FROM SUMMER_FREQUENT_RENTS
# ) AND START_DATE >= '2022-08-01 00:00:00' AND START_DATE < '2022-11-01 00:00:00'
# GROUP BY MONTH(START_DATE), CAR_ID
# ORDER BY MONTH ASC, CAR_ID DESC;






# 1. where start_date >= '2022-08-01 00:00:00' and start_date < '2022-11-01 00:00:00' 으로 대여기간 조건 맞는지 거르기
# 2. group by car_id having count(history_id) >= 5
# 로, 총 대여 횟수가 5회 이상인 자동차 거르기 (summer_rent_info)

# 3. CAR_RENTAL_COMPANY_RENTAL_HISTORY join summer_rent_info on CAR_RENTAL_COMPANY_RENTAL_HISTORY.CAR_ID = summer_rent_info.car_id
# 4. where start_date >= '2022-08-01 00:00:00' and start_date < '2022-11-01 00:00:00' 으로 대여기간 조건 맞는지 거르기
# 5. group by car_id, month(start_date)
# 6. order by month(start_date) asc, car_id desc;





# 대여 시작일을 기준으로, 2022년 8월부터 10월까지 총 대여 횟수가 5회 이상인 자동차
# 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수 리스트를 출력
# 월 기준 오름차순 월이 같다면 자동차 ID를 기준으로 내림차순
# 특정 월의 총 대여 횟수가 0인 경우 결과에서 제외