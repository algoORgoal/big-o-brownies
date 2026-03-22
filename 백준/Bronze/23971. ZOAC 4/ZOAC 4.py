
from math import ceil


def solution(h, w, n, m):
    return ceil((h / (n + 1))) * ceil(w / (m + 1))


if __name__ == "__main__":
    h, w, n, m = [int(string) for string in input().split()]
    answer = solution(h, w, n, m)
    print(answer)


# h * w에 세로 n칸, 가로 m칸 이상 비우고 앉기
# h <= (n + 1) => 1
# w <= (m + 1) => 1

# Math.ceil(h / (n + 1))
# Math.ceil(w / (m + 1))

# 5 4 1 1
# 6

# 2 2 3 3
# 1

# 10 2 3 2
