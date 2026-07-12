-- 코드를 입력하세요
# PRIMARY KEY: FLAVOR
# FIRST_HALF TABLE의 SHIPMENT_ID는 JULY TABLE의 SHIPMENT_ID의 외래키

# 1. 달별 맛 주문량 총합을 구하기 위해, JULY_TOTAL_ORDER_INFO 테이블 만들기 (group by, sum 사용)
# 2. 상반기 주문량 총합과 7월 주문량 총합을 더한 TOTAL_ORDER_INFO 테이블 만들기 (LEFT OUTER JOIN 사용하여 값 엇는 경우에도 대응하기)
# 3. TOTAL_ORDER_INFO에서 총 주문량 높은 세개의 맛 뽑기


WITH JULY_TOTAL_ORDER_INFO AS (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER 
    FROM JULY
    GROUP BY FLAVOR
),
TOTAL_ORDER_INFO AS (
    SELECT half.FLAVOR, IFNULL(half.TOTAL_ORDER, 0) + IFNULL(july.TOTAL_ORDER, 0) AS TOTAL_ORDER
    FROM FIRST_HALF half
    LEFT OUTER JOIN JULY_TOTAL_ORDER_INFO july
    ON half.FLAVOR = july.FLAVOR
)


SELECT FLAVOR
FROM TOTAL_ORDER_INFO
ORDER BY TOTAL_ORDER DESC
LIMIT 3;


# 같은 맛의 아이스크림도 다른 출하번호(다른 공장) 가질 수 이씅ㅁ
# 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회하는 sql문 작성하기


# mint_chocolate 1700 400 = 2100
# peach 2450 500 = 2950
# caramel 2600 460 = 3060


