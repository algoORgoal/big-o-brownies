from collections import deque
from sys import stdin
from sys import stdout

input = stdin.readline


def print(s):
    stdout.write(f"{s}\n")


def solution(l, root, target):
    visited_matrix = [[0 for j in range(0, l)] for i in range(0, l)]
    return bfs(l, visited_matrix, root, target)


def bfs(l, visited_matrix, root, target):
    queue = deque()
    queue.appendleft((root, 0))
    root_x, root_y = root
    visited_matrix[root_x][root_y] = 1

    while len(queue) > 0:
        current, distance = queue.pop()

        if current == target:
            return distance
        x, y = current
        candidates = [(x - 2, y - 1), (x - 2, y + 1), (x - 1, y - 2), (x - 1, y + 2),
                      (x + 1, y - 2), (x + 1, y + 2), (x + 2, y - 1), (x + 2, y + 1)]
        for candidate in candidates:
            candidate_x, candidate_y = candidate
            if 0 <= candidate_x < l and 0 <= candidate_y < l:
                if visited_matrix[candidate_x][candidate_y] == 0:
                    visited_matrix[candidate_x][candidate_y] = 1
                    queue.appendleft((candidate, distance + 1))


if __name__ == "__main__":
    test_case_count = int(input())
    for i in range(0, test_case_count):
        l = int(input())
        root = tuple(int(string) for string in input().split())
        target = tuple(int(string) for string in input().split())
        answer = solution(l, root, target)
        print(answer)


# edge weight이 같을 때, bfs를 통해 최단경로 탐색 가능
# queue에 (x, y), distance 저장하기
# 유효한 좌표이고 방문했는지 확인하고 append
# O(v + e) = O(v + 4v) = O(v)
# 입출력으로 인한 시간초과 방지하기 위해 stdin, stdout 사용
