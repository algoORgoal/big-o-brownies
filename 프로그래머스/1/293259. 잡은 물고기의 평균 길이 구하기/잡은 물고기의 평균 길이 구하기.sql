-- 코드를 작성해주세요


# 소수점 셋째자리에서 반올림 => ROUND(LENGHT, 2)
# 10cm 이하의 물고기들은 10cm로 취급하기
# 잡은 물고기의 평균 기링 구하기(AVERAGE_LENGTH)

SELECT ROUND(AVG(IFNULL(LENGTH, 10)), 2) AS AVERAGE_LENGTH
FROM FISH_INFO

