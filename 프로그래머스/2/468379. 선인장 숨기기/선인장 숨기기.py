import heapq
from math import inf
from collections import deque

# monotone deque
# 현재 슬라이딩 윈도우에 포함되어 있는 값만 가지고 있다.

# 제거되는 경우
#   1. 자리 이동으로 인해 슬라이딩 윈도우에 해당 값이 더이상 포함되지 않는 경우
#   2. 더 작은 값이 들어오는 경우(나중에 들어오는 값이기 때문에, 앞으로 진행되는 슬라이딩 윈도우에서는 항상 #      더 작은 값만 후보로 사용해도 된다.)

# 추가되는 경우
#   1. 해당 슬라이딩 윈도우로 진입할 때 




class TreeSet:
    def __init__(self):
        self.queue = deque()
        
    def add(self, num):
        
        while len(self.queue) > 0 and self.queue[len(self.queue) - 1] > num:
            self.queue.pop()
        
        self.queue.append(num)
    
    def remove(self, num):
        if len(self.queue) > 0 and self.queue[0] == num:
            self.queue.popleft()
        
    
    def min(self):
        if len(self.queue) == 0:
            return None
        
        return self.queue[0]
    
    def reset(self):
        self.queue = deque()
        
    def size(self):
        return len(self.queue)
        
        
        
    
    

def solution(m, n, h, w, drops):
    table = { (x, y): index + 1 for index, (x, y) in enumerate(drops) }
    matrix = [[ -inf for j in range(n) ] for i in range(m) ]
        
    heap = TreeSet()
    
    for i in range(m):
        for j in range(n - w + 1):
            if j == 0:
                heap.reset()
                for y in range(j, j + w):
                    if (i, y) in table:
                        heap.add(table[i, y])
            else:
                if (i, j - 1) in table:
                    heap.remove(table[i, j - 1])
                if (i, j + w - 1) in table:
                    heap.add(table[i, j + w - 1])
            matrix[i][j] = heap.min()    
    heap.reset()
    
    max_value = -inf
    max_position = [0, 0]
    
    for j in range(n - w + 1):
        for i in range(m - h + 1):
            if i == 0:
                heap.reset()
                for x in range(i, i + h):
                    if matrix[x][j] is not None:
                        heap.add(matrix[x][j])
            else:
                if matrix[i - 1][j] is not None:
                    heap.remove(matrix[i - 1][j])
                if matrix[i + h - 1][j] is not None:
                    heap.add(matrix[i + h - 1][j])
            
            
            candidate = inf if heap.min() is None else heap.min()
            if candidate > max_value:
                max_value = candidate
                max_position = [i, j]
            elif candidate == max_value:
                if i < max_position[0]:
                    max_position = [i, j]
                elif i == max_position[0] and j < max_position[1]:
                    max_position = [i, j]
            
    return max_position
                    
#             if j == 0:
#                 heap.reset()
#                 for x in range(i, i + h):
#                     for y in range(j, j + w):
#                         if matrix[x][y] > 0:
#                             heap.add(matrix[x][y])
#             else:
#                 new_y = j + w - 1
#                 old_y = j - 1
                
#                 for old_x in range(i, i + h):
#                     if matrix[old_x][old_y] > 0:
#                         heap.remove(matrix[old_x][old_y])
                    
#                 for new_x in range(i, i + h):
#                     if matrix[new_x][new_y] > 0:
#                         heap.add(matrix[new_x][new_y])
            
#             if heap.size() == 0:
#                 return [i, j]
            
#             if heap.min() > max_value:
#                 max_value = heap.min()
#                 max_point = [i, j]
                
    # return max_point
            
        
                
                
                
                
                

# dict point to num => 점: 숫자 만들기

# 슬라이딩 윈도우
# h * w 공간에서, 옆으로 밀면서 점 빼고, 점 쌓고
# 점 저장 방식: dictionary, (y 좌표): (x, y) 리스트

# 
# 1. y - 1에 있는 좌표 제거, y + w에 좌표 추가
#    좌표 제거시 maxheap에 있는 번호도 같이 제거
#    좌표 추가시 dictionary에도 추가하고, maxheap에도 번호 추가
# 2. maxheap에 현재 저장된 최댓값 반환

# 시간복잡도: O(m * n * log(m))

# 점 처음으로 없어지는 공간이 있는 경우 => 반환

# 없는 경우 => max 값 반환

# 시간복잡도: 완전 탐색 한번 => m * n * log(m * n)
# 공간복잡도: O(m * n)
# 500_000 => 4_000_000 = 4mb

# h * w 배열이 들어갈 공간이 있는지 탐색 (m * n) (막히는 곳 있으면 그대로 다음 곳부터 탐색)
# 들어갈 공간이 없으면, 
