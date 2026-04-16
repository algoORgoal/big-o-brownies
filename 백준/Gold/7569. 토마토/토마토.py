from sys import stdin
from collections import deque
from math import inf

input = stdin.readline


def solution(h, n, m, box):
    tomato_count = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] >= 0:
                    tomato_count += 1

    return bfs(h, n, m, box, tomato_count)


def bfs(h, n, m, box, tomato_count):
    queue = deque()
    visited = set()

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1:
                    queue.appendleft(((i, j, k), 0))
                    visited.add((i, j, k))

    max_distance = -inf

    while len(queue) > 0:
        node, distance = queue.pop()
        x, y, z = node

        max_distance = max(max_distance, distance)

        candidates = (
            (x - 1, y, z),
            (x + 1, y, z),
            (x, y - 1, z),
            (x, y + 1, z),
            (x, y, z - 1),
            (x, y, z + 1),
        )

        for candidate in candidates:
            candidate_x, candidate_y, candidate_z = candidate
            if not (0 <= candidate_x < h and 0 <= candidate_y < n and 0 <= candidate_z < m):
                continue

            if box[candidate_x][candidate_y][candidate_z] == -1:
                continue

            if candidate in visited:
                continue

            queue.appendleft(
                ((candidate_x, candidate_y, candidate_z), distance + 1))

            visited.add((candidate_x, candidate_y, candidate_z))

    if len(visited) < tomato_count:
        return -1

    return max_distance


if __name__ == "__main__":
    m, n, h = [int(string) for string in input().strip().split()]

    box = [[[int(string) for string in input().strip().split()]
            for j in range(n)] for i in range(h)]

    answer = solution(h, n, m, box)
    print(answer)


# 100 100 100 = 10 ** 6
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
