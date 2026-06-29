# select 아이디, 이름
# from animal_ins
# where INTAKE_CONDITION = 'Sick'
# order by animal_id

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID;