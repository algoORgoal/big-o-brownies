

def solution(m, n, puddles):
    table = [[ None for j in range(0, m + 1) ] for i in range(0, n + 1)]
    puddleSet = set()
    for y, x in puddles:
        table[x][y] = 0
        
    return dfs(table, n, m, 1, 1)

def dfs(table, n, m, x, y):
    if table[x][y] != None:
        return table[x][y]
    if n == x and m == y:
        table[x][y] = 1
        return table[x][y]
    
    table[x][y] = 0
    if x + 1 <= n:
        table[x][y] += dfs(table, n, m, x + 1, y)
    if y + 1 <= m:
        table[x][y] += dfs(table, n, m, x, y + 1)
    
    return table[x][y] % 1_000_000_007
    
    


# dp[x][y] = dp[x + 1][y] + dp[x][y + 1]
# x좌표, y좌표, 웅덩이 리스트
# 모든 상태공간 탐색시 2 ** 100 => 특정 좌표에서 destination까지 가는 경우의 수를 cache
# 2**100 => O(mn) (m <= 100, n <= 100)