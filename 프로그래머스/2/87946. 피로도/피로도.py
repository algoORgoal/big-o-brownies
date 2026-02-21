from itertools import permutations

def factorial(k):
    if k == 0:
        return 1
    if k == 1:
        return 1
    return k * factorial(k - 1)

def solution(k, dungeons):
    max_visit_count = 0
    for i in range(0, len(dungeons) + 1):
        for combo in permutations(dungeons[0:i]):
            stamina = k
            visit_count = 0
            for required, cost in combo:
                if stamina >= required:
                    stamina -= cost
                    visit_count += 1
                else:
                    break
            max_visit_count = max(visit_count, max_visit_count)
    return max_visit_count
            

            
    

    
    answer = 0
    return answer

# 모든 경우의 수 O(mP1 + ... + mPm) = (m <= 8)
# 각 경우의 수 별로 클리어 가능한지 확인
# 클리어 가능한 것 중 던전의 개수 최댓값 반환


