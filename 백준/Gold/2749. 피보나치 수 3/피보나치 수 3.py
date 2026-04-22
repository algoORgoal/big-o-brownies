

def solution(n):
    cache = {}

    a = 0
    b = 1

    cache[0] = 0
    cache[1] = 1

    if n == 0:
        return a
    if n == 1:
        return b
    for i in range(2, 1_500_000):
        c = (a + b) % 1_000_000

        cache[i] = c

        a = b
        b = c
    return cache[n % 1_500_000]


if __name__ == "__main__":
    n = int(input())
    answer = solution(n)
    print(answer)

# n <= 10 ** 18
# a = 0, b = 1이 150만 주기로 반복됌
# cache에 150만까지 저장하고 반환
# cache[i] = cache[i + 1_500_000]
# cache[n] = cache[n % 1_500_000]
# cache[0] = cache[1_500_000]
# cache[1] = cache[1_500_001]
