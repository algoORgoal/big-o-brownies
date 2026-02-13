import heapq
import sys
from math import inf


min_queue = []
max_queue = []
deletion_history = set()

def heappush(value, id):
    heapq.heappush(max_queue, [-value, id])
    heapq.heappush(min_queue, [value, id])
    

def heappop_max():    
    while len(max_queue) > 0:
        inverted_value, id = heapq.heappop(max_queue)
        if id not in deletion_history:
            deletion_history.add(id)
            return -inverted_value
    return None
        
def heappop_min():    
    while len(min_queue) > 0:
        value, id = heapq.heappop(min_queue)
        if id not in deletion_history:
            deletion_history.add(id)
            return value
    return None


    
    


def solution(operations):    
    for index, operation in enumerate(operations):
        command, numStr = operation.split(' ')
        num = int(numStr)
        if command == "I":
            heappush(num, index)
        elif command == "D" and num == 1 and len(max_queue) > 0:
            heappop_max()
        elif command == "D" and num == -1 and len(min_queue) > 0:
            heappop_min()
    
    max_value = heappop_max() or 0
    min_value = heappop_min() or max_value or 0
    return [ max_value, min_value ]
    
    
    

# min_queue와 max_queue를 별도로 운영
# min_queue에서 삭제된 요소를 max_queue에서 접근하지 않도록 id 같이 저장
# min_queue에서 삭제된 요소를 max_queue에서 접근하지 않도록 id 같이 저장

# 시간복잡도: O(nlogn)
# 공간복잡도: O(n)
        
    