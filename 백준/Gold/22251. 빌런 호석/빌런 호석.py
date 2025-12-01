# 각 dfs 연산마다 필요한 데이터
# n(upper bound)
# k: 만들 수 있는 자릿수 (10**k)
# left_conversion_count: 남은 반전 가능한 횟수
# current: 현재 숫자
# 각 depth마다 특정 자릿수를 변경했을 때 만들 수 있는 상태를 반환
# 만들 수 있는 상태: 반전 가능한 횟수가 필요한 반전 횟수 이상인가
# 반전 횟수 구하는 법: 비트마스크로 숫자를 표현하고 xor해서 1 나오는 부분 몇 개인지 찾기

table = {
    0: 0b1110111,
    1: 0b0010010,
    2: 0b1011101,
    3: 0b1011011,
    4: 0b0111010,
    5: 0b1101011,
    6: 0b1101111,
    7: 0b1010010,
    8: 0b1111111,
    9: 0b1111011,
}

def solution(n, k, p, x):
    return dfs(n, 0, k, p, x) - 1

def dfs(upper_bound, target_digit, digit_count, left_conversion_count, current):
    state_count = 0

    if target_digit == digit_count:
        if 1 <= current <= upper_bound:
            return 1
        else:
            return 0

    padded = f"{current:0{digit_count}d}"

    for i in range(0, 10):
        required_conversion_count = bin(table[int(padded[target_digit])] ^ table[i]).count("1")
        if required_conversion_count > left_conversion_count:
            continue

        
        candidate = int(padded[:target_digit] + str(i) + padded[target_digit + 1:])

        state_count += dfs(upper_bound, target_digit + 1, digit_count, left_conversion_count - required_conversion_count, candidate)
    
    return state_count
        


if __name__ == "__main__":
    n, k, p, x = [ int(i) for i in input().split() ]
    answer = solution(n, k, p, x)
    print(answer)


# 내가 생각하지 못했던 부분
# 앞자리를 무조건 바꾸는 노드만 각 상태에서 확인한다면, 앞자리를 그대로 두는 유효한 노드의 개수를 셀 수가 없다.
# 따라서 노드의 개수르 
