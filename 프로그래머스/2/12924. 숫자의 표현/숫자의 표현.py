def solution(target):
    ends = set()
    for k in range(1, target + 1):
        end = (2 * target + k * (k - 1)) / (2 * k)
        if int(end) == end:
            ends.add(end)

    return len(ends)



# 연속된 자연수들로 n을 표현하는 방법의 수 찾기
# prefix sum 유지하고, range(i, j)에 대해 찾기 => 시간복잡도 O(n ** 2) = 10 ** 8
# 공간복잡도 O(n)
# 100_000_000 => 가능

# prefix sum 유지할 필요 없음
# range(i, j)의 구간합 => 
# i == j => i
# i < j => j(j + 1)/ 2 - (i - 1)i / 2

# 10_000 * 10_000 = 10 ** 8
# 100_000_000

# 시간초과 왜 내냐 ㅋㅋ
# 15 = 15 / 7 8 / 4 5 6 /  / 1 2 3 4 5
# O(n) solution
# 길이 1, 2, ..., n인 subarray로 합 만들 수 있냐?
# 길이 2 => end = start + 1
# (start + 1)(start + 2) - (start - 1)start / 2 = 15
# start = 7 => (8 * 9 - 6 * 7) / 2 = (72 - 42) / 2 = 15
# 길이 k => end = start + m (k = m - 1)
# (start + m)(start + m + 1) - (start - 1)start = target
# end(end + 1) - (end - k)(end - k + 1) = target
# end = (2 * target + k * (k - 1)) / (2 * k)

