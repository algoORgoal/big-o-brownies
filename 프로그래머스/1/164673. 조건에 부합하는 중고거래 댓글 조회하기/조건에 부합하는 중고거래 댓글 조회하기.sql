# SELECT 게시글 제목, 게시글 id, 댓글 id, 댓글 작성자 id, 댓글 내용, 댓글 작성일
# from used_goods_board, used_goods_reply
# WHERE 2022년 10월에 작성
# order by 댓글작성일 asc, 게시글 제목 asc


# 댓글에 대한 정보를 보여주되, 참조하는 게시물의 제목을 보여줄 수 있어야 함
# 댓글 id, 댓글 작성자 id, 댓글 내용, 댓글 작성일


# used_goods_board의 primary key: board_id
# used_goods_reply의 primary key: reply id

SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, r.CREATED_DATE
FROM USED_GOODS_REPLY r
JOIN USED_GOODS_BOARD b
ON r.BOARD_ID = b.BOARD_ID
WHERE b.CREATED_DATE LIKE '2022-10-__'
ORDER BY r.CREATED_DATE ASC, b.TITLE ASC;