class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self, size):
        self.size = size
        self.table = {}
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head == None:
            self.head = node

        if self.tail == None:
            self.tail = node
        else:
            prev, next = self.tail, node
            prev.next, next.prev = next, prev
            self.tail = node

    def remove(self, node):
        if self.head == node:
            self.head = node.next

        if self.tail == node:
            self.tail = node.prev

        prev, next = node.prev, node.next
        if prev != None:
            prev.next = next
        if next != None:
            next.prev = prev

    def get(self, data):
        #  데이터가 테이블에 있을 경우, 제거하고 끝에다가 요소 추가
        if data in self.table:
            node = self.table[data]
            self.remove(node)
            self.table.pop(data)

        # 노드 새로 만들어서 linked list의 끝에다가 요소 추가 / table에 추가
        node = Node(data)
        self.table[data] = node
        self.append(node)

        # 캐시 사이즈를 넘어가는 경우 head 요소 제거하기
        if len(self.table) > self.size:
            self.table.pop(self.head.data)
            self.remove(self.head)

    def print(self):
        current = self.head

        while current != None:
            print(current.data, end="")
            current = current.next
        print()


def solution(cache_size, requests):
    linked_list = LinkedList(cache_size)
    for request in requests:
        if request == "!":
            linked_list.print()
        else:
            linked_list.get(request)


if __name__ == "__main__":
    i = 1
    while True:
        line = input()
        if line == "0":
            break

        tokens = line.split()
        cache_size, requests = int(tokens[0]), tokens[1]
        print(f"Simulation {i}")
        solution(cache_size, requests)

        i += 1


# linked list만으로 구현시: 캐시에 있는지 확인하기 위해 O(n) 시간 걸림
# hash table 같이 사용시: 캐시 확인에 O(1) 시간 걸림

# LinkedList
#   appendright(): linked list의 끝에다가 요소 추가
#   get():
#     1. 데이터가 테이블에 있을 경우, 제거하고 끝에다가 요소 추가
#        데이터가 테이블에 없을 경우, 노드 새로 만들어서 linked list의 끝에다가 요소 추가 /
#     3. 캐시 사이즈를 넘어가는 경우 head 요소 제거하기 / table에서도 제거하기


# ABCDE AF
# BCDEA
# CDEAF


# WXWYZ
# XWY
# WYZ + YZWYX
# WZY
# WYZ
# YZW
# ZWY
# WYX
