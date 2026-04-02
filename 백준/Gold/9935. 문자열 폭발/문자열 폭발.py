from sys import stdin
from collections import deque

input = stdin.readline


def solution(queue, pattern):

    stack = []

    while len(queue) > 0:
        letter = queue.popleft()
        stack.append(letter)

        if len(stack) >= len(pattern):
            top_pattern = "".join(stack[-len(pattern):])
            if top_pattern == pattern:
                for i in range(len(top_pattern)):
                    stack.pop()

    string = "".join(stack)

    if string == "":
        return "FRULA"
    else:
        return string


if __name__ == "__main__":
    queue = deque([char for char in input().strip()])
    pattern = input().strip()
    answer = solution(queue, pattern)
    print(answer)


# root가 C4 * 500_000, target이 C4
# 500_000 * 500_000 => O(n ** 2)

# 1 3 5 4 2
# 3 1 5 4 2


# queue 및 스택을 사용한다.
# stack의 top + queue에서 빼온 문자 => pop시키기
# stack이 empty => FRULA
# 아니라면, "".join(stack) 반환

# 시간복잡도: O(nm)
# 공간복잡도: O(n)
