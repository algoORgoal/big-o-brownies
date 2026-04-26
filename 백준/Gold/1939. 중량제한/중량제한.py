import heapq
from math import inf


def solution(n, m, edges, source, destination):
    graph = construct_graph(edges, n)
    return dijkstra(graph, source, destination)


def construct_graph(edges, n):
    graph = {}
    for vertex1, vertex2, weight in edges:
        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []
        graph[vertex1].append((vertex2, weight))
        graph[vertex2].append((vertex1, weight))
    return graph


def dijkstra(graph, source, destination):
    pq = []

    # 최대로 견딜 수 있는 하중을 저장
    visited = {}
    for node in graph.keys():
        visited[node] = -inf

    heapq.heappush(pq, (-inf, source))  # 어떤 중량이던 싣고 갈 수 있음
    visited[source] = inf

    while len(pq) > 0:
        minus_capacity, node = heapq.heappop(pq)
        capacity = minus_capacity * (-1)

        if visited[node] > capacity:
            continue

        for adjacent_node, adjacent_capacity in graph[node]:
            next_capacity = min(capacity, adjacent_capacity)

            if visited[adjacent_node] >= next_capacity:
                continue

            visited[adjacent_node] = next_capacity

            heapq.heappush(pq, (-next_capacity, adjacent_node))

    return visited[destination]


if __name__ == "__main__":
    n, m = [int(string) for string in input().split()]
    edges = [[int(string) for string in input().split()] for i in range(m)]
    source, destination = [int(string) for string in input().split()]
    answer = solution(n, m, edges, source, destination)
    print(answer)


# 섬 => vertex
# 다리가 양방향 => undirected edge
# undirected graph
# 다리에 중량제한이 있음 => weighted
# source부터 destination까지 옮길 수 있는 물건 중량 최댓값
# 중량 최댓값 = min(이전 경로까지의 중량 최댓값, 현재 edge의 중량 최댓값)
# 중량 최댓값이 더 큰 경로를 선택해야 함

# dijkstra's algorithm에서 pq를 활용하되 음수로 값을 저장하여 중량이 높은 곳부터 접근할 수 있도록 만들기
# 시간복잡도: O(mlogm)
# 공간복잡도: O(n + m)
