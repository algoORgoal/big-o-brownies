def solution(money):
    reversed_money = list(reversed(money))
    return max(tabulation(money), tabulation(reversed_money))
    

    
def tabulation(money):
    dp = [ [ 0, 0, None, None ] for i in range(0, len(money)) ]
    for i in range(0, len(dp)):
        if i == 0:
            dp[0] = [ money[i], 0, True, False ]
        elif i == 1:
            dp[1] = [ money[i], dp[0][0], False, True ]
        else:
            # i를 쓰는 경우
            dp[i][0] = money[i] + dp[i - 1][1]
            dp[i][2] = dp[i - 1][3]
            
            # i를 안 쓰는 경우
            if dp[i - 1][0] > dp[i - 1][1]:
                dp[i][1] = dp[i - 1][0]
                dp[i][3] = dp[i - 1][2]
            else:
                dp[i][1] = dp[i - 1][1]
                dp[i][3] = dp[i - 1][3]
        
    if len(dp) > 1:
        last_index = len(dp) - 1
        if dp[last_index][2] == True:
            dp[last_index][0] -= money[0]
        if dp[last_index][3] == True:
            dp[last_index][1] -= money[1]
            
    answer = 0
    for a, b, c, d in dp:
        answer = max(a, b, answer)
        
    return answer

# 0 <= i <= 1_000_000
# 1_000_000번 연산
# dp[0] = [ money[0], 0 ]
# dp[1] = [ money[1], dp[0] ]
# dp[i] = [ money[i] + dp[i - 1][1], max(dp[i - 1][0], dp[i - 1][1]) ]

# 추가적으로, 각각이 첫번째 요소를 사용하는지 안 하는지 별도로 boolean flag를 저장
# 마지막 집을 포함하는 결과를 구할 때 첫번째 요소를 사용하는 경우, 빼버리기

