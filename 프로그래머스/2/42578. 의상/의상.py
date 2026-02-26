def solution(clothes):
    table = {}
    for name, category in clothes:
        if category not in table:
            table[category] = 0
        table[category] += 1
    count = 1
    for category in table:
        count *= table[category] + 1
        
    return count - 1
        
        
    
    


    
    


# headgear: 2 + 안입음 1
# eyewear: 1 + 안입음 1
# 3 * 2 - (모두 안입음) = 5

