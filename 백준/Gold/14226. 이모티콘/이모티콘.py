from collections import deque
from math import inf


def solution(s):
    return bfs(1, s, set())


def bfs(root, target, visited):
    queue = deque()

    queue.appendleft((0, root, None))
    # 거리, 노드, 복사된 값

    visited.add((root, None))

    count = 0

    while len(queue) > 0:
        distance, current, copied = queue.pop()
        count += 1

        if current == target:
            return distance

        candidates = [(distance + 1, current - 1, copied)]
        if current != copied:
            candidates.append((distance + 1, current, current))
        if copied != None:
            candidates.append((distance + 1, current + copied, copied))

        for candidate in candidates:
            _, candidate_node, candidate_copied = candidate
            if (candidate_node, candidate_copied) in visited:
                continue
            if 1 <= candidate_node <= 2000 and 1 <= candidate_copied <= 2000:
                visited.add((candidate_node, candidate_copied))
                queue.appendleft(candidate)

    return inf


if __name__ == "__main__":
    s = int(input())
    answer = solution(s)
    print(answer)

# 복사 => 삭제 => 붙여넣기
# 복사 => 붙여넣기 => 삭제
# 동일한 결과를 보이기 때문에, 복사, 붙여넣기를 한 연산으로 보아도 된다.
# 경로의 최단거리를 구하는 것이므로 bfs로 해결 가능
# start state = 1
# end state = s
# transition function: 2배 늘어나게 만들고 거리 + 2 / 하나 지우고 거리 + 1
# a set of states: 1 <= s <= 2000 (2000에서 만들려면, 최소 1000번 지워야 함)
# 현재 거리가 가장 가까운 것을 제일 먼저 빼내야하므로, heap을 사용해야한다. queue로 쌓으면 순서 보장 불가능
# 예) 빼기, 빼기, 곱하기 push => 다음 노드 방문 => 빼기, 빼기, 곱하기 push
# queue에 다음면 [..., 빼기, 빼기, 곱하기, 빼기, 빼기, 곱하기]
# 그런데 사실은 [빼기 빼기, 빼기, 빼기, 곱하기, 곱하기] 순으로 체크해야 함


# 시간복잡도: O(vlogv + e) = O(vlogv + 2v) = O(vlogv) (v <= 2000)
# 공간복잡도: O(v)
