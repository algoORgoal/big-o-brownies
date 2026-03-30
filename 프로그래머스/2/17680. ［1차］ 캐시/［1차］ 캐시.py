
class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data
        
class LinkedList:
    def __init__(self, size):
        self.head = None
        self.tail = None
        self.table = {}
        self.size = size
    
    def appendleft(self, node):
        if self.head != None:
            prev, next = node, self.head
            prev.next, next.prev = next, prev
            
            self.head = node
        
        if self.head == None:
            self.head = node
        
        
        if self.tail == None:
            self.tail = node
        
        
    def get(self, data):
        # table 안에 있을 경우: 노드 제거하고 head 쪽에 붙이기
        if data in self.table:
            node = self.table[data]
            prev, next = node.prev, node.next
            if node != self.head:
                prev.next = next
            if node != self.tail:
                next.prev = prev
                
            if node == self.head:
                self.head = next
            if node == self.tail:
                self.tail = prev
            
            self.appendleft(node)
            
            return 1
        else:
            # table 안에 없을 경우: head 쪽에 붙이기, table에 주소 추가하기
            # size full일 경우 가장 오래된 놈 삭제하기
            node = Node(data)
            self.appendleft(node)
            self.table[data] = node
            
            if len(self.table) > self.size:
                prev, next = self.tail.prev, self.tail
                self.table.pop(self.tail.data)
                self.tail = prev
                
                if self.head == next:
                    self.head = prev
            
            return 5
            
        
    def print(self):
        current = self.head
        while current != None:
            print(current.data, end=" ")
            current = current.next
        print()
            
    
    


def solution(cacheSize, cities):
    linked_list = LinkedList(cacheSize)
    cost = 0
    for city in cities:
        cost += linked_list.get(city.lower())
    return cost


# LRU
# 각 도시가 주어졌을 때, cache 안에 있는지 확인하기
# cache 안에 있으면, 가장 최근 시간으로 업데이트하기 => 그 전에 쓰였던 놈들은 뒤로 한칸씩 밀림
# cache 안에 없으면, 가장 예전에 쓰였던 cache는 제거하기
# linked list 활용

# 위치 찾기 => O(n), 최대 도시 수 O(n)
# O(n ** 2) n <= 100_000 => 10 000 000 000 => 시간초과
# 대안: hash table 사용해서 각각의 노드 레퍼런스 기억하기, 단 cache 제거할 때 같이 지우고, cache에 추가할 때 노드 레퍼런스 같이 추가
# 위치 찾기 => O(1)
# O(n)

# cache 안에 있을 때, 1 추가
# cache 안에 없을 때, 5 추가

# LinkedList에서 필요한 상태
# head tail

# Node에서 필요한 상태
#  prev next data(도시 이름)

# HasthTable
#  도시 이름 => Node
