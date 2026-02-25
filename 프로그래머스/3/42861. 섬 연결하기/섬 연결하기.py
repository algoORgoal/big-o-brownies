from functools import cmp_to_key


class DisjointSet():
    def __init__(self, n):
        self.n = n
        self.parent = [ i for i in range(0, n) ]
    
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
        if root_a != root_b:
            self.parent[root_b] = root_a
    
def comparator(a, b):
    a_cost = a[2]
    b_cost = b[2]
    
    return a_cost - b_cost
    

def solution(n, costs):
    sorted_costs = sorted(costs, key=cmp_to_key(comparator))
    disjointSet = DisjointSet(n)
    
    current = 0
    for vertex1, vertex2, cost in sorted_costs:
        if disjointSet.find(vertex1) == disjointSet.find(vertex2):
            continue
        else:
            disjointSet.union(vertex1, vertex2)
            current += cost
    return current
            
    
         
    
    
    
    
    

# minimum spanning tree
# 모든 노드 간에 path가 존재하는, cost의 합이 최소인 tree

# priority queue 사용
  # 1. priority queue에 긴선 모두 담음
# 2. proirity queue에 Edge가 있는 동안:
#     edge를 꺼냄
#     또는 node1, node2가 방문되지 않았을 경우
#     방문 처리
#     sum += cost

# 시간복잡도 mlogm = n ** 2 * log n ** 2 = n ** 2 * log n
# 공간복잡도 O(n)

# 중간에 요소 삽입/삭제가 필요 없어서 정렬만 해도 됌
# 반례: node1, node2가 모두 방문되어도 서로 다른 connected component에만 있고 경로가 존재하지 않을 수 있다.
# 해결방법: 같은 connected component에 있는지 확인하기 위해서, union-find의 find() 연산을 수행한다.
# 루트가 다르면 다른 connected component 안에 있으므로 union 연산을 통해 두 connected component를 연결한다.


# Kruskal's Algorithm
# 정렬 후 edge가 사이클을 형성하는지 확인
# 사이클 형성하는지 아닌지는 disjoint-set(union-find)를 통해서 확인 가능
# find(): root 요소 반환, 시간복잡도 O(1) 
# union(): union, 시간복잡도 O(1)