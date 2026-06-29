# select count(*)
# from user_info
# where 2021년에 가입, 20세 이상 29세 이하

SELECT COUNT(*)
FROM USER_INFO
WHERE JOINED LIKE '2021-__-__' AND AGE >= 20 AND AGE <= 29 