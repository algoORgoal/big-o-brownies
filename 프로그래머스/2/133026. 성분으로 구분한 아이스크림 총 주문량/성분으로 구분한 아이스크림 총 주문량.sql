# first_half, icecream_table

# 재료 유형별
# 총 주문량 조회

SELECT I.INGREDIENT_TYPE, SUM(H.TOTAL_ORDER) AS TOTAL_ORDER
FROM ICECREAM_INFO I
JOIN FIRST_HALF H
ON I.FLAVOR = H.FLAVOR
GROUP BY I.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER


# 1. icecream_info와 first_half join
# 2. group by로 같은 ingredient type끼리 묶기
# 3. sum(total_order)가 total order가 된다.