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
    sorted_countries = sorted(countries, key=cmp_to_key(comparator))

    rank_table = {}

    current_rank = 1

    for i in range(n):
        if i > 0:
            medals = sorted_countries[i][1:]
            previous_medals = sorted_countries[i - 1][1:]
            if previous_medals != medals:
                current_rank = i + 1
        country_id = sorted_countries[i][0]
        rank_table[country_id] = current_rank

    return rank_table[k]


if __name__ == "__main__":
    n, k = [int(string) for string in input().split()]
    countries = [[int(string) for string in input().split()] for i in range(n)]
    answer = solution(n, k, countries)
    print(answer)


# 정렬 순서
# 1. 금메달 내림차순 >= 은메달 내림차순 >= 동메달 내림차순
# 2. hashmap 만들고, 등 수 별로 리스트로 관리
# 3. hashmap에서 탐색하여, 국가 k 등수 반환

# 내가 틀린 부분: 인덱스가 곧 등수가 아니다. 공동 등수를 차지한 국가만큼 등수 밀려야 함.

# 해결 방법
# 1. 금메달 내림차순 >= 은메달 내림차순 >= 동메달 내림차순 정렬
# 2. dictionary로 각 조합별 몇 팀 있는지 파악하기
#  diciotnary가 삽입 순서 유지한다는 점 이용해서, 순회하면서 등수 세서 반환

# 더 좋은 해결 방법
# medal_combinations, rank_table 모두 필요가 없음
# 메달 조합이 같으면 이전 순위 유지
# 메달 조합이 다르면 인덱스를 통해 현재 등수 계산 가능


# 3 1
# 3 0 0 1
# 1 0 0 1
# 2 0 0 1


# 4 3
# 1 1 2 0
# 2 0 1 0
# 3 0 1 0
# 4 0 0 1


# 5 5
# 4 0 0 1
# 5 0 0 1
# 1 1 0 0
# 2 0 1 1
# 3 0 1 1
