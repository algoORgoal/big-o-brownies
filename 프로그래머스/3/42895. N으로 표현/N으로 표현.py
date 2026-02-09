def digits(n, count):
    if (count - 1 == 0):
        return n
    return (n * (10 ** (count - 1))) + digits(n, count - 1)


def solution(N, number):
    dp = [ set() for i in range(0, 9) ]
    dp[1].add(N)
    dp[2].add(digits(N, 2)),
    dp[2].add(N + N),
    dp[2].add(N - N),
    dp[2].add(N * N),
    dp[2].add(N // N),
    
    for i in range(3, 9):
        for j in range(1, i):
            for k in dp[i - j]:
                for l in dp[j]:
                    dp[i].add(k + l)
                    dp[i].add(k - l)
                    dp[i].add(k * l)
                    if (l > 0):
                        dp[i].add(k // l)    
        dp[i].add(digits(N, i))
    
    for i in range(0, len(dp)):
        if number in dp[i]:
            return i
    return -1
    


# dp[1] = [ 5, ]
# dp[2] = { 55, 5+5, 5-5, 5*5, 5/5 }
# dp[3] = { 555, 1/2로 만들 수 있는 조합 }
# 경우의 수(dp[1] + ... + dp[8]) = 4606