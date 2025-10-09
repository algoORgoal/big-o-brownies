import sys
sys.setrecursionlimit(10**7)
# adjacency matrix 시간복잡도 -> O(ev)
# adjacency list 시간복잡도 -> O(e)
# indirect graph에서 모든 경로 방문이 가능한지 아닌지 찾는 문제(오일러 경로 만들 수 있는지)
# 오일러 경로 만들 수 있는 조건: adjacent edges 홀수개인 노드 두개, 나머지 adjacent edges 짝수개

# 오일러 회로를 만들기 위한 필요충분조건
# 1. 모든 정점이 하나의 컴포넌트에 속해 있어야 한다.
# 2. 차수가 홀수인 정점의 개수가 0개 또는 2개이다.
# 2만 만족시키는 경우 반례: 삼각형 두개. 차수가 홀수인 정점의 개수가 0개이지만 모든 정점이 하나의 컴포넌트에 속해있지 않다.
# https://geniusnohkang.tistory.com/26

def main(v: int, e: int, edges: list[int]):
    graph = {}
    for source, destination in edges:
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []    
        graph[source].append(destination)
        graph[destination].append(source)
    
    oddCount = 0
    evenCount = 0
    
    visited = set()
    dfs(graph, 1, visited)

    if len(visited) < v:
        return False

    for vertex in graph:
        if len(graph[vertex]) % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1

    if oddCount == 0 or oddCount == 2:
        return True
    else:
        return False


def dfs(graph: dict[list[int]], current: int, visited: set[int]):
    adjacent_nodes = graph[current]
    if not adjacent_nodes:
        return
    for adjacent_node in adjacent_nodes:
        if adjacent_node in visited:
            continue
        visited.add(adjacent_node)
        dfs(graph, adjacent_node, visited) 

            
    

if __name__ == "__main__":
    v, e = [ int(string) for string in input().split(" ") ]
    edges = [ [ int(string) for string in input().split(" ") ]  for i in range(e) ]
    canDrawEulerianPath = main(v, e, edges)
    if canDrawEulerianPath:
        print("YES")
    else:
        print("NO")


# 1 outgoing 2, 3, 4
# 2 incoming 1 outgoing 3, 4
# 3 incoming 1, 2
# 4 incoming 1, 2