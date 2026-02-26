class DisjointSet:
    def __init__(self, n):
        self.parent = [ i for i in range(0, n) ]
    
    def find(self, a):
        if a == self.parent[a]:
            return a
        else:
            self.parent[a] = self.find(self.parent[a])
            return self.parent[a]
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            return
        
        self.parent[root_a] = root_b

def solution(n, computers):
    disjoint_set = DisjointSet(n)
    for i in range(0, len(computers)):
        for j in range(0, len(computers[i])):
            if computers[i][j] == 1:
                disjoint_set.union(i, j)
    
    roots = set()
    for i in range(0, n):
        root = disjoint_set.find(i)
        roots.add(root)

    return len(roots)


# 그래프에서 connected component의 개수 세기
# disjoint set을 통해서 connected component끼리 같은 set에 있게 만들 수 있음
# 0부터 n-1까지, find() 연산을 통해 가져오는 root를 집합에 담음
# 집합에 담기는 개수
# 시간복잡도 O(n + m) = O(n + n ** 2) = O(n ** 2)
# 공간복잡도 O(n + m) = O(n + n ** 2) = O(n ** 2)


