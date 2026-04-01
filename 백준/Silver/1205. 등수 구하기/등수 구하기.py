from bisect import bisect_right
from bisect import bisect_left

# 5 10 10 20
# 5 10 10 10 20


def solution(n, new_score, p, scores):
    sorted_scores = sorted(scores)

    amount = len(scores) + 1 - bisect_left(sorted_scores, new_score)
    if amount > p:
        return -1

    rank = len(scores) + 1 - bisect_right(sorted_scores, new_score)

    return rank


if __name__ == "__main__":
    n, score_to_add, p = [int(string) for string in input().split()]
    if n == 0:
        print("1")
    else:
        scores = [int(string) for string in input().split()]
        answer = solution(n, score_to_add, p, scores)
        print(answer)

# rank_table로 랭킹 계산
# new_score를 포함한 rank_table로 계산
# new_score까지의 점수의 개수 > p => -1 반환
# 아니라면 rank_table[new_score] 반환
