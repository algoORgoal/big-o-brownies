-- 코드를 입력하세요

# 중고 거래 게시물 3건 이상 등록한 사용자
# 사용자 id, 닉네임, 전체주소, 전화번호

# 1. USER_ID = WRITER_ID로 join
# group by user_id하고, count(user_id) >= 3인 row만 남게 필터링하기

# 2. TLNO는 - 삽입하고, 도로명 주소, 상세 주소를 합쳐서 출력하기

WITH USED_GOODS_OLDTIMER AS (
    SELECT U.USER_ID, U.NICKNAME, U.CITY, U.STREET_ADDRESS1, U.STREET_ADDRESS2, TLNO
    FROM USED_GOODS_USER U
    JOIN USED_GOODS_BOARD B
    ON U.USER_ID = B.WRITER_ID
    GROUP BY U.USER_ID
    HAVING COUNT(U.USER_ID) >= 3
)

SELECT
    USER_ID,
    NICKNAME,
    CONCAT(CITY, " ", STREET_ADDRESS1, " ", STREET_ADDRESS2) AS 전체주소,
    CONCAT(SUBSTR(TLNO, 1, 3), "-", SUBSTR(TLNO, 4, 4), "-", SUBSTR(TLNO, 8, 4)) AS 전화번호
FROM USED_GOODS_OLDTIMER
ORDER BY USER_ID DESC;



