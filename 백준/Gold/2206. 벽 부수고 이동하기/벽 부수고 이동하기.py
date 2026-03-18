from sys import stdin
from collections import deque
from math import inf

input = stdin.readline


def solution(n, m, matrix):
    visited = [[inf for j in range(m)] for i in range(n)]
    bfs((0, 0), visited, matrix)
    visited2 = [[inf for j in range(m)] for i in range(n)]
    bfs((n - 1, m - 1), visited2, matrix)

    minimum_distance = visited[n - 1][m - 1]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                candidates = (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)
                for first in candidates:
                    for second in candidates:
                        if first == second:
                            continue
                        first_x, first_y = first
                        second_x, second_y = second
                        if 0 <= first_x < n and 0 <= second_x < n and 0 <= first_y < m and 0 <= second_y < m:
                            minimum_distance = min(
                                minimum_distance, visited[first_x][first_y] + visited2[second_x][second_y] + 1, visited[second_x][second_y] + visited2[first_x][first_y] + 1)

    return minimum_distance if minimum_distance != inf else -1


def bfs(root, visited, matrix):
    queue = deque([(root, 1)])
    root_x, root_y = root
    visited[root_x][root_y] = 1

    while len(queue) > 0:
        current, distance = queue.pop()

        x, y = current
        candidates = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
        for candidate in candidates:
            candidate_x, candidate_y = candidate
            if 0 <= candidate_x < n and 0 <= candidate_y < m and matrix[candidate_x][candidate_y] == 0 and visited[candidate_x][candidate_y] == inf:
                visited[candidate_x][candidate_y] = distance + 1
                queue.appendleft((candidate, distance + 1))


if __name__ == "__main__":
    n, m = [int(string) for string in input().split()]
    matrix = [[int(string) for string in input().strip()] for i in range(n)]
    answer = solution(n, m, matrix)
    print(answer)


# 상태공간 2 ** 1_000
# 모든 경우의 수를 확인하기 힘들다.
# 캐싱 가능한 값: (현재 좌표, 부순 벽)

# dfs 후 결과 백트래킹 가능

# 현재 좌표 / 부순 벽 =>  1_000_000 * 1_000_000
# 여전히 시간초과


# bfs를 통해 최단거리 방문 가능
# 이 때, 각 상태에서 (현재 좌표, 벽 부수기 수행한 여부, 거리) 저장
# 각 상태에서, 벽 부수기 수행 안 했고 1이면 수행한 거까지 노드로 뻗음
# 벽 부수기 수행했고 주위 1이면 해당 노드로 뻗을 수 없음
# 상태 개수 1_000_000 * 1_000_000 => 시간 초과

# 두가지 경우로 분리 가능
# 1. 0만 방문하는 경우
# 2. 0만 방문 => 1 방문 => 0만 방문

# 1. 각각의 칸에, (0,0) 과의 최단 거리 / (n, m)과의 최단거리 기록 - bfs 활용
# 2. 각각의 1에서, (0,0)과의 최단 거리 + (n, m)과의 최단거리 기록이 가장 짧은 것 기록
# 3. (1), (2)에서 찾아진 값 중 가장 작은 값 반환
