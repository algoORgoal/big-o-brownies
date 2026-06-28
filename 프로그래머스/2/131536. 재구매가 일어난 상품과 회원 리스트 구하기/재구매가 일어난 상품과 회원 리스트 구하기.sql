-- 코드를 입력하세요
# (USER_ID, PRODUCT_ID)가 두번 이상 등장한 경우 재구매 데이터

# select 재구매한 회원 id, 재구매한 상품 id
# from online_sale
# where count(*) > 1
# group by 구매한 회원 id, 구매한 상품 id
# order by 회원id asc 상품id desc

SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) > 1 
ORDER BY USER_ID ASC, PRODUCT_ID DESC;


