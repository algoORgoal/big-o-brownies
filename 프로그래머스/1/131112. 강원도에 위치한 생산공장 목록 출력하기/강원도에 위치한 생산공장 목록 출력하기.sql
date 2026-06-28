-- 코드를 입력하세요
# where 강원도에 위치
# select 식품공장의 공장 id, 공장 이름, 주소
# from food-factory
# order by 공장id asc;

SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '강원도 %'
ORDER BY FACTORY_ID ASC;