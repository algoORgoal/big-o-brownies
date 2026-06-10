def solution(n, l, r):
    l -= 1
    r -= 1
    
    return recursive(n, r, 1) - recursive(n, l - 1, 1)

def recursive(n, count, multiple):
    if count < 0:
        return 0
    
    if n < 0:
        return 0
    
    
    rest = (count % 5) + 1
    next = count // 5 - 1
    
    left = 0

    for i in range(0, rest):
        rest_index = count - i
        
        is_zero = False
        
        for j in range(n, 0, -1):
            amount = 5 ** (j - 1)
            start, end = amount * 2, amount * 3
            
            if start <= (rest_index % (5 **j)) < end:
                is_zero = True
                break
        
        if is_zero == False:
            left += 1
            

            
        
    
        
    return (left * multiple) + recursive(n - 1, next, multiple * 4)

# 1번째 유사 칸토어 비트열: 1
# 2번째 유사 칸토어 비트열: 11011
# 3번째 유사 칸토어 비트열: 110[11 11011 00000 11]011 11011
# 3번째에서 3 ~ 16번째까지 1의 개수
# 2번째에서, (3 // 5) ~ (16 // 5)까지 1의 개수 = 0 ~ 3까지의 1의 개수
# 1번째에서, (0 // 5) ~ (0 // 3)까지의 1의 개수 = 
# 

# = (n = 2에서, 1에서 17번째 까지 1의 개수) - (n = 2에서, 1에서 4번째까지 1의 개수)

# n = 1 길이 5 => between 2 and 2
# n = 2 길이 25 => between 10 and 14
# n = 3 길이 125 => between 50 and 74

# amount = 5 ** (n - 1)
# amount * 2 ~ amount * 3


