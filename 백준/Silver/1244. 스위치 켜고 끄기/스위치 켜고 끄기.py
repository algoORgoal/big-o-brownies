def solution(n, m, switches, cards):
    adjusted_switches = [0] + switches

    for gender, num in cards:
        if gender == 1:
            for i in range(num, len(adjusted_switches), num):
                adjusted_switches[i] ^= 1
        else:
            offset = 0
            while 1 <= num - offset < len(adjusted_switches) and 1 <= num + offset < len(adjusted_switches) and adjusted_switches[num - offset] == adjusted_switches[num + offset]:
                if offset == 0:
                    adjusted_switches[num - offset] ^= 1
                else:
                    adjusted_switches[num - offset] ^= 1
                    adjusted_switches[num + offset] ^= 1
                offset += 1

    return adjusted_switches[1:]


if __name__ == "__main__":
    n = int(input())
    switches = [int(string) for string in input().split()]
    m = int(input())
    cards = [[int(string) for string in input().split()] for i in range(m)]
    answer = solution(n, m, switches, cards)
    for index, num in enumerate(answer):
        if index % 20 == 19:
            print(num, end="\n")
        else:
            print(num, end=" ")


# 1인 경우 => 카드의 배수가 되는 스위치 바꾸기
# 2인 경우 => 해당 숫자를 중심으로 대칭을 이루는 최대 구간 모두 바꾸기
# 시간복잡도 O(nm)
# 공가복잡도 O(n)


# 40
# 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1
# 1
# 1 3
