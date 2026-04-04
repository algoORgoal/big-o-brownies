from collections import deque


def solution(n):
    queue = deque([i for i in range(1, n + 1)])

    while len(queue) > 1:
        queue.popleft()
        num = queue.popleft()
        queue.append(num)

    return queue[0]


if __name__ == "__main__":
    n = int(input())
    answer = solution(n)
    print(answer)

# deque 써서, popleft / popleft + append
# 이 과정에서 길이 1만 남는 경우 해당 숫자 반환
# 시간복잡도: O(n)
# 공간복잡도: O(n)
