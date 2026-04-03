from math import inf


def solution(n, rank_list):
    team_rank_table = {}
    for index, team in enumerate(rank_list):
        rank = index + 1

        if team not in team_rank_table:
            team_rank_table[team] = []
        team_rank_table[team].append(rank)

    invalid_teams = set()

    for team in team_rank_table:
        if len(team_rank_table[team]) < 6:
            invalid_teams.add(team)

    rank_score_table = {}

    current_score = 1
    for index, team in enumerate(rank_list):
        rank = index + 1

        if team in invalid_teams:
            rank_score_table[rank] = -inf
        else:
            rank_score_table[rank] = current_score
            current_score += 1

    valid_team_scores = []
    for team in team_rank_table:
        if team not in invalid_teams:

            first = sum(
                [rank_score_table[rank] for rank in team_rank_table[team][:4]])
            second = rank_score_table[team_rank_table[team][4]]
            third = rank_score_table[team_rank_table[team][5]]
            valid_team_scores.append((first, second, third, team))

    winner_team_score = sorted(valid_team_scores)[0]

    return winner_team_score[3]


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        rank_list = [int(string) for string in input().split()]
        answer = solution(n, rank_list)
        print(answer)

# 해쉬 테이블을 이용하여, 팀 별로의 등수 기록하기
# 4 명이 되지 않는 팀 찾기
# 4 명이 되지 않는 팀 번호를 기반으로, 등수를 점수로 변환하는 테이블 만들기
# 유효한 팀들을 4명 점수 기준으로 오름차순하기
# 가장 낮은 점수의 팀들 고르기
# 그 중에서 5번째 주자 점수 비교 => 동일할 경우 6번째 주자 점수 비교
# [4명까지 점수, 5번재 주자 점수, 6번째 주자 점수, 팀 번호] 오름차순으로 정렬

# 시간복잡도: nlog(n)
