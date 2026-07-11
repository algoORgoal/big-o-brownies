-- 코드를 작성해주세요
# 최대 하나의 parent item을 가진다 => tree
# 더이상 업그레이드 할 수 없는 아이템의 id, 아이템 명, 아이템의 희귀도
# 아이템 id를 기준으로 내림차순 정렬하기

# 더이상 업그레이드 할 수 없는 아이템 == 자신이 parent가 되지 않는다 => item.id = item_tree.parent_item_id인 경우가 존재하지 않는다.

# select item_id, item_name, rarity 
# from item_info
# where exists (
#   select 1
#   from item_tree
#   where item_info.item_id = item_tree.parent_item_id
# )
# 



# select item_id, item_name, rarity 
# from item_info
# where exists (
#   select 1
#   from item_tree
#   where item_info.item_id = item_tree.parent_item_id
# )

# id, 명, 희귀도, 가격

SELECT info.ITEM_ID, info.ITEM_NAME, info.RARITY
FROM ITEM_INFO info
WHERE NOT EXISTS (
    SELECT 1
    FROM ITEM_TREE tree
    WHERE info.ITEM_ID = tree.PARENT_ITEM_ID
)
ORDER BY ITEM_ID DESC;