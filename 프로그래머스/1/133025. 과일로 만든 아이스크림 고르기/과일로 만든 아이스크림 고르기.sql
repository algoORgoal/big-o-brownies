-- 코드를 입력하세요
-- first_half, icecream_info
-- first half: shipment_id, flavor, total_order
-- first_half 테이블의 기본 키: flavor
-- icecream_info 테이블의 기본 키: flavor

-- 주문량이 3000보다 높으면서 아이스크림의 주 성분이 과일인 아이스크림의 맛을 총 주문량이 큰 순서대로 조회
SELECT FLAVOR
FROM ICECREAM_INFO
WHERE INGREDIENT_TYPE = 'fruit_based'
  AND FLAVOR IN (
      SELECT FLAVOR
      FROM FIRST_HALF
      WHERE TOTAL_ORDER >= 3000
  )

