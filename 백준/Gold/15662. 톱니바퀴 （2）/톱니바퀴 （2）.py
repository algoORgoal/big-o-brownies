

def solution(t, gears, k, commands):
    for num, direction in commands:
        index = num - 1

        left, right = find_range(t, gears, index)
        for i in range(left, right + 1):
            diff = abs(i - index)
            if diff % 2 == 0:
                gears[i] = spin(gears[i], direction)
            else:
                gears[i] = spin(gears[i], 1 if direction == -1 else -1)

    count = 0
    for gear in gears:
        if int(gear[0], base=2) == 1:
            count += 1

    return count


def find_range(t, gears, target):
    left = target
    right = target

    while 0 < left:
        if int(gears[left - 1][2], base=2) ^ int(gears[left][6], base=2) == 1:
            left -= 1
        else:
            break

    while right < t - 1:
        if int(gears[right][2], base=2) ^ int(gears[right + 1][6], base=2) == 1:
            right += 1
        else:
            break

    return left, right


# bin: 십진수를 이진수 문자열로 변환
# int: n진수 문자열을 10진수로 변환
# 2진수 문자열을 10진수 변환 => bitwise rotation => 이진수 변환후 앞의 0b 제거


def spin(bin_str, direction):
    num = int(f"0b{bin_str}", base=2)
    if direction == 1:
        rotated_num = ((num >> 1) | (num << 7)) & 0b11111111
    else:
        rotated_num = ((num << 1) | (num >> 7)) & 0b11111111
    rotated_bin_str = bin(rotated_num)[2:]

    return "0" * (8 - len(rotated_bin_str)) + rotated_bin_str


if __name__ == "__main__":
    t = int(input())
    gears = [input() for i in range(t)]
    k = int(input())
    commands = [[int(string) for string in input().split()] for i in range(k)]
    answer = solution(t, gears, k, commands)
    print(answer)


# index, direction이 주어짐
# gear[index][2]: 왼쪽 부분
# gear[index][6]: 오른쪽 부분
# 왼쪽으로 6 - 2번이 서로 다른 연속되는 부분 찾음
# 오른쪽으로 6 - 2번이 서로 다른 연속되는 부분 찾음
# [왼쪽, 오른쪽] 구간에 대해, gear[index] 시계방향(1) 회전 => >> 반시계방향(-1) 회전 => <<
# gear[index - 1], gear[index + 1]은 gear[index]의 반대로 회전, ... 반복

# 시간복잡도: O(k * t)
# 공간복잡도: O(t)

# 현재 left에 대해서:
# left - 1 >= 0 and left - 1의 2번째 digit xor left의 6번째 digit == 1:
#   left -= 1

# 현재 right에 대해서:
# right + 1 < t and right의 2번째 digit xor right + 1의 6번째 digit == 1:
#   right += 1


# range에 대해, diff == 홀수 => 반대 방향, diff == 짝수 => 정방향
