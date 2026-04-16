from sys import stdin
from math import inf
import heapq

input = stdin.readline


def solution(n, m, a, b, c, edges):
    graph = [[] for _ in range(n+1)]
    weight_set = set()
    for vertex1, vertex2, weight in edges:
        graph[vertex1].append((vertex2, weight))
        graph[vertex2].append((vertex1, weight))
        weight_set.add(weight)

    # max_weight이가 n일 때 최단경로 cost <= max_weight가 n + 1일 때 최단경로 cost
    # 최단경로 cost가 c 이하인 경로 중 max_weight의 최솟값

    sorted_edge_weights = sorted(weight_set) + [1_000_000_001]

    start = 0
    end = len(sorted_edge_weights) - 1

    while start < end:
        mid = (start + end) // 2
        max_weight = sorted_edge_weights[mid]
        cost = dijkstra(graph, a, b, max_weight, n, c)

        if cost <= c:  # [start, mid], 현재 max_weight으로는 cost가 c 이하인 최단경로를 만들 수 있음
            end = mid
        else:  # (mid, end], 현재 max_weight으로는 cost가 c 이하인 최단경로를 만들 수 없음
            start = mid + 1

    if start == len(sorted_edge_weights) - 1:
        return -1

    return sorted_edge_weights[start]


def dijkstra(graph, source, destination, max_weight, n, max_cost):
    queue = []
    costs = [10 ** 15] * (n + 1)
    costs[source] = 0

    heapq.heappush(queue, (0, source))

    while len(queue) > 0:
        cost, node = heapq.heappop(queue)

        if cost > costs[node]:
            continue

        if node == destination:
            return cost

        for adjacent_node, weight in graph[node]:
            if weight > max_weight:
                continue

            next_cost = cost + weight

            if next_cost >= costs[adjacent_node]:
                continue
            if next_cost > max_cost:
                continue

            costs[adjacent_node] = cost + weight
            heapq.heappush(queue, (cost + weight, adjacent_node))

    return 10 ** 15


if __name__ == "__main__":
    n, m, a, b, c = [int(string) for string in input().strip().split()]
    edges = [[int(string) for string in input().strip().split()]
             for i in range(m)]
    answer = solution(n, m, a, b, c, edges)
    print(answer)

# indirect graph

# 1. 가지고 있는 돈으로 갈 수 없으면 -1
# 2. 가지고 있는 돈으로 갈 수 있으면:
#      갈 수 있는 경로 중에서 max edge weight이 가장 낮은 경로 찾기

# cost 이하인 경로가 존재하는지 여부 확인 => Dijkstra's algorithm
# cost 이하인 경로 중에서 max edge weight이 가장 낮은 경로 찾기


# 수치심 = max edge weight 값
# max edge weight 값을 줄이고 싶을 수록 같거나 더 많은 돈이 필요하고, max edge weight을 늘리면 같거나 더 적은 돈이 필요하다.

# max edge weight이 n일 때 최단거리 <= max edge weight이 n + 1일 때 최단 거리
# 1 <= edge weight <= 1_000_000_000
# 다익스트라 * 이진탐색 시간복잡도: O(mlog(n) * log(1_000_000_000)
# 최댓값:
# 248_292_141.02104458 => 시간제한 5초이므로 넉넉히 가능
