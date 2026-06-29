# from online_sale and offline_sale
# select 판매 날짜, 상품 id, 유저id, 판매량
# offline_sale 테이블 판매 데이터의 user_id 값은 null로 표시
# order by 판매일 asc, 상품 id asc, 유저id asc


SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE SALES_DATE LIKE '2022-03-__'

UNION

SELECT SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE SALES_DATE LIKE '2022-03-__'

ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC;