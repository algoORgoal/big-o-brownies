from math import inf
from functools import lru_cache

def solution(n, weak, dist):
    m = len(weak)
    extended = weak + [w + n for w in weak]

    dist.sort(reverse=True)

    cover = [[0] * len(dist) for _ in range(m)]

    for start_idx in range(m):
        for friend_idx, d in enumerate(dist):
            limit = extended[start_idx] + d
            mask = 0

            for j in range(start_idx, start_idx + m):
                if extended[j] <= limit:
                    mask |= 1 << (j % m)
                else:
                    break

            cover[start_idx][friend_idx] = mask

    @lru_cache(None)
    def dfs(friend_idx, remain_mask):
        if remain_mask == 0:
            return friend_idx

        if friend_idx == len(dist):
            return inf

        answer = inf

        for start_idx in range(m):
            if remain_mask & (1 << start_idx):
                next_mask = remain_mask & ~cover[start_idx][friend_idx]
                answer = min(answer, dfs(friend_idx + 1, next_mask))

        return answer

    result = dfs(0, (1 << m) - 1)
    return result if result != inf else -1