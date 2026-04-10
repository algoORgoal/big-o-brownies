from math import inf
import heapq


def solution(n, matrix):
    visited = [[False for j in range(n)] for i in range(n)]
    return dijkstra((0, 0), (n - 1, n - 1), matrix, visited)


def dijkstra(root, destination, matrix, visited):
    n = len(matrix)

    queue = []
    root_x, root_y = root
    root_cost = matrix[root_x][root_y]
    heapq.heappush(queue, (root_cost, root))

    while len(queue) > 0:
        cost, node = heapq.heappop(queue)
        x, y = node

        if visited[x][y] == True:
            continue

        visited[x][y] = True

        if node == destination:
            return cost

        candidates = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)

        for candidate in candidates:
            candidate_x, candidate_y = candidate
            if 0 <= candidate_x < n and 0 <= candidate_y < n:
                heapq.heappush(
                    queue, (cost + matrix[candidate_x][candidate_y], candidate))

    return inf


if __name__ == "__main__":
    i = 0
    while True:
        n = int(input())

        if n == 0:
            break

        matrix = [[int(string) for string in input().split()]
                  for i in range(n)]
        answer = solution(n, matrix)
        print(f"Problem {i + 1}: {answer}")

        i += 1

# graph로 모델링 가능
# source에서 destination까지의 shortest path
# edge weight이 서로 다름
# dijkstra's algorithm 사용 가능
# O(mlogn) (n <= 125 * 125, m <= 4 * 125 * 125)
