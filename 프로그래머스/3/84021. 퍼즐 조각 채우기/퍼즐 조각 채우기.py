def solution(game_board, table):
    inverted_game_board = [ [ game_board[i][j] ^ 1 for j in range(0, len(game_board[i])) ] for i in range(0, len(game_board)) ]
    
    shape_points = get_shape_points(table)
    
    blocks = extract_blocks_from(inverted_game_board)
    
    count = 0
    
    for block in blocks:
        points = convert_to_points(block)
        if points in shape_points and shape_points[points] > 0:
            rotated_blocks = get_shape(block)
            
            rotated_points = set([ convert_to_points(block) for block in rotated_blocks ])

            for points in rotated_points:
                shape_points[points] -= 1
            count += len(points)
    
    
    
    return count


def extract_blocks_from(table):
    visited = set()
    
    # O(n) n = i * j, 1 <= i,j <= 50
    blocks = []
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            point = i, j
            if point not in visited and table[i][j] == 1:
                visited.add(point)
                points = dfs(point, table, visited)
                block = convert_to_block(points)
                blocks.append(block)
                
    return blocks

def get_shape_points(table):
    blocks = extract_blocks_from(table)
                
    shape_points = {}
    for block in blocks:
        shape = get_shape(block)
        
        rotated_points = set([ convert_to_points(block) for block in shape ])
        for points in rotated_points:
            if points not in shape_points:
                shape_points[points] = 0
            shape_points[points] += 1
            
    return shape_points

def dfs(current, table, visited):
    height, width = len(table), len(table[0])
    
    x, y = current
    candidates = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
    
    points = [ current ]
    
    for candidate in candidates:
        candidate_x, candidate_y = candidate
        if 0 <= candidate_x < height and 0 <= candidate_y < width and candidate not in visited and table[candidate_x][candidate_y] == 1:
            visited.add(candidate)
            points += dfs(candidate, table, visited)
            
    return points

def convert_to_block(points):
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    block = [ [ 0 for j in range(min_y, max_y + 1) ] for i in range(min_x, max_x + 1)]
    
    for x, y in convert_to_absolute_points(points):
        block[x][y] = 1
    return block

def convert_to_absolute_points(points):
    min_x = min([ point[0] for point in points ])
    min_y = min([ point[1] for point in points ])
    return [ (point_x - min_x, point_y - min_y) for point_x, point_y in points]

def convert_to_points(block):
    points = []
    for i in range(0, len(block)):
        for j in range(0, len(block[i])):
            if block[i][j] == 1:
                point = i, j
                points.append(point)

    return tuple(sorted(points))

def get_shape(block1):
    block2 = rotate(block1)
    block3 = rotate(block2)
    block4 = rotate(block3)
    
    return block1, block2, block3, block4

def rotate(block):
    height = len(block)
    width = len(block[0])
    
    rotated_block = [ [ 0 for j in range(0, height) ]  for i in range(0, width) ]
    for i in range(0, height):
        for j in range(0, width):
            rotated_block[j][height - 1 - i] = block[i][j]
            
    return rotated_block


    
    
# block: n * m matrix
# shape: 회전시켜서 만들 수 있는 한 블럭이 만들 수 있는 가능한 조합. n * m matrix
# 
            



# 퍼즐 블락을 어떻게 데이터 모델링 할 것인가?
# 회전을 어떻게 표현할 것인가?

