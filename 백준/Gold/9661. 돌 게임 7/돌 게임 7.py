

def solution(n):
    digit = n % 10
    first_win_digits = {1, 3, 4, 6, 8, 9}

    if digit in first_win_digits:
        return 0
    else:
        return 1


if __name__ == "__main__":
    n = int(input())
    answer = solution(n)
    if answer == 0:
        print("SK")
    else:
        print("CY")


# 홀수개의 1, 4, 16, ...의 합으로 분할 가능 => SK 승
# 짝수개의 1, 4, 16, ...의 합으로만 분할 가능 => CY 승

# 끝자리가 1, 3, 4, 6, 8, 9 => SK 우승
# 끝자리가 1, 3, 6, 8 => CY 우승

# 0 CY
# 1 SK
# 2 CY
# 3 SK
# 4 SK
# 5 CY
# 6 SK
# 7 CY
# 8 SK
# 9 SK
# 10 CY
# 11 SK
# 12 CY
# 13 SK
# 14 SK
# 15 CY
# 16 SK
# 17 CY
# 18 SK
# 19 SK
# 20 CY
# 21 SK
# 22 CY
# 23 SK
# 24 SK
# 25 CY
# 26 SK
# 27 CY
# 28 SK
# 29 SK
# 30 CY
# 31 SK
# 32 CY
# 33 SK
# 34 SK
# 35 CY
# 36 SK
# 37 CY
# 38 SK
# 39 SK
# 40 CY
# 41 SK
# 42 CY
