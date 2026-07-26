-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE 
    ANIMAL_TYPE = 'Dog' 
    AND (
        NAME LIKE '%el%'
        OR NAME LIKE '%eL%'
        OR NAME LIKE '%El%'
        OR NAME LIKE '%EL%'
    )
ORDER BY NAME ASC, ANIMAL_ID ASC;

# 이름에 el이 들어가는 개의 아이디와 이름 조회
# 이름 순으로 조회