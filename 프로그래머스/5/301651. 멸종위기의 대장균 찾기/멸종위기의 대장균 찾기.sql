# ecoli_data
# 1. 각 row에 대해서 세대 매기기 => 재귀적으로
#    base case: parent id is null
#    inductive case: parent.id = child.parent_id
# 2. 같은 세대에 대해서 groupby로 묶기
# 3. count를 통해 동일 세대의 개수 세기, 
# 4. 세대에 대해서 오름차순 정리하기


WITH RECURSIVE TREE AS (
    SELECT ID, PARENT_ID, 1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    SELECT CHILD.ID, CHILD.PARENT_ID, TREE.GENERATION + 1 AS GENERATION
    FROM ECOLI_DATA CHILD
    JOIN TREE
    ON CHILD.PARENT_ID = TREE.ID
)


SELECT COUNT(*) AS COUNT, GENERATION
FROM TREE
WHERE NOT EXISTS (
    SELECT 1
    FROM ECOLI_DATA CHILD
    WHERE CHILD.PARENT_ID = TREE.ID
)
GROUP BY GENERATION
ORDER BY GENERATION ASC;


