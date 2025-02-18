function solution(target) {
    const dp = Array.from({ length: target + 1 > 20 ? target + 1 : 21 }, () => [ Infinity, -Infinity ]);
    
    dp[0] = [ 0, 0 ];
    for (let i = 1; i <= 20; i++) {
        dp[i] = [ 1, 1 ];
    }
    
    for (let i = 21; i <= target; i++){
        for (let j = 1; j <= 20; j++) {
            const single = [ dp[i - j][0] + 1, dp[i - j][1] + 1];
            if (single[0] < dp[i][0] || (single[0] === dp[i][0] && single[1] > dp[i][1])) {
                dp[i] = single;
            }
            if (i - 2 * j < 0) continue;
            const double = [ dp[i - 2 * j][0] + 1, dp[i - 2 * j][1] ];
            if (double[0] < dp[i][0] || (double[0] === dp[i][0] && double[1] > dp[i][1])) {
                dp[i] = double;
            }
            if (i - 3 * j < 0) continue;
            const triple = [ dp[i - 3 * j][0] + 1, dp[i - 3 * j][1] ];
            if (triple[0] < dp[i][0] || (triple[0] === dp[i][0] && triple[1] > dp[i][1])) {
                dp[i] = triple;
            }
        }
        if (i >= 50) {
            const bull = [ dp[i - 50][0] + 1, dp[i - 50][1] + 1 ];
            if (bull[0] < dp[i][0] || (bull[0] === dp[i][0] && bull[1] > dp[i][1])) {
                dp[i] = bull;
            }
        }
    }
    return dp[target];
}
