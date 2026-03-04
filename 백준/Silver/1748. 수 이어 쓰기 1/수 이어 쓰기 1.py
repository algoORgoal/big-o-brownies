def count(n, digit=0):
    if n >= 10 ** (digit + 1):
        sum = (10 ** (digit + 1) - 10 ** digit) * (digit + 1)
        return sum + count(n, digit + 1)
    else:
        return (n - 10 ** digit + 1) * (digit + 1)


def solution(n):
    return count(n)


if __name__ == "__main__":
    n = int(input())
    answer = solution(n)
    print(answer)

# 5 = len(12345)
# 15 = len(123456789 101112131415) = 9 + 12 = 21
# 1부터 n까지 길이를 계산해서 더하면 됨 (n <= 100_000_000)
# 시간복잡도 O(n)
# 공간복잡도 O(1)

# 문제: string의 len을 하는데 오래 걸림
# 1 <= n: 1
# 10 <= n: 2
# 100 <= n: 3 (10 - 1)
