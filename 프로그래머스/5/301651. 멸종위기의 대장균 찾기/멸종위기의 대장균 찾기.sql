# 각 세대별 자식이 없는 개체의 수, 세대 출력
# 세대에 대해 오름차순 정렬
# 각 세대 출력하기

WITH RECURSIVE TREE AS (
    SELECT ID, PARENT_ID, 1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    SELECT child.ID, child.PARENT_ID, parent.GENERATION + 1 AS GENERATION
    FROM TREE parent
    JOIN ECOLI_DATA child
    ON child.PARENT_ID = parent.ID
)

SELECT COUNT(*) AS COUNT, tree.GENERATION
FROM TREE tree
WHERE NOT EXISTS (
    SELECT 1
    FROM ECOLI_DATA child
    WHERE child.PARENT_ID = tree.ID
)
GROUP BY tree.GENERATION
ORDER BY tree.GENERATION;




