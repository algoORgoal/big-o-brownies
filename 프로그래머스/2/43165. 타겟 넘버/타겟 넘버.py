from itertools import product


def solution(numbers, target):
    return dfs(numbers, 0, 0, target)

def dfs(numbers, num_count, total, target):
    if num_count == len(numbers):
        if total == target:
            return 1
        else:
            return 0
        
    current = numbers[num_count]
    
    return dfs(numbers, num_count + 1, total + current, target) + dfs(numbers, num_count + 1, total - current, target)
    
    
        


# +, -로 모든 상태를 만들 경우 2 ** 20
# 시간복잡도 2 ** n
# 공간복잡도 2 ** n