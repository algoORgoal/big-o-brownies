from math import inf

def solution(arr):
    operands = []
    operators = []
    for i in range(0, len(arr)):
        if i % 2 == 0:
            num = int(arr[i])
            operands.append(num)
        else:
            operators.append(arr[i])
    dp = [ [ [-inf, inf] for j in range(0, len(operands)) ] for i in range(0, len(operands)) ]
    
    for j in range(0, len(operands)): # length
        for i in range(0, len(operands)): # starting index
            start = i
            end = i + j
            if end >= len(operands):
                continue
                
            if start == end:
                dp[start][end][0] = operands[start]
                dp[start][end][1] = operands[start]
                continue
            
            for middle in range(start, end):
                max_result = dp[start][middle][0] + dp[middle + 1][end][0] if operators[middle] == "+" else dp[start][middle][0] - dp[middle + 1][end][1]
                min_result = dp[start][middle][1] + dp[middle + 1][end][1] if operators[middle] == "+" else dp[start][middle][1] - dp[middle + 1][end][0]
                
                dp[start][end][0] = max(dp[start][end][0], max_result)
                dp[start][end][1] = min(dp[start][end][1], min_result)
            
                    
    return dp[0][len(operands) - 1][0]
        


# dp[i][i] = arr[i] (0 <= i < 숫자의 개수)
# dp[i][j] = max(
# dp[i][i] operator dp[i + 1][j],
# dp[i][i + 1] operator dp[i + 2][j],
# ...,
# dp[i][j] operator dp[j - 1][j]) (i <= j)
# 

# 1. dp[i][i] = arr[i] 할당
# 2. for j in range: j는 길이
#      for i in range: i는 시작점 
#        for k in range(0, j + 1)
#           dp[i][j] = max(dp[i][k] operator dp[k][j])

# 틀린 부분: 합칠 때  - 인 경우 최대 최대가 아닌, 최대 / 최소가 dp[i][j]의 최댓값을 만든다.
# 따라서 각 항의 최댓값, 최솟값을 따로 구해야한다.