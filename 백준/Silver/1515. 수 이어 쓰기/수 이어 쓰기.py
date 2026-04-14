from collections import deque


def solution(num_str):
    digit_chars = deque([char for char in num_str])

    for i in range(1, 100_000_000):
        target = str(i)
        digit_str = ""

        for char in target:
            if len(digit_chars) > 0 and digit_chars[0] == char:
                digit_chars.popleft()

        if len(digit_chars) == 0:
            return i

    return i


if __name__ == "__main__":
    num_str = input()
    answer = solution(num_str)
    print(answer)


# 최대 3000자리이므로 1부터 3000까지하면 충분(각 자리당 최소 1자리 차지하므로)
# 1부터 3000까지 각 자리당 숫자를 최대한 붙일 수 있는대로 붙여서 뺌

# 시간복잡도 O(n)
# 공간복잡도: O(n)
