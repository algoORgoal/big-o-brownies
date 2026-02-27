from collections import deque

def solution(rectangles, characterX, characterY, itemX, itemY):
    matrix = [ [ 0 for j in range(0, 200) ] for i in range(0, 200) ]
    
    for rectangle in rectangles:
        x1, y1, x2, y2 = [ number * 2 for number in rectangle]
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                matrix[x][y] = 1
            
    root = (2 * characterX, 2 * characterY,)
    target = (2 * itemX, 2 * itemY,)

    return bfs(matrix, root, target, set()) / 2
            
                
    
def bfs(matrix, root, target, visited):
    queue = deque([ (root, 0,) ])
    visited.add(root)
    
    while len(queue) > 0:
        current, distance = queue.pop()
        
        x, y = current
        
        if target == current:
            return distance
            
        corners = [ (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1 ), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1) ]
        
        isAllFilled = all([ matrix[corner_x][corner_y] == 1 for corner_x, corner_y in corners ])
        
        if isAllFilled:    
            continue
            
        next_nodes = [ (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1 ) ]

        for next_node in next_nodes:
            if next_node in visited:
                continue
                
            next_x, next_y = next_node
            if matrix[next_x][next_y] == 0:
                continue
                
            visited.add(next_node)
            queue.appendleft((next_node, distance + 1,))

            
    return 10000
            
        
        
    
    
    
#     min_table_x = {}
#     max_table_x = {}
#     min_table_y = {}
#     max_table_y = {}
    
#     for rectangle in rectangles:
#         x1, y1, x2, y2 = rectangle
#         # 1. x1 그대로, y1 => y2
#         # 2. x2 그대로, y1 => y2
#         for y in range(y1, y2 + 1):
#             if y not in min_table_y:
#                 min_table_y[y] = x1
#                 max_table_y[y] = x2
                
#             min_table_y[y] = min(min_table_y[y], x1)
#             max_table_y[y] = max(min_table_y[y], x2)
            
#         for x in range(x1, x2 + 1):
#             if x not in min_table_x:
#                 min_table_x[x] = y1
#                 max_table_x[x] = y2
                
#             min_table_x[x] = min(min_table_x[x], y1)
#             max_table_x[x] = max(min_table_x[x], y2)
            
#     valid_positions = set()
    
#     for x in min_table_x:
#         y = min_table_x[x]
#         valid_positions.add((x, y,))
    
#     for x in min_table_x:
#         y = max_table_x[x]
#         valid_positions.add((x, y,))
        
#     for y in min_table_y:
#         x = min_table_y[y]
#         valid_positions.add((x, y,))
        
#     for y in max_table_y:
#         x = max_table_y[y]
#         valid_positions.add((x, y,))
        
#     print((4,5,) in valid_positions)
        
        
#     print(valid_positions)
        
        # 3. y1 그대로, x1 => x2
        # 4. y2 그대로, x1 => x2
        
    
    
    answer = 0
    return answer

# 해결책 1
# 각 x좌표에서 최소값/최대값, 각 y좌표에서 최소값/최대값 구함
# 모여서 한 다각형을 이루므로 이 좌표들만 이동할 수 있는 유효한 값
# bfs로 다음 노드 이동할 때 해당 좌표들로만 이동 가능
# 문제: 최대값 최소값이 아닌 중간 값중에도 유효한 값이 있는데 이를 유효하지 않은 값으로 간주.

# 해결책 2
# 주어지는 다각형 영역을 1로 표시
# 좌표계 확장: 2배로 확장.(좌표계 확장)
# bfs 탐색을 진행하되, 
# 다각형 영역에 포함되는 부분만 탐색, 
# 그리고 주변(상하좌우) 좌표가 모두 다각형에 포함되는 경우 버림
# 거리 = 확장된 좌표계에서의 거리 / 2




# 최대 사이즈 100 * 100 = 10000
# 1. 지형 테두리를 모두 칠한다
# 2. 가장자리에서 어느 방향으로 가야 할까?
#    