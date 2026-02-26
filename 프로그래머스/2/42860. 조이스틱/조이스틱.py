from math import inf

def calculate_vertical_distance(char):
    start = ord('A')
    end = ord('Z')
    target = ord(char)

    return min(abs(target - start), abs(end - target + 1))

def solution(name):
    vertical_distance = 0
    for char in name:
        vertical_distance += calculate_vertical_distance(char)

    positions = []
    for i in range(0, len(name)):
        char = name[i]
        if char != "A":
            positions.append(i)
            
    return vertical_distance + calculate_horizontal_distance(0, positions, len(name))

def circular_distance(a, b, n):
    return min(abs(a - b), n - abs(a - b))
            
def calculate_horizontal_distance(current, positions, n):
    if len(positions) == 0:
        return 0
    first = positions[0]
    last = positions[len(positions) - 1]
    
    forward_distance = circular_distance(current, first, n)
    a = forward_distance + calculate_horizontal_distance(first, positions[1:], n)
    
    if current < last:
        backward_distance = circular_distance(current, last, n)
        b = backward_distance + calculate_horizontal_distance(last, positions[0:-1], n)
    else:
        backward_distance = circular_distance(current, last, n)
        b = backward_distance + calculate_horizontal_distance(last, positions[0:-1], n)
    return min(a, b)
    
    

# 1. positions[i]를 기준으로 회전하여, positions[i + 1]에 도착 (정방향 / 역방향) (len(positions) > 2)
# 2. 처음부터 끝까지 정방향
# 3. 처음부터 역방향


    
        
        
        
        

    
        
    
    
    
    # 역방향 우선
    
    return count


# min(처음것 조작 + 역방향 or 정방향)
# 각 알파벳 도달: Z부터 이동 + 1 vs A부터 이동

# 반례 AZAAAAZ
# 다시 돌아오는 왕복식으로 하는 게 더 빠름
# 정방향 / 역방향으로 나눠서 항상 가장 가까운 놈에 도달하는 알고리즘 구성


