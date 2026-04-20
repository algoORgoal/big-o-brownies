import heapq


def solution(k, n, prime_nums):
    queue = []
    for num in prime_nums:
        heapq.heappush(queue, num)

    count = 0

    while len(queue) > 0:
        num = heapq.heappop(queue)

        count += 1
        if count == n:
            return num

        for prime_num in prime_nums:
            heapq.heappush(queue, prime_num * num)
            if prime_num * num >= 2 ** 31:
                break
            if num % prime_num == 0:
                break

    while True:
        num = heapq.heappop(queue)
        count += 1
        if count == n:
            return num


if __name__ == "__main__":
    k, n = [int(string) for string in input().split()]
    prime_nums = [int(string) for string in input().split()]
    answer = solution(k, n, prime_nums)
    print(answer)


# 2 3 5 7
# 2 때서 각각에 곱해주고, 2 * 2 넣기
# 3 5 7 / 4 6 10 14
# 3 때서 각각에 곱해주고, 3 * 3 넣기
# 5 7 / 4 6 10 14 / 15 21 12 18 30 42

# 언제까지 반복하지?


# 2 4 5 7
# 8 10 14
# 16 20 28 32
#
