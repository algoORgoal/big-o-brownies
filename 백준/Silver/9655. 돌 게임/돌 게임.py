from sys import setrecursionlimit

setrecursionlimit(10 ** 3 + 10)


def solution(n):
    return traverse(0, 0, 0, n, {})


def traverse(turn, a, b, total, cache):
    if (turn, (a, b)) in cache:
        return cache[turn, (a, b)]

    rest = total - (a + b)

    if rest == 0:
        cache[turn, (a, b)] = turn ^ 1
        return cache[turn, (a, b)]

    winners = []

    if rest >= 1:
        if turn == 0:
            winner1 = traverse(turn ^ 1, a + 1, b, total, cache)
        else:
            winner1 = traverse(turn ^ 1, a, b + 1, total, cache)
        winners.append(winner1)
    if rest >= 3:
        if turn == 0:
            winner2 = traverse(turn ^ 1, a + 3, b, total, cache)
        else:
            winner2 = traverse(turn ^ 1, a, b + 3, total, cache)
        winners.append(winner2)

    if turn in winners:
        cache[turn, (a, b)] = turn
    else:
        cache[turn, (a, b)] = turn ^ 1

    return cache[turn, (a, b)]


if __name__ == "__main__":
    n = int(input())
    answer = solution(n)
    if answer == 0:
        print("SK")
    else:
        print("CY")


# 전체 상태 개수: 2 <= 300 ~ 2 ** 1000에 수렴 => 시간초과

# 현재 차례, 0이 먹은 돌의 개수, 1이 먹은 돌의 개수, 전체 돌의 개수
# 남은 돌의 개수 = 전체 돌의 개수 - (0이 먹은 돌의 개수 + 1이 먹은 돌의 개수)

# 남은 돌의 개수 == 0:
#   return !현재 차례 (이전 놈이 승리)
# 남은 돌의 개수 >= 3:
#   차례1 = (!현재 차례, 0이 먹은 돌의 개수 + 3, 1이 먹은 돌의 개수) (현재 차례가 1이었다고 가정)
# 남은 돌의 개수 >= 1:
#   차례2 = (!현재 차례, 0이 먹은 돌의 개수 + 1, 1이 먹은 돌의 개수)
# 현재 차례 in (차례1, 차례2): return True
# return False
# 최적화: 현재 차례, 0이 먹은 돌의 개수, 전체 돌의 개수를 기준으로 캐싱
