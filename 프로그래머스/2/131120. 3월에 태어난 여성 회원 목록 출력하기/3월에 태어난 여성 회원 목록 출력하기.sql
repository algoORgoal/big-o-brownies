-- 코드를 입력하세요
# where 생일이 3월인 여성 회원
# select id, 이름, 성별, 생년월일
# where 전화번호 not null
# order by 회원id asc

# id => MEMBER_ID
# 이름 => MEMBER_NAME
# 성별 => GENDER
# 생년월일 => DATE_OF_BIRTH

SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE
    (GENDER = 'W'
    AND DATE_OF_BIRTH LIKE '____-03-__'
    AND TLNO IS NOT NULL)
ORDER BY MEMBER_ID ASC;
