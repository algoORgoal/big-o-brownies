from itertools import product


def solution(numbers, target):
    cases = [ [ number, -number ] for number in numbers ]
    
    
    count = 0
    for combination in product(*cases):
        current = 0
        for num in combination:
            current += num
        if current == target:
            count += 1
    return count
        


# +, -로 모든 상태를 만들 경우 2 ** 20
# 2 ** n
# ㄴㅇㄹ