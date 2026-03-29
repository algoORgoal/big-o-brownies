from functools import cmp_to_key


def comparator(a, b):
    a_id, a1, a2, a3 = a
    b_id, b1, b2, b3 = b
    if a1 != b1:
        return b1 - a1
    if a2 != b2:
        return b2 - a2
    return b3 - a3


def solution(n, k, countries):

    sorted_countries = sorted(
        countries, key=cmp_to_key(comparator))

    medal_combinations = {}

    for country in sorted_countries:
        identifier, gold, silver, bronze = country
        if (gold, silver, bronze) not in medal_combinations:
            medal_combinations[(gold, silver, bronze)] = []
        medal_combinations[(gold, silver, bronze)].append(identifier)

    target_country = countries[k - 1]
    target_combination = tuple(target_country[1:])

    for index, combination in enumerate(medal_combinations):
        if k in medal_combinations[combination]:
            return index + 1


if __name__ == "__main__":
    n, k = [int(string) for string in input().split()]
    countries = [[int(string) for string in input().split()] for i in range(n)]
    answer = solution(n, k, countries)
    print(answer)


# 정렬 순서
# 1. 금메달 내림차순 >= 은메달 내림차순 >= 동메달 내림차순
# 2. hashmap 만들고, 등 수 별로 리스트로 관리
# 3. hashmap에서 탐색하여, 국가 k 등수 반환
