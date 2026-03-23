from sys import setrecursionlimit

setrecursionlimit(10 ** 3 + 10)


def solution(n):
    return traverse(0, 0, n, {})


def traverse(turn, spent, total, cache):
    if (turn, spent) in cache:
        return cache[turn, spent]

    rest = total - spent

    if rest == 0:
        cache[turn, spent] = turn
        return cache[turn, spent]

    winners = []

    if rest >= 1:
        winner1 = traverse(turn ^ 1, spent + 1, total, cache)
        winners.append(winner1)
    if rest >= 3:
        winner2 = traverse(turn ^ 1, spent + 3, total, cache)
        winners.append(winner2)

    if turn in winners:
        cache[turn, spent] = turn
    else:
        cache[turn, spent] = turn ^ 1

    return cache[turn, spent]


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

# 누가 먹었는지가 중요하지 않으므로, a/b를 별도로 관리할 필요가 없음. 현재 먹은 갯수만 계산
