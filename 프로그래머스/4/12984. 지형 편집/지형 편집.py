from math import inf

def solution(land, P, Q):
    heights = sorted([ tower for towers in land for tower in towers ])
    
    lowest_height = heights[0]
    

    
    lowest_height_cost = 0
    
    for towers in land:
        for tower in towers:
            lowest_height_cost += Q * (tower - lowest_height)
            
    plus_cost = 0
    minus_cost = lowest_height_cost
    
    min_cost = plus_cost + minus_cost
    
    for i, height in enumerate(heights):
        if i == 0:
            continue
            
        diff = heights[i] - heights[i - 1]
        
        plus_cost = plus_cost + P * diff * i # 쌓는데 드는 cost
        minus_cost = minus_cost - (Q * diff * (len(heights) - i)) # 제거하는데 드는 cost
        min_cost = min(min_cost, plus_cost + minus_cost)
    
    return min_cost
            
#     sorted_heights = height_frequency
    
#     print(height_frequency)
#     return 0

# 최대 300 * 300 = 900_000개의 다른 층 나온다.
# 답은 900_000개의 다른 층 중 하나인가?


# 제거할 경우 코스트, 추가할 경우 코스트
# 각 층별로 코스트 계산하는 경우: 

# 1. 각 level별로 블럭이 몇개가 있는지 계산
# 2. 각 레벨별로 부족한 블럭의 개수, 존재하는 블럭의 개수 계산
# 3. prefix, suffix 계산
# 4. prefix 중에 최소값, suffix 합 중에 최소값 계산
# 5. 최소값의 cost 계산
# 6. min()

# 시간복잡도: O(m * n * n) (m <= 10억)

# 기둥이 10 10 20 20이 있을 때
# P = 10, Q = 20
# 20 20 으로 맞추기: (10 + 10) * 10 = 200
# 10 10 으로 맞추기: (20 + 20) * 10 = 400
# 15 15으로 맞추기: (10 + 10) * 5 = 100, (20 + 20) * 5 = 200
# a + b = n ** 2
# a * p * diff
# b * q * diff

# 900_000
# ... > 정답 - 1인 경우 드는 cost > 정답인 경우 드는 cost < 정답 + 1인 경우 드는 cost < 정답 + 2인 경우 드는 c ost < ...
# 

# a를 제거하는데 드는 코스트 vs b를 추가하는데 드는 코스트
# a + b = n ** 2
# a를 제거하는데 드는 코스트가 더 작으면 => a 제거
# b를 제거하는데 드는 코스트가 더 크면 => b 추가

# 8_100_000_000

# 90_000

# 뾰족점이 되는 이유
# 가장 코스트가 적게 드는 높이가 h라고 하자.
# i번째 타워의 높이가 x_i일 때, cost
# c(x_i) = (x_i - h) * P if x_i > h otherwise (h - x_i) * Q
# c(x_i)는 볼록함수
# c(x) = c(x_1) + c(x_2) + ... + c(x_n)
# 볼록함수의 합도 볼록함수
# 따라서 삼진탐색이 가능하다.

# 삼진탐색이 안 되는 이유
# 탑을 만드는데 드는 코스트는 300 * 300 * 10억까지 도달할 수 있다.

# 존재하는 층만 탐색하면 된다.
# 지형이 3층하고 5층밖에 없다고 가정하자.
# 3층하고 5층 사이 x층으로 맞추는데 드는 cost
# 낮은 층이 x, 높은 층이 y
# C(x) = P * (x - 3) + Q * (5 - x) = (P - Q)x - 3P + 5Q
# 1차 함수 => 직선이므로, 3 <= x <= 5에서 최소값을 가지는 경우는 x == 3 or x == 5 밖에 없다.

# 각 층 사이는 탐색할 필요가 없으므로, 존재하는 층에 드는 cost만 탐색한다.
# 모든 탑을 각 층별로 탐색하는 경우:
# O(n * n * n * n) (n * n개의 탑, 높이가 n * n개 존재 가능) => 시간초과
# 


# 높이 순으로 정렬
# 1. 처음에 가장 낮은 층으로 평탄화하고, 코스트 계산하기
# 2. 다음 층에 대한 코스트 계산하는 법
#    차이 = 다음 층 높이 - 이전 층 높이
#    (이전층 높이였던 것) * P * (차이) 계산하기
#    (다음층 높이 이상이였던 것) * Q * (차이) 계산하기


