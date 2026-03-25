from math import inf
from collections import deque


def solution(n, m, ladders, snakes):
    ladder_table = {low: high for low, high in ladders}
    snake_table = {high: low for high, low in snakes}

    return bfs(1, {}, ladder_table, snake_table)


def bfs(root, visited, ladder_table, snake_table):
    queue = deque([])
    queue.appendleft((0, root))
    visited[root] = 0

    while len(queue) > 0:
        distance, current = queue.pop()

        candidates = [current + i for i in range(1, 7)]

        for candidate in candidates:
            if candidate in ladder_table:
                candidate = ladder_table[candidate]
            if candidate in snake_table:
                candidate = snake_table[candidate]

            if candidate in visited:
                continue
            if candidate > 100:
                continue

            visited[candidate] = distance + 1
            queue.appendleft((distance + 1, candidate))

    return visited[100]


if __name__ == "__main__":
    n, m = [int(string) for string in input().split()]
    ladders = [[int(string) for string in input().split()] for i in range(n)]
    snakes = [[int(string) for string in input().split()] for i in range(m)]
    answer = solution(n, m, ladders, snakes)
    print(answer)


# 모든 경우의 수:
# 1~100 칸에서 각각 주사위 1~6까지 굴린다 => 100 * 6 = 10 ** 12 = 1_000_000_000_000
# 불가능

# dp[1] = 0
# dp[2] = 1, ... dp[7] = 1
# dp[n] = min(dp[n - 1], dp[n - 2], dp[n - 3], dp[n - 4], dp[n - 5], dp[n - 6], dp[table[n]])
# table의 key: 높은 곳, value: 낮은 곳 (사다리)
# 뱀을 타는 순간 무조건 손해 => n - 1 ~ n - 6이 뱀이 있는 칸인지 확인하고 거르기
# 그런데 사다리 고려 => dp[n] =

# 시간복잡도: O(100)
# 공간복잡도: O(100 + n + m)

# dp로 풀 수 없다.
# 반례: 사다리를 탔다가, 뱀을 탔다가, 사다리를 타는 게 최적인 경우도 있다.
# 1 => 80 => 81 => 50 => 51 => 99 => 100
# 1 - 80: 사다리, 81 => 50: 뱀, 51 => 99: 사다리

# 완전탐색을 통해서 풀되, 각각의 최단거리만 구하면 된다.
# 뱀 or 사다리의 edge weight: 0
# bfs로 해결 가능하다.
# 상태: (위치, 거리)
# 후보 = (위치 + 1) ~ (위치 + 6)
# if 후보 not in visited:
#   visited[후보] = 후보 거리
#   if 후보 in ladder_table:
#     queue.add((ladder_table[후보], 거리))
#   if 후보 in snake_table:
#     queue.add((snake_table[후보], 거리))
#
# return visited[100]

# 문제점: edge weight가 서로 다를 때는 bfs가 정답을 못 찾는다.
# dijkstra algorithm을 사용해야 한다.
# 문제: 다만 사다리나 뱀이 있는 특정 좌표에 이동했을 때, 선택지가 하나로 강제되므로 주사위를 굴려서는 안 된다.
# 따라서 bfs로도 풀 수 있기는 하다.
# 주사위 굴리기 + 뱀/사다리 타는 경우

# 시간 복잡도: O(elogv) (e <= v * 7, v <= 100)
