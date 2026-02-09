import sys
sys.setrecursionlimit(10**7)



def solution(land):
    visited = [ [ False for j in range(len(land[0])) ] for i in range(len(land))]
    rowCount = len(land)
    colCount = len(land[0])
    
    for i in range(0, rowCount):
        for j in range(0, colCount):
            if visited[i][j] == False and land[i][j] > 0:
                dfs(land, i, j, visited, (i, j))
                    
    maxSum = 0
    for j in range(0, colCount):
        sum = 0
        columnSet = set()
        for i in range(0, rowCount):
            if land[i][j] != 0:
                id = visited[i][j]
                if id not in columnSet:
                    columnSet.add(id)
                    idX, idY = id
                    sum += land[idX][idY]
            
        maxSum = max(sum, maxSum)
        
    return maxSum
    
                
    
                
                
def dfs(land, x, y, visited, id):
    visited[x][y] = id
    
    rowCount = len(land)
    colCount = len(land[0])
    
    next = [[ x - 1, y ], [ x + 1, y ], [ x, y - 1], [ x, y + 1 ]]
    
    total = 0
    
    for nextX, nextY in next:
        if 0 <= nextX < rowCount and 0 <= nextY < colCount:
            if visited[nextX][nextY] == False and land[nextX][nextY] > 0:
                dfs(land, nextX, nextY, visited, id)
                total += land[nextX][nextY]
        
    land[x][y] = total + land[x][y]
    
    
# 못찾은 반례: [ 1 1 1] [1 0 1] [ 1 1 1 ]
# 가운데 뚫려있는 것
    
# 상태 정의에 필요한 것:
# x, y, id(i,j)
    
    

# 1. 각 칸에서 추출할 수 있는 석유량을 열 시추시 매번 구함 => O(n ** 2 * m ** 2) => 시간초과
# 2. 미리 각 칸에서 추출할 수 있는 석유량을 구해서 칸에 저장 후, 열의 시추량 구할 때는 다음과 같이 석유량 합 구함
#    - 첫 행이거나, 그 윗칸이 석유 없는 칸인 경우 합에 포함
#    dfs를 돌리고 돌아왔을 때 누적합을 더해줌, 이 값이 석유량
#    모든 석유 덩어리에 대해서 석유량 값을 저장
#    시간복잡도 O(n * m), 공간복잡도 O(n * m)