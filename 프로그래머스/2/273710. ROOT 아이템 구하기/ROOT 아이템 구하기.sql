-- 코드를 작성해주세요

# direct acyclic graph

# 아이템 id, 아이템 명을 출력하는 sql을 작성하기
# 결과는 아이템 id를 기준으로 오름차순


SELECT info.ITEM_ID, info.ITEM_NAME
FROM ITEM_INFO info
JOIN ITEM_TREE tree
ON info.ITEM_ID = tree.ITEM_ID
WHERE tree.PARENT_ITEM_ID IS NULL
ORDER BY info.ITEM_ID ASC;

# item_info join item_tree on info.item_id = item_tree.item_id
# where item_tree.parent_item_id is null
# order by item_id asc;

