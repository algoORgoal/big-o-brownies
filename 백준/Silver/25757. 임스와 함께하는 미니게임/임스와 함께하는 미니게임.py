def solution(n, type, requests):
    requesting_players = set(requests)
    if type == "Y":
        return len(requesting_players)
    elif type == "F":
        return len(requesting_players) // 2
    elif type == "O":
        return len(requesting_players) // 3


if __name__ == "__main__":
    tokens = input().split()
    n, type = int(tokens[0]), tokens[1]

    requests = [input() for i in range(n)]
    answer = solution(n, type, requests)
    print(answer)


# 동일한 플레이어와 게임을 못함
# 게임을 플레이할 수 있는 횟수:
# Y => 신청한 플레이어의 수
# F => 신청한 플레이어의 수 // 2 (3명씩 플레이 가능, 임 + 2명의 플레이어)
# O => 신청한 플레이어의 수 // 3 (4명씩 플레이 가능, 임 + 3명의 플레이어)

# 시간복잡도 O(1)
# 공간복잡도 O(n)
