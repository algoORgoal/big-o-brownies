-- 코드를 입력하세요
SELECT
    ORDER_ID,
    PRODUCT_ID,
    OUT_DATE,
    CASE
        WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
        WHEN OUT_DATE > '2022-05-02' THEN '출고대기'
        ELSE '출고미정'
    END AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID ASC;


# 주문양, 생산일자, 입고일자, 출고일자
# 2022년 5월 1일까지 출고 => 출고완료
# 이후 날짜 => 출고대기
# NULL => 출고미정