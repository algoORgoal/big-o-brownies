

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, node):
        if (not self.head) and (not self.tail) :
            self.head = node
            self.tail = node
            return
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
    
    def pop(self, node):
        if self.head is node and self.tail is node:
            self.head = None
            self.tail = None
            return

        if self.head is node:
            self.head = node.next
            self.head.prev = None
            return
        
        
        if self.tail is node:
            self.tail = node.prev
            self.tail.next = None
            return
        
        
        next = node.next
        node.prev.next = next
        
        prev = node.prev
        node.next.prev = prev

            
        
        

def solution(number, k):
    arr = [ int(i) for i in number ]
    linkedList = LinkedList()
    for i in arr:
        linkedList.append(Node(i))
        
    
    node = linkedList.head
    while node and k > 0:
        if node.prev and node.prev.data < node.data:
            linkedList.pop(node.prev)
            k -= 1
        else:
            node = node.next
    
    for i in range(0, k):
        linkedList.pop(linkedList.tail)
        
            
    
    node = linkedList.head
    sum = ""
    
    while node:
        sum += str(node.data)
        node = node.next
    
    return sum


# 4 17 7 25 28 4 1
# 1 제거 

# 47 7 25 28 4 1
# 4 제거

# 7 7 25 28 4 1
# 2 제거

# 7 7 58 4 1
# 2 제거

# 7 7 58 4 1


# 1 9 2 4
# 1 제거
# 9 2 4
# 2 제거
# 9 4

# 현재 자릿수가 앞 자릿수보다 클 때까지
#  앞 자릿수 제거
# 나머지: 뒷자릿수 제거
# 시간복잡도: O(n)
# 공간복잡도: O(n)







# 4 1 7 7 2 5 2 8 4 1
# x x     x   x

# 큰 자릿수를 먼저 제거해야함
# 더 큰 자릿수를 만들기 위해 제거해야하는 숫자의 개수가 k개 이하여야 한다.

