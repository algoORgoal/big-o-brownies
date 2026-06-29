

# select id, 길이
# from fish_info
# order by ISNULL(length, 0) asc, id asc
# limit 10


SELECT ID, LENGTH
FROM FISH_INFO
ORDER BY IFNULL(LENGTH, 0) DESC, ID ASC
LIMIT 10;




