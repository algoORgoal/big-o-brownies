# genotype => 형질
# 2번 형질을 보유하지 않으면서 1번이나 3번 형질을 보유하고 있는 대장균 개체의 수 불러오기

# from ecoli_data
# select count(*)
# where (GENOTYPE & 2) = 0 and (genotype & 1) > 0 and (genotype & 4) > 0


SELECT COUNT(*) as COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0 AND (GENOTYPE & 5) > 0



