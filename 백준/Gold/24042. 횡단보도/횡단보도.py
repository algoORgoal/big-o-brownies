from sys import stdin
import heapq
from math import inf
from math import ceil


input = stdin.readline


def solution(n, m, edges):
    graph = {}
    for index, (vertex1, vertex2) in enumerate(edges):
        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []

        graph[vertex1].append((vertex2, index))
        graph[vertex2].append((vertex1, index))

    return dijkstra(n, m, graph, 1)


def dijkstra(n, m, graph, root):
    queue = []
    visited = set()

    heapq.heappush(queue, (0, root))

    while len(queue) > 0:
        time, node = heapq.heappop(queue)

        if node in visited:
            continue

        if node == n:
            return time

        visited.add(node)

        if node not in graph:
            continue

        for adjacent_node, index in graph[node]:
            if adjacent_node in visited:
                continue

            # m: edge의 개수
            # t: 현재 시간
            # k: 현재 edge의 번호

            next_time = max(0, ceil((time - index) / m)) * m + index + 1

            heapq.heappush(queue, (next_time, adjacent_node))

    return inf


if __name__ == "__main__":
    n, m = [int(string) for string in input().strip().split()]
    edges = [[int(string) for string in input().strip().split()]
             for i in range(m)]
    answer = solution(n, m, edges)
    print(answer)


# 7 ** 100_000
# 100개의 노드에서 7개의 노드로 갈 수 있음 => TLE

# 0번부터 m - 1번의 edge
# 0번 edge의 경우 0, M, 2M에 열림 => 주기 잘 못맞추면 기다려야 함


# 시간 - edge
# 0일 때 0번 건너기 => 1
# 1 - 5일 때 0번 건너기 => 6
# 6 - 10일 때 0번 건너기 => 11
# 11 - 15일 때 0번 건너기 => 16

# 시간 - edge
# 0 - 1일 때 1번 건너기 => 2
# 2 - 6일 때 1번 건너기 => 7
# 7 - 11일 때 1번 건너기 => 12
# 12 - 16일 때 1번 건너기 => 17


# 0번 edge: 0, 5, 10, 15에 시작
# 1번 edge: 1, 6, 11, 16에 시작
# 3번 edge: 2, 7, 12, 17에 시작
# 4번 edge: 3, 8, 13, 18에 시작
# 5번 edge: 4, 9, 14, 19에 시작


# 0번 edge, 시간 t
# ceil(t // 5) * 5
# 0 => 0 가능
# 1 => 5 가능
# 5 => 5 가능
# 6 => 10 가능

# 1번 edge, 시간 t
# ceil(max(0, t - 1 // 5)) * 5 + 1
# 0 => 1 가능
# 1 => 1 가능
# 2 => 6 가능
# 6 => 6 가능
# 7 => 11 가능

# k번 edge, 시간 t
# max(0, ceil((t - k) / m)) * m + k에 가능 => 건너고 난 뒤 시간 max(0, ceil((t - k) // m)) * m + k + 1
# m: edge의 개수
# t: 현재 시간
# k: 현재 edge의 번호


# graph: dict(vertex 번호, list[(vertex 번호, edge 번호)]) 저장
# dijkstra:
#   (현재 시간, 노드) 계산
#   방문 안 했으면 현재 노드 방문
#   다음 시간 계산에서 queue에 push

# 시간복잡도: mlog(n) (m <= 700_000)
# 13_591_896.77754609 => 가능
# 공간복잡도: O(m + n)

