# dp[j] = max(dp[j], dp[j - w] + v) (j >= w), dp[0] = 0
# 문제였던 부분: 각 dp마다 모든 물건의 가치를 고려한 최대합을 계산하려고 했으나, 순차적으로 각 물건을 고려했을 때의 최댓값을 계산해야 문제를 풀 수 있다.

def main(n, k, stuffs):
    dp = [ 0 for i in range(k + 1) ]
    for weight, value in stuffs:
        for i in range(k, -1, -1):
            if  i >= weight:
                dp[i] = max(dp[i], dp[i - weight] + value)
    return dp[k]

if __name__ == "__main__":
    n, k = [ int(i) for i in input().split(' ')]
    stuffs = [ [ int(j) for j in input().split(' ') ] for i in range(n) ]
    answer = main(n, k, stuffs)
    print(answer)