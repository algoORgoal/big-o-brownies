def solution(n):
    dp = [ [ 0 for i in range(0, n + 1) ] for i in range(0, 3 + 1) ]
    
    # f(2, n) 계산
    dp[2][1] = 1
    dp[2][2] = 2
    for i in range(3, n + 1):
        dp[2][i] = dp[2][i - 1] + dp[2][i - 2]
        dp[2][i] %= 1_000_000_007
    
    dp[3][0] = 1
    dp[3][2] = 3
    for i in range(4, n + 1):
        if i % 2 == 0:
            # dp[3][i] = (dp[2][i] * 2 - 1 + dp[3][i - 4] * 2) % 1_000_000_007
            special_pattern_sum = 0
            j = 4
            while i - j >= 0:
                special_pattern_sum += (dp[3][i - j] * 2) 
                j += 2
            
            dp[3][i] = (dp[3][i - 2] * 3 + special_pattern_sum) % 1_000_000_007
        

    
    return dp[3][n]

# 3 * n
# f(3 , n): 타일링 경우의 수
# f(3 , n) = f(3, n - 2) * f(3, 2) + f(2, n) * 2
# f(3, 2) = 3

# f(2, n) = f(2, n - 1) + f(2, n - 2) (세로로 하나 추가 / 가로로 두개 추가)
# f(2, 1) = 1, f(2, 2) = 2



