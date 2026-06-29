-- 코드를 작성해주세요


# join을 통해 parent가 자신이 되는 경우를 센다 
# 자식의 수 = parent가 자신이 되는 경우의 수

# select 개체 id, count(*)
# from ECOLI_DATA parent
# join ECOLI_DATA child
# on parent.id = child.parent_id
# order by parent.id asc;


# SELECT parent.ID, child.ID as CHILD_ID
# FROM ECOLI_DATA parent
# LEFT OUTER JOIN ECOLI_DATA child
# ON parent.ID = child.PARENT_ID
# ORDER BY parent.ID ASC


WITH parent_child AS (
    SELECT parent.ID, child.ID as CHILD_ID
    FROM ECOLI_DATA parent
    LEFT OUTER JOIN ECOLI_DATA child
    ON parent.ID = child.PARENT_ID
    ORDER BY parent.ID ASC
)


SELECT ID, COUNT(CHILD_ID) AS CHILD_COUNT
FROM parent_child
GROUP BY parent_child.ID
