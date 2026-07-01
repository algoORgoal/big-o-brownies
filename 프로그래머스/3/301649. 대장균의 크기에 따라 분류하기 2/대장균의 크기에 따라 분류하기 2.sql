# critial / high / medium / low => colony_name
# 대장균 개체의 id, colony_name을 출력하는 sql문 작성
# 이 때 결과는 개체의 id에 대해 오름차순으로 정렬
# order by id asc


SELECT 
    ID,
    CASE NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC)
        WHEN 1 THEN 'CRITICAL'
        WHEN 2 THEN 'HIGH'
        WHEN 3 THEN 'MEDIUM'
        WHEN 4 THEN 'LOW'
    END AS COLONY_NAME
FROM ECOLI_DATA
ORDER BY ID ASC;