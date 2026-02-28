import sys
sys.setrecursionlimit(10 ** 6)

class DisjointSet:
    def __init__(self, nodes):
        self.parent = { node: node for node in nodes }
        
    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
            return self.parent[a]
        return a
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            return
        
        self.parent[root_a] = root_b

def move(node, direction):
    x, y = node
    if direction == 0:
        return (x - 1, y), (x - 2, y)
    if direction == 1:
        return (x - 1, y + 1), (x - 2, y + 2)
    if direction == 2:
        return (x, y + 1), (x, y + 2)
    if direction == 3:
        return (x + 1, y + 1), (x + 2, y + 2)
    if direction == 4:
        return (x + 1, y), (x + 2, y)
    if direction == 5:
        return (x + 1, y - 1), (x + 2, y - 2)
    if direction == 6:
        return (x, y - 1), (x, y - 2)
    return (x - 1, y - 1), (x - 2, y - 2)
    

def solution(arrows):
    root = (0, 0)
    
    nodes = set()
    
    node = root
    nodes.add(root)
    
    
    for direction in arrows:
        next_node, next_next_node = move(node, direction)
        nodes.add(next_node)
        nodes.add(next_next_node)
        node = next_next_node
        
        
    disjointSet = DisjointSet(nodes)    
    
    visited_edges = set()
    
    node = root
    count = 0
    
    
    for direction in arrows:
        next_node, next_next_node = move(node, direction)
        
        edge = tuple(sorted((node, next_node)))
        if edge not in visited_edges and disjointSet.find(node) == disjointSet.find(next_node):
            count += 1
            
        visited_edges.add(edge)
        disjointSet.union(node, next_node)
        
        node = next_node
        
        edge = tuple(sorted((next_node, next_next_node)))
        if edge not in visited_edges and disjointSet.find(next_node) == disjointSet.find(next_next_node):
            count += 1
            
        visited_edges.add(edge)
        disjointSet.union(next_node, next_next_node)
        
        node = next_next_node

    return count
        
        
        


    
    
    
    

# 그래프에서 사이클의 개수를 찾는 문제
# disjoint set에서, find(current) == find(next)인 경우
# - 사이클의 개수는 방은 항상 한번에 한개씩만 추가됌
# - 예외사항: 1 => 2 => 1 같은 것은 사이클은 되나 방이 안 만들어짐
#   처리 방법: edge의 방문 여부도 따로 확인
#            sort를 통해 vertex의 순서 보장, == 연산 작동 여부 확인함