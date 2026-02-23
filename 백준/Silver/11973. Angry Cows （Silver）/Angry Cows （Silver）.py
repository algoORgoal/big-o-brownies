def solution(n: int, k: int, arr: list[int]):
    sorted_arr = sorted(arr)

    start = 0
    end = 1_000_000_000

    while start < end:
        middle = (start + end) // 2

        current_range = [sorted_arr[0], sorted_arr[0] + 2 * middle]
        count = 1
        for bale in sorted_arr:
            if bale > current_range[1]:
                current_range = [bale, bale + 2 * middle]
                count += 1

        # k개 안에 제거 가능 => [start, middle]만 보면 됌 (middle + 1부터 모두 가능)
        # k개 안에 제거 불가능 => [middle + 1, end]만 보면 됌 (middle까지 모두 불가능)
        if count <= k:
            end = middle
        else:
            start = middle + 1

    return start


if __name__ == "__main__":
    n, k = [int(string) for string in input().split(' ')]
    arr = [int(input()) for i in range(0, n)]
    answer = solution(n, k, arr)
    print(answer)

# 1. sort the position of hay bales in ascending order
# 2. latest_shoot = [ arr[0], arr[0] + 2 * k ], count = 1
# 3. how to count the minimum number of cows to remove all hay bales
#    for i in arr:
#      if i not in latest_shoot:
#        latest_shoot = [ i, 2 + 2 * k ]
#        count += 1

#

# time complexity: O(nlogm) (n <= 50_000, m <= 1_000_000_000)
# space complexity: O(n)
