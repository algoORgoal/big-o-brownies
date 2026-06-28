-- 코드를 입력하세요
# where 서울에 위치한 식당
# from rest_review info
# join rest_info review
# on info.rest_id = review.rest_id
# select 식당 id, 식당 이름, 음식 종류, 즐겨찾기 수, 주소, avg(리뷰 점수)
# group by 식당 id
# order by 평균점수 desc, 즐겨찾기수 desc;

SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, ROUND(AVG(R.REVIEW_SCORE), 2) as SCORE
FROM REST_INFO I
JOIN REST_REVIEW R
ON I.REST_ID = R.REST_ID
WHERE I.ADDRESS LIKE '서울특별시 %' OR I.ADDRESS LIKE '서울시 %'
GROUP BY I.REST_ID
ORDER BY ROUND(AVG(R.REVIEW_SCORE), 2) DESC, I.FAVORITES DESC;
