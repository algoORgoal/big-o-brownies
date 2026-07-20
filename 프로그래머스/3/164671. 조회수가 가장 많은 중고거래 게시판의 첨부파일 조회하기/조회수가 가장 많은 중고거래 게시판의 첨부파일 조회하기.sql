# 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로 조회하기

# 1. 조회수가 가장 높은 중고거래 게시물 뽑기
# 2. from most_viewed_post join used_goods_file on board_id
# CONCAT('/home/grep/src/', BOARD_ID, '/', 'FILD_ID', 'FILE_NAME', 'FILE_EXT') as file_path


WITH MOST_VIEWED_BOARD AS (
    SELECT BOARD_ID, VIEWS
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 1
)

SELECT
    CONCAT('/home/grep/src/', B.BOARD_ID, '/', F.FILE_ID, F.FILE_NAME, F.FILE_EXT) AS 'FILE_PATH'
FROM MOST_VIEWED_BOARD B
JOIN USED_GOODS_FILE F
ON B.BOARD_ID = F.BOARD_ID
ORDER BY F.FILE_ID DESC;


