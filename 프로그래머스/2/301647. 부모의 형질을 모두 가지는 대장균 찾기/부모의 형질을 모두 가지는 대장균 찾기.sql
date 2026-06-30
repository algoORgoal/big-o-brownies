-- 코드를 작성해주세요


# 부모의 형질을 모두 보유한 대장균
SELECT child.ID, child.GENOTYPE, parent.GENOTYPE as parent_genotype
FROM ECOLI_DATA child
JOIN ECOLI_DATA parent
ON child.PARENT_ID = parent.id
WHERE parent.GENOTYPE & child.GENOTYPE = parent.GENOTYPE
ORDER BY child.ID ASC;
