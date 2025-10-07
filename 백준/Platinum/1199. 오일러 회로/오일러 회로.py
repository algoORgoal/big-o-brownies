import sys
sys.setrecursionlimit(10**6)

def main(vertexCount: int, matrix: list[list[int]]):
    n = vertexCount

    # 차수 검사
    for i in range(n):
        if sum(matrix[i]) % 2 == 1:
            print(-1)
            return

    # 각 정점에 대해 이웃 스택을 만든다 (중복 허용)
    # 중복으로 넣어두면 pop() 한 번으로 '한 번 사용할 수 있는 반쪽 간선'을 나타냄
    adj_stacks = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cnt = matrix[i][j]
            if cnt > 0:
                # i 방향으로 j를 cnt번 push
                # (무향이므로 matrix[j][i]에도 동일하게 push 되어 있을 것임)
                adj_stacks[i].extend([j] * cnt)

    # Hierholzer - 스택(반복) 버전. 재귀 깊이 신경 쓸 필요 없음.
    start = 0
    stack = [start]
    path = []

    while stack:
        v = stack[-1]
        # adj_stacks[v]에서 하나 꺼내서 실제로 사용 가능한지 확인
        while adj_stacks[v]:
            u = adj_stacks[v].pop()   # O(1)
            # lazy-skip: pop한 항목이 이미 다른 쪽에서 소모되어 matrix[v][u] == 0일 수 있음
            if matrix[v][u] > 0:
                # 무향이므로 양쪽을 동시에 감소
                matrix[v][u] -= 1
                matrix[u][v] -= 1
                stack.append(u)
                break
            # matrix[v][u] == 0 이면 이미 소모된 항목이므로 그냥 계속 pop
        else:
            # 더 이상 나갈 간선이 없으면 경로에 추가
            path.append(stack.pop())

    # path는 끝에서부터 역순으로 쌓였으므로 뒤집어 출력
    path.reverse()
    print(" ".join(str(x+1) for x in path))


if __name__ == "__main__":
    vertexCount = int(sys.stdin.readline())
    mat = []
    for _ in range(vertexCount):
        row = list(map(int, sys.stdin.readline().split()))
        mat.append(row)
    main(vertexCount, mat)