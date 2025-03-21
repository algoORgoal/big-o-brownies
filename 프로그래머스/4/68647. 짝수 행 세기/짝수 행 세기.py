def solution(a):
    mod = 10000019
    r = len(a)           # 행의 개수
    m = len(a[0])        # 열의 개수

    # a의 각 열의 1의 개수를 구합니다.
    A = [sum(a[i][j] for i in range(r)) for j in range(m)]
    
    # 만약 열의 개수가 1이면, 모든 행이 0이어야 (짝수) 하므로 a의 열 합이 0이어야 함.
    if m == 1:
        return 1 if A[0] == 0 else 0

    # 첫 m-1열을 자유롭게 채울 수 있는 부분 (free part)
    free = m - 1

    # 조합 계산을 위해 comb[i][j] = C(i, j) 를 미리 구합니다. (0 ≤ i, j ≤ r)
    comb = [[0]*(r+1) for _ in range(r+1)]
    for i in range(r+1):
        comb[i][0] = 1
        comb[i][i] = 1
        for j in range(1, i):
            comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % mod

    # dp[i][j]: 첫 i열 (free part)를 채운 후, 총 행 중 j개의 행이 홀수 상태(1의 개수가 홀수)인 경우의 수
    dp = [[0]*(r+1) for _ in range(free+1)]
    dp[0][0] = 1  # 아직 열을 채우지 않았으므로 모든 행은 0(짝수) 상태

    # free 부분의 각 열에 대해 처리 (열 인덱스 0 ~ free-1)
    for i in range(free):
        # 이번 열에서 채워야 하는 1의 개수는 A[i]로 정해져 있음.
        k_target = A[i]
        for odd in range(r+1):
            ways = dp[i][odd]
            if ways == 0:
                continue
            # 현재 상태에서 짝수 상태인 행의 개수는 (r - odd)
            even = r - odd

            # 이번 열에서 짝수 행에서 x개, 홀수 행에서 y개를 선택하여 1을 배치한다고 하자.
            # x + y = k_target, 단, 0 ≤ x ≤ even, 0 ≤ y ≤ odd.
            # x의 가능한 범위는 max(0, k_target - odd)부터 min(k_target, even)까지.
            for x in range(max(0, k_target - odd), min(k_target, even) + 1):
                y = k_target - x
                if y > odd:
                    continue
                # 이번 열을 채운 후, 상태 업데이트:
                # 짝수 행에서 1을 선택하면 해당 행은 홀수로 바뀌고 (x개),
                # 홀수 행에서 1을 선택하면 해당 행은 짝수로 바뀝니다 (y개 사라짐).
                # 따라서 새 홀수 행의 수 = (현재 홀수 중 1을 선택하지 않은 행: odd - y) + (짝수 중 1을 선택한 행: x)
                new_odd = (odd - y) + x

                # 이번 열에 대해, 짝수 행에서 x개 선택하는 경우의 수: C(even, x)
                # 홀수 행에서 y개 선택하는 경우의 수: C(odd, y)
                dp[i+1][new_odd] = (dp[i+1][new_odd] + ways * comb[even][x] * comb[odd][y]) % mod

    # free 부분을 채운 후, 각 행의 마지막 원소(열 m-1)는 앞 열의 홀짝 상태에 따라 결정됩니다.
    # 한 행의 마지막 원소는, 앞 열에서 해당 행의 1의 개수가 홀수이면 1, 짝수이면 0이 되어 전체 행의 1의 개수를 짝수로 만듭니다.
    # 따라서, 마지막 열의 1의 개수는 free part에서 홀수 상태인 행의 수와 같아집니다.
    # 문제 조건에 따라, 마지막 열의 1의 개수는 A[m-1]이어야 하므로,
    # 최종 정답은 dp[free][A[m-1]] 가 됩니다.
    return dp[free][A[m-1]] % mod