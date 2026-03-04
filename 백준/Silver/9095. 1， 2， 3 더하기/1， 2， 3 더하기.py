def solution(arr):
    upper_bound = 10
    dp = [0 for i in range(0, upper_bound + 1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, upper_bound + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return [dp[i] for i in arr]


if __name__ == "__main__":
    t = int(input())
    arr = [int(input()) for i in range(0, t)]
    answer = solution(arr)
    for i in answer:
        print(i)


# 1
# 1

# 2
# 1 1
# 2

# 3
# 3
# 1 1 1
# 2 1
# 1 2


# 4
# = f(4 - 3) + f(4 - 2) + f(4 - 1) = f(1) + f(2) + f(3) = 1 + 2 + 4 = 7
# f(1) = 1, f(2) = 2, f(3) = 4
# f(k) = f(k - 3) + f(k - 2) + f(k - 1)
# 시간복잡도 O(n * len(test cases)) (n <= 10)
