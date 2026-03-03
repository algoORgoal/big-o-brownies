from collections import deque
from math import inf
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


def solution(n, k):
    path = bfs(n, k, set())
    path_length = len(path) - 1
    path_string = " ".join([str(i) for i in bfs(n, k, set())])
    return path_length, path_string


def get_path(current, parent, path=deque()):
    path.appendleft(current)

    if current != parent[current]:
        get_path(parent[current], parent, path)


def bfs(root, target, visited):
    parent = {}
    queue = deque()
    queue.appendleft(root)
    visited.add(root)
    parent[root] = root

    while len(queue) > 0:
        current = queue.pop()

        if current == target:
            path = deque()
            get_path(current, parent, path)
            return path

        candidates = [current - 1, current + 1, current * 2]

        for candidate in candidates:
            if candidate < 0 or candidate > 100_000:
                continue
            if candidate in visited:
                continue
            visited.add(candidate)
            parent[candidate] = current
            queue.appendleft(candidate)

    return inf


if __name__ == "__main__":
    n, k = [int(string) for string in input().split(' ')]
    answer = solution(n, k)
    for i in answer:
        print(i)


# 두 지점 사이의 최단경로
# edge weight가 동일함
# 일반적인 bfs로 가능
# 다만 경로를 들고 있어야 함
# disjiont set의 parent와 동일하게 bfs를 통해 탐색되는 tree 구조를 parent로 저장 가능
