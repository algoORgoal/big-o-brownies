import heapq

# 1. 다익스트라 알고리즘을 사용해야 한다.
# (weighted graph로 표현 가능)

# 2. 현재 방향 기억하고 있기.
#    다음에 갈 경로의 방향이 다르다 => 500 + 100, 같다 => 100

# 상태: (cost, 좌표, 방향)
# 출발 상태: (0, (0, 0), -1)
# -1에서는 어디든 가도 100원
# 목적 좌표 (n - 1, n - 1)

dx = [ 0, 0, -1, 1]
dy = [ 1, -1, 0, 0]


def solution(board):
    n = len(board)
    source = (0, 0)
    destination = (n - 1, n - 1)
    
    return dijkstra(board, source, destination, n)

def dijkstra(board, source, destination, n):
    queue = []
    
    heapq.heappush(queue, (0, source, 4))
    
    visited = [ [ [ False for k in range(5) ] for j in range(n) ] for i in range(n) ]
    
    while len(queue) > 0:
        cost, position, direction = heapq.heappop(queue)
        
        x, y = position
        
        if (x, y) == destination:
            return cost
        
        if visited[x][y][direction] == True:
            continue
        
        visited[x][y][direction] = True            
        candidates = []
        
        for next_direction in range(len(dx)):
            offset_x = dx[next_direction]
            offset_y = dy[next_direction]
            
            next_x = x + offset_x
            next_y = y + offset_y
            
            
            # within range
            if next_x < 0 or next_x >= n:
                continue
                
            if next_y < 0 or next_y >= n:
                continue
            
            # is not a block
            if board[next_x][next_y] == 1:
                continue
            
            next_position = (next_x, next_y)
            
            if direction == 4 or direction == next_direction:
                weight = 100
                next_cost = cost + weight
                
                
                heapq.heappush(queue, (next_cost, next_position, next_direction))
                
                continue
            
            # direction != next_direction
            weight = 500 + 100
            next_cost = cost + weight
            
            
                    
            heapq.heappush(queue, (next_cost, next_position, next_direction))
        
        
                
        
        
        
        
        