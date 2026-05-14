from math import inf

def solution(land):
    r, c = len(land), 4
    
    dp = [[ -inf for j in range(c) ] for i in range(r) ]
    
    for i in range(r):
        if i == 0:
            dp[0][0] = land[0][0]
            dp[0][1] = land[0][1]
            dp[0][2] = land[0][2]
            dp[0][3] = land[0][3]
        else:
            dp[i][0] = land[i][0] + max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][3])
            dp[i][1] = land[i][1] + max(dp[i - 1][0], dp[i - 1][2], dp[i - 1][3])
            dp[i][2] = land[i][2] + max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][3])
            dp[i][3] = land[i][3] + max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
    
    return max(dp[-1])


    
    

    



# n * 4
# 땅을 밟으면 점수를 얻는다.
# 같은 열을 연속해서 밟을 수 없다.

# 0 <= i < n

# if i == 0
# dp[0][0] = arr[0][0]
# dp[0][1] = arr[0][1]
# dp[0][2] = arr[0][2]
# dp[0][3] = arr[0][3]

# else
# dp[i][0] = arr[i][0] + max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][3])
# dp[i][1] = arr[i][1] + max(dp[i - 1][0], dp[i - 1][2], dp[i - 1][3])
# dp[i][2] = arr[i][2] + max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][3])
# dp[i][3] = arr[i][3] + max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])

# 정답: max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2], dp[n - 1][3])
