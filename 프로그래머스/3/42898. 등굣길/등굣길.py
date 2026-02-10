def solution(m, n, puddles):
    dp = [ [ 0 for j in range(0, m + 1) ] for i in range(0, n + 1)]
    puddleSet = set()
    for puddleY, puddleX in puddles:
        puddleSet.add((puddleX, puddleY,))
    
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if (x, y,) in puddleSet:
                dp[x][y] = 0            
            elif x - 1 > 0 and y - 1 > 0:
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
            elif x - 1 > 0:
                dp[x][y] = dp[x - 1][y]
            elif y - 1 > 0:
                dp[x][y] = dp[x][y - 1]
            elif x == 1 and y == 1:
                dp[x][y] = 1
            dp[x][y] %= 1_000_000_007
                
    return dp[n][m]


# dp[x][y] = dp[x][y - 1] + dp[x - 1][y] if y - 1 >= 0, x - 1 >= 0
#            dp[x][y - 1] if x - 1 == 0
#            dp[x - 1][y] if y - 1 == 0
#            1            otherwise
