-- 코드를 입력하세요


SELECT COUNT(*)
FROM (
    SELECT NAME
    FROM ANIMAL_INS
    WHERE NAME IS NOT NULL
    GROUP BY NAME
) NAMES;

# 동물 보호소에 들어온 이름의 개수 세기