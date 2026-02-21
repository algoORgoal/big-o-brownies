from math import log2

# def integer_partition(n, m):
#     if n < m:
#         return 0
#     if n == m:
#         return 1
#     if m == 1:
#         return 1
#     return integer_partition(n - 1, m - 1) + integer_partition(n - m, m)


def solution(n, times):
    start = 1
    end = 1_000_000_000 * 1_000_000_000 # 1_000_000_000 걸리는 심사관 1명이 1_000_000_000 사람 심사
    
    while start < end:
        middle = (start + end) // 2
        
        capacity_count = 0
        for time in times:
            capacity_count += (middle // time)
            
        if capacity_count >= n:
            end = middle
        else:
            start = middle + 1
        
    
    return start

# 1 <= m <= 100_000, m = len(times)
# 1 <= n <= 1_000_000_000 (사람 수)
# 심사 시간 t <= 1_000_000_000 (times[k])

# 모든 경우의 수: n명의 사람을 m개의 그룹으로 분할
# p(n, m) = p(n - 1, m - 1), p(n - m, m)
# n < m => 1
# n == m => 1
# m == 1 => 1
# 메모이제이션시 O(m * n) (1_000_000_000 * 100_000) => 시간초과


# n분만에 심사 가능한 사람의 수 구하는데 시간: O(m)
# 탐색 시간 O(log(t * n)) log(t * n) <= 60
# O(log(t * n) * m) => 가능 m <= 100_000

# n분만에 k명 심사 가능 => [ start, n ] 탐색
# n분만에 k명 심사 불가능 => [ n + 1, end ] 탐색
# 최솟값 k를 구함









