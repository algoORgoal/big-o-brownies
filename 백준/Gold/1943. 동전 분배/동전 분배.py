from sys import stdin
from sys import setrecursionlimit

input = stdin.readline


def solution(n, coins):
    coin_sum = sum([coin * count for coin, count in coins])

    # 홀수이면 반으로 쪼개기 불가능
    if coin_sum % 2 == 1:
        return False

    half_sum = coin_sum // 2

    return dp(half_sum, coins)


def dp(target: int, coins: list[int, int]):
    dp = [-1] * (target + 1)
    dp[0] = 0

    for coin, count in coins:
        next_dp = [-1] * (target + 1)

        # 이전에 만들 수 있었던 것들은 현재 동전을 0번 소모
        for sum in range(target + 1):
            if dp[sum] >= 0:
                next_dp[sum] = count

        # 기본에 만드는 게 불가능했다면, 현재 동전을 [sum - coin]에서 한번 더 써서 제작 가능
        # 만약 음의 정수 결과라면 만드는 게 불가능함
        for sum in range(target + 1):
            if next_dp[sum] == -1 and sum - coin >= 0 and next_dp[sum - coin] > 0:
                next_dp[sum] = next_dp[sum - coin] - 1
        dp = next_dp

    return dp[target] >= 0


if __name__ == "__main__":
    for i in range(3):
        n = int(input())
        coins = [[int(string) for string in input().strip().split()]
                 for i in range(n)]
        answer = solution(n, coins)
        if answer == True:
            print(1)
        else:
            print(0)


# sum / 2를 만들 수 있는지 확인해야 된다

# n <= 100_000

# 동전 종류: 100개
# 동전으로 만들 수 있는 금액의 총 합: 100_000개
# 각 동전은 어림잡아 최대 1_000개 존재 가능
# 동전을 사용하는 모든 경우의 수 => 100 ** 1000 => TLE
# (각 동전은 최대 1000개까지 존재 가능, n <= 100_000)

# cache: (현재 사용해야되는 동전, 현재 사용하는 동전을 통해서 만들어야 하는 합)

# 100 * 100_000 = 10_000_000 = 10 ** 7
# 상태 개수는 이렇지만, 100 * 100_000 * coin_count => 시간초과
# 시간복잡도 O(nm * k)
# 공간복잡도 O(nm)

# 1: 만들 수 있음 => 1원짜리 1개
# 2: 만들 수 있음 => 2원짜리 1개
# 3: 만들 수 있음 => 3원짜리 1개

# dp[i + k * coin] = dp[i]
# 1 <= i <= 100_000
# 1 <= coin <= 100
# 코인의 개수 최대 1000개

# dp[current][target]: current번째 동전만 써서 target을 만들 수 있나?
# dp[s] == -1이면 합 s 못만들고, dp[s] >= 0이면 만들 수 있음
