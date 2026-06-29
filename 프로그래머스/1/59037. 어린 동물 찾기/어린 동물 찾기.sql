# select 아이디, 이름
# from animal_ins
# where INTAKE_CONDITION != 'Aged'
# order by 아이디

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
ORDER BY ANIMAL_ID;