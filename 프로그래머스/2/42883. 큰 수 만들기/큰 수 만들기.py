class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, node):
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            return
    
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        
        
        
    def pop(self, node):
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
            return
        if node is self.head:
            self.head = node.next
            self.head.prev = None
            return
        if node is self.tail:
            self.tail = node.prev
            self.tail.next = None
            return
        next = node.next
        prev = node.prev
        
        node.prev.next = next
        node.next.prev = prev
        
        
        


def solution(number, k):
    digits = [ int(i) for i in number ]
    linkedList = LinkedList()
    
    for digit in digits:
        linkedList.append(Node(digit))
        
    current = linkedList.head
    while current:
        if k > 0 and current.prev and current.prev.data < current.data:
            linkedList.pop(current.prev)
            k -= 1
        else:
            current = current.next
            
    for i in range(0, k):
        linkedList.pop(linkedList.tail)
    
    
    current = linkedList.head
    sum_str = ""
    while current:
        sum_str += str(current.data)
        current = current.next
        
    return sum_str
    

# 링크드리스트 구현

# append, pop을 O(1)에 할 수 있어야 함
# hea 필요
# append: tail 필요, tail에다가 붙이면 O(1)
# pop: prev와 tail 연결