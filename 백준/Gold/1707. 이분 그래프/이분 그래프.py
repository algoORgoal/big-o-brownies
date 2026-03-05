from sys import setrecursionlimit
from sys import stdin
from sys import stdout

input = stdin.readline


def print(s):
    stdout.write(f"{s}\n")


setrecursionlimit(10 ** 6)


def solution(v, e, edges):
    graph = {}
    for vertex1, vertex2 in edges:
        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)

    visited = {}

    for i in range(1, v + 1):
        if i not in visited:
            visited[i] = 0
            if dfs(graph, i, visited) == False:
                return False

    return True


def dfs(graph, current, visited):
    if current not in graph:
        return True

    adjacent_nodes = graph[current]

    for adjacent_node in adjacent_nodes:
        if adjacent_node in visited:
            if visited[adjacent_node] == visited[current]:
                return False
        else:
            inverse_color = 1 ^ visited[current]
            visited[adjacent_node] = inverse_color
            if dfs(graph, adjacent_node, visited) == False:
                return False

    return True


if __name__ == "__main__":
    k = int(input())
    for i in range(0, k):
        v, e = [int(string) for string in input().split()]
        edges = []
        for i in range(0, e):
            edge = [int(string) for string in input().split()]
            edges.append(edge)
        answer = solution(v, e, edges)
        if answer == True:
            print("YES")
        else:
            print("NO")

# adjacency list 그래프 만들기
# dfs 순환
# 이웃한 노드 중, 방문된 노드인 경우 현재 노드의 color와 다른지 확인
#   다르지 않다면 탐색 중단하고 False 반환
# 이웃한 노드 중 방문되지 않은 노드 다시 탐색
# True를 반환

# 시간복잡도 O(v + e)
# 공간복잡도 O(v + e)

# input하는 개수가 너무 많아서 IO 병목 걸린 것으로 추정
