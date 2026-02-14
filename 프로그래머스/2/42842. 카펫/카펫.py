def solution(brown, yellow):
    size = brown + yellow
    for a in range(3, size // 2 + 1):
        if size % a == 0:
            b = size / a
            if (a - 2) * (b - 2) == yellow:
                return [ b, a ]
        
    
    return [ -1, -1 ]
    

# brown + yellow = n인 ab 중에 (a - 2) * (b - 2) = yellow인 것 찾기
# 48
# 48 * 1
# 24 * 2
# 12 * 4
# 6 * 8일 때 yellow 개수: (6 - 2) * (8 - 2) = 4 * 6 = 24

# 시간복잡도: O(n + m)
# 공간복잡도: O(1)


# 24
# = 24 * 1 => brown의 개수: (26 * 3) - yellow
# = 12 * 2
# = 8 * 3
# = 6 * 4 => brown의 개수: (8 * 6) - yellow

# 2 * 1일 때 brown의 개수: (4 * 3) - yellow

