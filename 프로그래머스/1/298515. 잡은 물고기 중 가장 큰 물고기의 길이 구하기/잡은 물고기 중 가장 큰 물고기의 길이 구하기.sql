-- 코드를 작성해주세요

# 잡은 물고기 중 가장 큰 물고기의 길이를 cm를 붙여 출력

SELECT CONCAT(MAX(LENGTH), 'cm') AS MAX_LENGTH
FROM FISH_INFO

# 여러 값을 하나의 문자열로 합칠 때는 'cm'을 사용할 수 있다.