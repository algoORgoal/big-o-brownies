
def solution(hour, min, offset):
    while offset > 0:
        min += 1

        if min == 60:
            hour += 1
            min = 0

        if hour == 24 and min == 0:
            hour = 0
            min = 0

        offset -= 1

    return hour, min


if __name__ == "__main__":
    hour, min = [int(string) for string in input().split()]
    offset = int(input())
    answer = solution(hour, min, offset)
    print(*answer)

# 시간복잡도: O(c) (0 <= c <= 1000)
