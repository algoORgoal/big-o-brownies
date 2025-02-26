// 모든 경우의 수를 탐색하면 O(n!)이므로 현실적으로 불가능하다.
// 큰 빌딩부터 차례대로 놓는다고 해보자.
// sum(dp[i]) = sum(dp[i-1]) * ((i - 1) * 2 + 1)
// 기존 빌딩의 배치 경우의 수가 dp[i-1]이고, 기존 배치된 배열 사이에 현재 빌딩을 배치할 수 있기에 경우의 수가 ((i - 1) * 2 + 1)이다.
// 기존 빌딩 배치의 맨 앞에 현재 빌딩 놓으면 count가 1 증가하고, 그 밖의 곳에 넣으면 count가 그대로 유지된다.
// dp[i][j]: 높이 i까지의 빌딩 쌍을 이용하여 j가 보이는 경우의 수
// dp[i][0] = 0
// dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] * (i - 1) * 2
// dp[i][i] = dp[i - 1][i - 1](dp[i - 1][i]는 존재 불가능)
// base case: dp[i][0] = 0, dp[1][1] = 1

function solution(n, count) {
    const dp = Array.from({ length: n + 1 }, () => Array.from({ length: n + 1 }, () => 0));
    for (let i = 0; i < dp.length; i++) {
        if (i === 0) continue;
        if (i === 1) {
            dp[1][0] = 0;
            dp[1][1] = 1;
            continue;
        }
        dp[i][0] = 0;
        for (let j = 1; j < i; j++) {
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] * (i - 1) * 2) % 1_000_000_007;
        }
        dp[i][i] = dp[i - 1][i - 1]  % 1_000_000_007;
    }
    return dp[n][count] % 1_000_000_007;
}