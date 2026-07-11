-- 코드를 입력하세요
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;

# 이름이 없는 동물의 이름을 No name이라고 표시하기

