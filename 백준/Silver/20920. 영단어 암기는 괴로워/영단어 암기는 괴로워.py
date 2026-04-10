from sys import stdin
from sys import stdout
from functools import cmp_to_key

input = stdin.readline


def print(string, end="\n"):
    stdout.write(f"{string}{end}")


def comparator(a, b):
    a_word, a_frequencies = a
    b_word, b_frequencies = b

    if a_frequencies != b_frequencies:
        return b_frequencies - a_frequencies

    if len(a_word) != len(b_word):
        return len(b_word) - len(a_word)

    return -1 if a < b else 1


def solution(n, m, words):
    table = {}
    for word in words:
        if len(word) < m:
            continue

        if word not in table:
            table[word] = 0

        table[word] += 1

    return [word for word, frequencies in sorted([(word, table[word]) for word in table], key=cmp_to_key(comparator))]


if __name__ == "__main__":
    n, m = [int(string) for string in input().strip().split()]
    words = [input().strip() for i in range(n)]
    answer = solution(n, m, words)
    for word in answer:
        print(word)


# (단어 빈도, 단어)
# 1. 단어 빈도 내림차순
# 2. 단어 길이 내림차순
# 3. lexicographically (오름차순)

# 길이가 m 이상인 것만

# 정렬 =>
# 시간복잡도 O(nlogn)
# 공간복잡도 O(n)
