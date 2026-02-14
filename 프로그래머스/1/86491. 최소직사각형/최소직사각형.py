def solution(sizes):
    max_width = 0
    max_height = 0
    for i in range(0, len(sizes)):
        width, height = sizes[i]
        if width > height:
            max_width = max(width, max_width)
            max_height = max(height, max_height)
        else:
            max_width = max(height, max_width)
            max_height = max(width, max_height)
    return max_width * max_height
            
    
    
    

# 완전탐색: 2 * 2 * 2 *... 
# O(2 ** n) (1 <= n <= 10_000)

# 최소로 만드는 방법:
# 모든 도형의 가로를 길게, 세로를 짧게
# max_a * max_b
# 이 때 a[i], b[i]를 스위칭한다고 해보자.
# 1. max_b를 스위칭하는 경우: 무조건 커짐
# 2. max_a를 스위칭하는 경우: 무조건 커짐
# 3. 아닌 경우: 동일 값 유지

# max_a >= a[i] >= min_a, max_a > max_b >= b[i] >= min_b
# max_a == a[i] 인 경우 



