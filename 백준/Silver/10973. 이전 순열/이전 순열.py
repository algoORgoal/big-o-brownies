
def solution(n, arr):
    i = len(arr) - 1

    while i > 0:
        if arr[i - 1] > arr[i]:
            j = n - 1
            while j >= i:
                if arr[i - 1] > arr[j]:
                    arr[i - 1], arr[j] = arr[j], arr[i - 1]
                    break
                j -= 1
            start_part = arr[:i]
            # arr[i] < arr[i + 1] < ... < arr[n - 1]
            end_part = list(reversed(arr[i:]))
            return start_part + end_part
        i -= 1
    return -1


if __name__ == "__main__":
    n = int(input())
    arr = [int(string)for string in input().split()]
    answer = solution(n, arr)
    if answer == -1:
        print(answer)
    else:
        for index, num in enumerate(answer):
            if index == len(answer) - 1:
                print(num, end="")
            else:
                print(num, end=" ")

# arr[i - 1] > arr[j] : 값이 작아짐
# arr[i - 1] < arr[j] : 값이 커짐
# 따라서 arr[i - 1] > arr[j] 중 최댓값을 찾아야 함.
# arr[i - 1] > arr[i] < ... < arr[n]
# arr[n]부터 오른쪽에서 왼족으로 비교하면서, 처음으로 arr[i - 1] > arr[j] 인 j 찾기
# arr[i - 1] > arr[j] 이므로 arr[j - 1] < arr[j] < arr[i - 1]
# 오른쪽에서 왼쪽으로 반복문 실행했으므로 arr[i - 1] < arr[j + 1] < ... < arr[n]


# 2 1 3 4 -> 1 4 3 2
# 1. 오른쪽 -> 왼쪽으로 가면서 arr[i - 1] > arr[i] 만족하는 i 찾기
# 2. j = n - 1부터 시작하여 최초로 arr[j] < arr[i - 1]인 j 찾기 (arr[i - 1]보다 작은 것 중 최댓값, arr[i] < arr[i + 1] < ... < arr[n - 1]이므로)
# 3. swap(arr[i - 1], arr[j]), arr[j]  < arr[i - 1]이므로 arr[j - 1] < arr[j] < arr[i - 1], 오른쪽에서 왼쪽 탐색했으므로 arr[i - 1] < arr[j + 1]
#    arr[j - 1] < arr[i - 1] < arr[j + 1] 여전히 만족
# 4. arr[i:] 부분 reversed 시켜서 합치기
