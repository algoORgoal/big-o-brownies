import heapq

# from sys import setrecursionlimit
# setrecursionlimit(10 ** 9)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)


# print(factorial(10_000))


def solution(n, m, matrix):
    return dijkstra(n, m, (0, 0), matrix, [[None for j in range(m)] for i in range(n)])


def dijkstra(n, m, start_vertex, matrix, visited):
    queue = []
    heapq.heappush(queue, (0, start_vertex))

    while len(queue) > 0:
        distance, vertex = heapq.heappop(queue)
        x, y = vertex

        if visited[x][y] != None:
            continue

        visited[x][y] = distance

        candidates = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
        for candidate in candidates:
            candidate_x, candidate_y = candidate

            if 0 <= candidate_x < n and 0 <= candidate_y < m:
                if visited[candidate_x][candidate_y] != None:
                    continue
                candidate_distance = distance + \
                    matrix[candidate_x][candidate_y]
                heapq.heappush(queue, (candidate_distance, candidate))

    return visited[n-1][m-1]


if __name__ == "__main__":
    m, n = [int(string) for string in input().split()]
    matrix = [[int(char) for char in input()] for i in range(0, n)]
    answer = solution(n, m, matrix)
    print(answer)


# node (0, 0)에서 node (n,m)까지 경로가 존재하기 위해 0 node로 바꾸어야 하는 1 node의 최소 개수
# 모든 경우의 수: 2 **  (100 * 100)! = 2 ** 10_000

# (부순 벽 정보, 개수)
# 10_000 * 10_000 = 10 ** 8
# 100_000_000 <= 1억 => 공간복잡도


# (v, 0)인 vertex (v in visited) => edge weight이 0
# (v, 1)인 vertex (v in visited) => edge weight이 1
# edge weight이 서로 다른 graph에서, (0,0) => (m,n) 사이의 최단거리 => 다익스트라 알고리즘
# 시간복잡도 O(elog e + e) 가능
# 공간복잡도 O(eloge)

# prority queue (0, start_vertex)
# while priority queue is not empty:
#   distance, vertex = priority queue.pop()
#   if vertex in visited continue
#   else
#     visited[vertex] = distance
#     for adjacent vertex in graph vertex:
#       if adjacent vertex not in visited:
#         priority queue.push(distance + edge weight(vertex, adjacent_node), adjacent vertex)


# 시간복잡도 push / pop 둘 다 O(eloge) = O(elogv**2) = O(2elogv)= O(elogv)
# 공간복잡도 O(v + e)

# 상태 (distance, vertex)
