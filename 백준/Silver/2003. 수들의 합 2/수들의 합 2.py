def solution(n, m, arr):
    start = 0
    end = 0
    current = arr[start]
    count = 0

    while start < len(arr) and end < len(arr):
        if current > m:
            current -= arr[start]
            start += 1
        elif current < m:
            end += 1
            if end < len(arr):
                current += arr[end]
        else:
            current -= arr[start]
            start += 1
            count += 1
    return count


if __name__ == "__main__":
    n, m = [int(string) for string in input().split(' ')]
    arr = [int(string) for string in input().split(' ')]
    answer = solution(n, m, arr)
    print(answer)

# 완전탐색: O(n ^ 2) (n <= 10 ** 4)
# 10 ** 8 = 100_000_000 => 시간제한 0.5초이므로 불가능

# 요소들이 전부 자연수이므로,
# [start, end] < [start, end + 1]
# [start + 1, end] < [start, end]
# 슬라이딩 윈도우 사용 가능
# 시간복잡도 O(n)
# 공간복잡도 O(1)
