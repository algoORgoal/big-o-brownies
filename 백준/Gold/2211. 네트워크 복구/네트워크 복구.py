import heapq


def solution(n, m, edges):
    graph = [[] for i in range(0, n + 1)]
    for vertex1, vertex2, weight in edges:
        graph[vertex1].append((vertex2, weight))
        graph[vertex2].append((vertex1, weight))

    return dijkstra(graph, 1)


def dijkstra(graph, source):
    queue = []
    visited = set()

    heapq.heappush(queue, (0, source, source))

    edges = []

    while len(queue) > 0:
        distance, node, parent = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        if node != parent:
            edges.append((parent, node))

        for adjacent_node, weight in graph[node]:
            heapq.heappush(queue, (distance + weight, adjacent_node, node))

    return edges


if __name__ == "__main__":
    n, m = [int(string) for string in input().split()]
    edges = [[int(string) for string in input().split()] for i in range(m)]
    answer = solution(n, m, edges)
    print(len(answer))
    for row in answer:
        print(*row)


# undirected graph
# connected component가 될 수 있게하는 최소 개수의 edge 찾기
# 원래 네트워크의 minimum distance == connected component의 minimum distance

# 1에서 최단거리 경로 상에 있는 edge n - 1개 선정
# edge weight가 서로 다름 => 최소 거리를 알기 위해 dijkstra's algorithm 사용해야 함
# dijkstra를 돌리면서, 이미 방문했던 node이면 다시 방문하지 않기

# 상태: (distance, current, parent)
# (current, parent)를 edges에 추가

# 시간복잡도 O(mlogn)
# 공간복잡도 O(m + n)
