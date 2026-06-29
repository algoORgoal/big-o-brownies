# bass와 snapper 수를 출력하기
# join / on을 통해 잡은 물고기의 이름 확인

SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO info
JOIN FISH_NAME_INFO name_info
ON info.FISH_TYPE = name_info.FISH_TYPE
WHERE name_info.FISH_NAME in ('BASS', 'SNAPPER')