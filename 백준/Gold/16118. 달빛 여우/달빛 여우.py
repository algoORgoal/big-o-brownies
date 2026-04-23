import heapq
from math import inf
from sys import stdin

input = stdin.readline


def solution(n, m, edges):
    source = 1
    graph = create_graph(edges, n)
    rabbit_distances = rabbit_dijkstra(graph, source, n)
    wolf_distances = wolf_dijkstra(graph, source, n)

    count = 0
    for node in range(1, n + 1):
        if rabbit_distances[node] < min(*wolf_distances[node]):
            count += 1

    return count


def create_graph(edges, n):
    graph = {i: [] for i in range(1, n + 1)}
    for start, end, weight in edges:
        graph[start].append((end, weight * 2))
        graph[end].append((start, weight * 2))

    return graph


def rabbit_dijkstra(graph, source, n):
    pq = []
    distances = [inf for i in range(n + 1)]
    heapq.heappush(pq, (0, source))

    while len(pq) > 0:
        distance, node = heapq.heappop(pq)

        if distances[node] < distance:
            continue

        for adjacent_node, weight in graph[node]:
            next_distance = distance + weight
            if distances[adjacent_node] <= next_distance:
                continue

            distances[adjacent_node] = next_distance

            heapq.heappush(pq, (next_distance, adjacent_node))

    return distances


def wolf_dijkstra(graph, source, n):
    pq = []
    distances = [[inf, inf] for i in range(n + 1)]

    heapq.heappush(pq, (0, source, 1))

    while len(pq) > 0:
        distance, node, can_rush = heapq.heappop(pq)

        if distances[node][can_rush] < distance:
            continue

        distances[node][can_rush] = distance

        for adjacent_node, weight in graph[node]:
            if can_rush == True:
                next_distance = distance + (weight // 2)
            else:
                next_distance = distance + (weight * 2)

            if distances[adjacent_node][can_rush ^ 1] <= next_distance:
                continue

            distances[adjacent_node][can_rush ^ 1] = next_distance
            heapq.heappush(
                pq, (next_distance, adjacent_node, can_rush ^ 1))

    return distances


if __name__ == "__main__":
    n, m = [int(string) for string in input().strip().split()]
    edges = [[int(string) for string in input().strip().split()]
             for i in range(m)]
    answer = solution(n, m, edges)
    print(answer)

# shortest path from 1 to all nodes
# 토끼: edge weight 그대로 따름
# 늑대: edge를 홀수번째에 지날 때는 절반으로 줄어들고, 짝수번째에 지날 때는 2배로 늘어난다.

# edge weight가 있음 => 다익스트라 활용
# 토끼의 최단경로 길이는 다익스트라 활용
# 늑대의 최단경로 길이:
# (거리, vertex, 짝수번)
# (거리, vertex, 홀수번)
# 으로 나눠서, 짝수번일 경우에는 다음 거리 넣을 때 edge weight 1/2으로 계산하고 다음 노드는 홀수번이 됌
#           홀수번일 경우에는 다음 거리 넣을 때 edge weight * 2로 계산하고 다음 노드는 짝수번이 됌
# 토끼의 최단 경로 길이 < 늑대의 최단 경로 길이인 노드의 개수 찾기

# 시간복잡도 O(mlogm)
