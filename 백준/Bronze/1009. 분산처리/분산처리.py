
# 20번 컴퓨터 => 10
# 21번 컴퓨터 => 1

# 1 => 0
# 2 => 1
# 3 => 2
# 4 => 3
# 5 => 0

def solution(a, b):
    first_digit = int(str(a)[-1])

    table = {
        0: [10],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1],
    }

    return table[first_digit][(b - 1) % len(table[first_digit])]


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b = [int(string) for string in input().split()]
        answer = solution(a, b)
        print(answer)


# 2 ** 1 = 2
# 2 ** 2 = 4
# 2 ** 3 = 8
# 2 ** 4 = 16
# 2 ** 5 = 32


# 3 ** 1 = 3
# 3 ** 2 = 9
# 3 ** 3 = 27
# 3 ** 4 = 81
# 3 ** 5 = 243
# 3 ** 6 = 729

# 4
# 6
# 4
# 6
# 4

# 6
# 6
# 6
# 6
# 6

# 7
# 9
# 3
# 1
# 7

# 8
# 4
# 2
# 6
# 8

# 9
# 1
# 9
# 1
# 9
# 1
