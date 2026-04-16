from sys import stdin
from collections import deque
from math import inf

input = stdin.readline


def solution(n, m, box):
    tomato_count = 0

    for i in range(n):
        for j in range(m):
            if box[i][j] >= 0:
                tomato_count += 1

    return bfs(n, m, box, tomato_count)


def bfs(n, m, box, tomato_count):
    queue = deque()
    visited = set()

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.appendleft(((i, j), 0))
                visited.add((i, j))

    max_distance = -inf

    while len(queue) > 0:
        node, distance = queue.pop()
        x, y = node

        max_distance = max(max_distance, distance)

        candidates = (
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
            (x, y),
            (x, y),
        )

        for candidate in candidates:
            candidate_x, candidate_y = candidate
            if not (0 <= candidate_x < n and 0 <= candidate_y < m):
                continue

            if box[candidate_x][candidate_y] == -1:
                continue

            if candidate in visited:
                continue

            queue.appendleft(
                ((candidate_x, candidate_y), distance + 1))

            visited.add((candidate_x, candidate_y))

    if len(visited) < tomato_count:
        return -1

    return max_distance


if __name__ == "__main__":
    m, n = [int(string) for string in input().strip().split()]
    box = [[int(string) for string in input().strip().split()]
           for i in range(n)]

    answer = solution(n, m, box)
    print(answer)


# 1000 1000 = 10 ** 4
# 입력 딜레이 => readline

# bfs 수행하기
# 모든 칸을 방문에 성공했다 => len(visited) == h * m * n - (토마토가 들어있지 않은 칸)
#  가장 마지막 거리 반환
# 모든 칸을 방문에 실패했다 => len(visited) < h * m * n - (토마토가 들어있지 않은 칸)
#  -1 반환

# 1: 익은 토마토
# 0: 익지 않은 토마토
# -1: 토마토가 들어있지 않은 칸

# edge weight가 1로 똑같을 때, 모든 노드를 방문하는데 걸리는 거리
