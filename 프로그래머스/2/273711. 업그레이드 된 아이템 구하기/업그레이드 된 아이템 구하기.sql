# root item, parent item(a -> b에서 a)
# rare 아이템의 다음 업그레이드 아이템(child) id, name, rarity를 출력하기
# => parent가 rare인 item인 id, name, rarity
# join을 통해 parent 정보 가져오고, 그 중에 parent의 rarity인 것 선별하여 id, name, rarity 가져오기. 정렬은 id 순으로

# select item_id, item_name, rarity
# from ITEM_INFO info
# join ITEM_TREE tree
# on info.id = tree.parent_item_id
# order by item_id desc;

SELECT child.ITEM_ID, child.ITEM_NAME, child.RARITY
FROM ITEM_TREE tree
JOIN ITEM_INFO child
ON child.ITEM_ID = tree.ITEM_ID
JOIN ITEM_INFO parent
ON parent.ITEM_ID = tree.PARENT_ITEM_ID
WHERE parent.RARITY = 'RARE'
ORDER BY child.ITEM_ID DESC;


