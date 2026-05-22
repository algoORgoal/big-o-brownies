from collections import deque



def solution(n, edges):
    graph = construct_graph(edges)
    
    root = 1
    a_pair = bfs(root, graph, node_count=1)[0]
    
    b_pair, candidate_pair1 = bfs(a_pair[1], graph, 2)
    
    a_pair, candidate_pair2 = bfs(b_pair[1], graph, 2)
    
    return max(candidate_pair1[0], candidate_pair2[0])    
    
def construct_graph(edges):
    graph = {}
    for vertex1, vertex2 in edges:
        if vertex1 not in graph:
            graph[vertex1] = []
            
        if vertex2 not in graph:
            graph[vertex2] = []
        
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
        
    return graph

def bfs(root, graph, node_count):
    queue = deque()
    node_to_distance_map = {}
    queue.appendleft((root, 0))
    
    while len(queue) > 0:
        node, distance = queue.pop()
        
        if node in node_to_distance_map:
            continue
        
        node_to_distance_map[node] = distance
        
        if node in graph:
            for adjacent_node in graph[node]:
                queue.appendleft((adjacent_node, distance + 1))
    
    return sorted([ (node_to_distance_map[node], node) for node in node_to_distance_map ], reverse=True)[:node_count]
        
    
        
    

# maximal value of distance(a, b) + distance(b, c) + distance(c, a) where a, b, c is in tree
# 3 <= n <= 250_000
# 세 점간의 거리 따지는 법
# root node로부터 가장 멀리 떨어진 노드 세개?

# 두 노드 간의 거리 계산: n(n - 1) => 20708500
# 31_312_375_000 계산 불가능


# A = distance(a, lca(a, b, c)), B = distance(b, lca(a, b, c)), C = distance(c, lca(a, b, c))
# 첫번째 두번째 큰거 / 첫번째 세번째 큰거 / 두번째 세번째 큰거
# f(a, b, c) = max(A, B, C) + min(A, B, C)
# lca가 x일 때 가질 수 있는 subtree에서 가져올 수 있는 가장 큰 node의 depth(a, b, c의 subtree는 모두가 일치하지 않음)
# dp[x] = 최대 두개 씩 + 1 한 다음에 subchild에서 가져와서 가장 큰 세개 고름,  for child in children
# dists += [ dist + 1 for dist in dp[child][:2]] 
# dists.append(0) => 현재 노드 
# dp[current] = sorted(dists)[:3] # 모든 dists가 같은 subtree에서 오는 것을 방지 => 그래야 current가 lca가 된다
# lca가 x일 때 f(a, b, c) 중간값 최대값: dp[current][0] + dp[current][2] if len(dp[current]) >= 3
# 모든 노드에서 dp[0] + dp[2]를 구한 것 중 최대값을 찾는다.

# lca로는 못찾는다. subtree에 있는 애들끼리 거리가 제일 멀 수도 있는데 그걸 못 찾는다.
# 트리 지름을 이용한다.
# 트리 지름이란? 트리에서, 가장 거리가 먼 노드 사이의 거리
# 두 노드 사이 거리의 최대값은 트리 지름을 통해서 구할 수 있다.
# 두 노드가 a, b라고 할 때 c를 정하는 방법: 
# max(a에서 b를 제외하고 가장 멀리 떨어진 노드의 거리, b에서 a를 제외하고 가장 멀리 떨어진 노드의 거리)
# a에서 모든 노드 사이의 거리를 나타내는 list 만들기
# b에서 모든 노드 사이의 거리를 나타내는 list 만들기
# list.pop() => b / a, 한번 더 => 그 다음으로 먼 거리의 노드 나온다.
#



#   
# construct_graph()
# bfs(root, graph, node_count): => 노드 개수 반환
# bfs 1번 기준으로 돌리기
# 가장 먼 노드 a 찾기
# bfs a번 기준으로 돌리기
# 가장 먼 노드 두개 찾기
# bfs b번 기준으로 돌리기
# 가장 먼 노드 두개 찾기

# second인 두 노드 중 거리가 더 먼 것을 반환하기

# 시간복잡도 O(n)
# 공간복잡도 O(n + m) = O(n)




