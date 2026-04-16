from sys import stdin
from collections import deque

input = stdin.readline


def solution(n, k, m, sets):
    return bfs(1, n, sets)


def bfs(source, destination, sets):
    queue = deque()
    visited_sets = set()
    visited_nodes = set()

    queue.appendleft((source, 1))
    visited_nodes.add(source)

    while len(queue) > 0:
        node, distance = queue.pop()

        if node == destination:
            return distance

        for index, vertex_set in enumerate(sets):
            if index in visited_sets:
                continue
            if node not in vertex_set:
                continue

            visited_sets.add(index)

            for vertex in vertex_set:
                if vertex in visited_nodes:
                    continue

                visited_nodes.add(vertex)
                queue.appendleft((vertex, distance + 1))

    return -1


if __name__ == "__main__":
    n, k, m = [int(string) for string in input().strip().split()]
    sets = [set([int(string) for string in input().strip().split()])
            for i in range(m)]
    answer = solution(n, k, m, sets)
    print(answer)


# vertex 1000개를 1000번 연결 =>
# ((1000 * 999) / 2) * 1000 = 499_500_000.0
# edge가 5억개 => 시간초과


# 1 2 3
# 2 3 4 5


# 1에서 시작
# for set in sets:
#   if 1 in set:
#     for num in set:
#       if num not in visted:
#         visited.add(num)
#         queue.appendleft((distance, num))

# 방문하는 집합의 개수: 최대 1000개
# 방문하는 노드의 개수: 100_000개
#   매번 노드를 방문할 때마다 모든 집합의 요소 접근: 100_000 * 1000 * 1000
#   이전에 방문한 집합 방문 X => 100_000 * 1000 O(nm)

# 시간복잡도:
# queue에는 num이 각각 최대 1번씩 들어감 => O(n)
#   각각의 num을 탐색할 때 set m개 탐색 => O(m)
# 시간복잡도: O(nm) = 100,000,000
# 공간복잡도: O(n + mk)
