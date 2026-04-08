def solution(n, words):
    table = {}
    for word in words:
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            if prefix not in table:
                table[prefix] = 0

            table[prefix] += 1

    longest_prefix = ""

    # python 3.7부터, dictionary는 삽입 순서가 보장된다.
    # 처음 출현하는 단어의 순서가 이를수록 prefix도 일찍 접근하게 된다.
    # 따라서 가장 긴 prefix 중 가장 일찍 나오는 prefix에 접근하게 된다.
    for prefix in table:
        if table[prefix] >= 2 and len(longest_prefix) < len(prefix):
            longest_prefix = prefix

    most_similar_words = []

    # 동일한 prefix를 가지는 단어들 중 가장 빨리 나오는 두 단어를 고른다.
    for word in words:
        if word[:len(longest_prefix)] == longest_prefix:
            most_similar_words.append(word)

        if len(most_similar_words) == 2:
            return most_similar_words


if __name__ == "__main__":
    n = int(input())
    words = [input() for i in range(n)]
    answer = solution(n, words)
    for word in answer:
        print(word)

# 두 단어끼리 비교해서 common prefix 크기 구하기 => O(w) (1 <= w <= 100)
# 모든 단어끼리 서로 비교 => 4 * (10 ** 8) * 100 = 4 * 100 000 000 * 100 => TLE

# dp['a'-'z']['a'-'z']...['a'-'z'] 27 ** 100: 시간 초과, 메모리 초과

# 각 단어 별로,
# prefix의 hash table 1씩 증가시키기
# hash table의 key 개수: n * 100 (n <= 20_000)

# prefix 중에서 가장 일찍 나오고, 가장 긴 prefix 선정(빈도 2 이상)
# words에서 prefix로 시작하는 문자열 두개 뽑아서 반환


# 8바이트 * 2_000_000
# 16바이트 * 1_000_000
# 16kb => 16mb
