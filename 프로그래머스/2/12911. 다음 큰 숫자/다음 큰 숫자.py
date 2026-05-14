from itertools import combinations
from bisect import bisect_left
from math import inf

def solution(n):
    one_count = count_ones(n)
    current = n + 1
    while count_ones(current) != one_count:
        current += 1
    
    return current
    

def count_ones(n):
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
    return count





# 1. n보다 큰 자연수
# 2. 2진수로 변환했을 때 1의 개수가 같다.
# 3. 만족하는 수 중 가장 작은 수


# 1_000_000 < 2 ** 20
# 20Cr이 최대인 경우 => r = 10인 경우
# 20Cr <= 20C10 = 184756
# 정렬하기 => nlogn
# 이진탐색 => logn
# 그 다음 인덱스에 있는 수 구하기

# 시간복잡도: O(nlogn) (n <= 184756)


    
