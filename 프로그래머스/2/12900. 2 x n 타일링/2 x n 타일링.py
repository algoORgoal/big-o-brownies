def solution(n):
    dp = [ 0 for i in range(0, n + 1) ]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %=  1_000_000_007
    return dp[n]


# dp[1] = 1, dp[2] = 2
# dp[i] = dp[i - 1] + dp[i - 2]

# time complexity: O(n)
# space complexity: O(n)