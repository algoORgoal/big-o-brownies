from math import inf
from collections import deque

def vertical_distance(char):
    start = ord('A')
    end = ord('Z')
    target = ord(char)

    return min(abs(target - start), abs(end - target + 1))

def calculate_directional_distances(n, current, next):
    normal_distance = next - current
    reversed_distance = (n - next) + current + 1
    return [normal_distance, reversed_distance]



def solution(name):
    count = 0
    for char in name:
        count += vertical_distance(char)

        
    
    positions = deque()
    for i in range(0, len(name)):
        char = name[i]
        if char != "A":
            positions.append(i)
            
    if len(positions) == 0:
        return count
    
    if len(positions) == 1:
        return count + min(calculate_directional_distances(len(name) - 1, 0, positions[0]))
    
    distance = inf
    
    normal = positions[len(positions) - 1]
    opposite = len(name) - positions[0]
    
    
    distance = min(distance, normal)
    distance = min(distance, opposite)
    
    for i in range(0, len(positions) - 1):
        reversed1 = 2 * positions[i] + len(name) - positions[i + 1]
        reversed2 = (len(name) - positions[i + 1]) * 2 + positions[i]
        distance = min(distance, reversed1)
        distance = min(distance, reversed2)
        
    
        
    print(distance, count)
            
    return distance + count
    

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


