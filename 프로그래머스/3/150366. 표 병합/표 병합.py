class DisjointSet:
    def __init__(self, nodes):
        self.nodes = nodes
        self.parent = { node: node for node in nodes }
        self.values = { node: None for node in nodes }
        
        self.children = { node: set([ node ]) for node in nodes }
        
        
    def find(self, node):
        if self.parent[node] == node:
            return node

        self.parent[node] = self.find(self.parent[node])
        self.children[self.parent[node]].add(node)
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 == root2:
            return
        
        if self.values[root1] is None and self.values[root2] is not None:
            self.children[root2] |= self.children[root1]
            self.children[root1] = set([ root1 ])
            self.parent[root1] = root2
        else:
            self.children[root1] |= self.children[root2]
            self.children[root2] = set([ root2 ])
            self.parent[root2] = root1
        
    
    def update1(self, r, c, value):
        node = (r, c)
        root = self.find(node)
        self.values[root] = value
        
    def update2(self, before, after):
        for key, value in self.values.items():
            if value == before:
                self.values[key] = after
    
    def merge(self, r1, c1, r2, c2):
        node1 = (r1, c1)
        node2 = (r2, c2)
        self.union(node1, node2)
        
    
    def unmerge(self, r, c):
        node = (r, c)
        root = self.find(node)
        value = self.values[root]
        
        for child in self.children[root]:
            self.parent[child] = child
            self.values[child] = None
    
        self.values[node] = value
        self.children[root] = set([ root ])
        
    def print_node(self, r, c):
        node = (r, c)
        root = self.find(node)
        if self.values[root] is None:
            return "EMPTY"
        else:
            return self.values[root]

# 1. update r c value O(1)
# 2. update value1 -> value2 O(n ** 2) 2_500
# 3. merge r1 c1 r2 c2
# 4. unmerge r c: chlidren 모두 부모 자기 자신으로 바꿈
# 5. print

# 1 <= commands <= 1_000


# 그러면 궁금한 점:
# merge 1 1 2 2
# merge 2 2 3 3
# 이렇게 되면, 3,3 -> 2,2 -> 1,1인가?
# (3, 3), (2, 2) -> (1 ,1)

# merge 1 1 2 2
# unmerge 2 2
# 병합된 셀 모두 빈 상태로 되돌리고, (r, c)의 셀에 해당 값 할당

# disjoint set을 쓰자!
# 인덱스 탐색시: find((x, y))로 루트에 접근해서 값을 바꾼다

# update r c value: find((x, y))로 루트에 접근해서, 대응하는 값을 바꾼다
# update value1 -> value2: value1 가지고 있는 모든 칸 값 수정
# merge r1 c1 r2 c2: union((r1, c1), (r2, c2))
# print r c: find((x, y))로 루트에 접근해서 대응하는 값 출력



def solution(commands):
    nodes = set()
    for i in range(1, 51):
        for j in range(1, 51):
            nodes.add((i, j))
            
    disjoint_set = DisjointSet(nodes)
    
    result = []
    
    for command in commands:
        tokens = command.split()
        if tokens[0] == "UPDATE" and len(tokens) == 4:
            r, c, value = int(tokens[1]), int(tokens[2]), tokens[3]
            disjoint_set.update1(r, c, value)
        if tokens[0] == "UPDATE" and len(tokens) == 3:
            value1, value2  = tokens[1:]
            disjoint_set.update2(value1, value2)
        if tokens[0] == "MERGE":
            r1, c1, r2, c2 = int(tokens[1]), int(tokens[2]), int(tokens[3]), int(tokens[4])
            disjoint_set.merge(r1, c1, r2, c2)
        if tokens[0] == "UNMERGE":
            r, c = int(tokens[1]), int(tokens[2])
            disjoint_set.unmerge(r, c)
        if tokens[0] == "PRINT":
            r, c = int(tokens[1]), int(tokens[2])
            result.append(disjoint_set.print_node(r, c))

    return result

# 1.  update2(value2, value2) => update2(value1, value2)
# 2.  children을 union에서도 업데이트해줘야 한다.
# 3.  - 합집합 연산은 &= 이 아니라 |= 이다.