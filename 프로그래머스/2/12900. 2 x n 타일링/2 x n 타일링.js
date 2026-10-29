function solution(n) {
    const dp = [ 0, 0, 0 ];
    dp[0] = 1;
    dp[1] = 2;
    
    if (n === 1) {
        return dp[0];
    }
    
    if (n === 2) {
        return dp[1];
    }
    
    for (let i = 3; i <= n; i++) {
        dp[2] = (dp[0] + dp[1]) % 1_000_000_007;
        dp[0] = dp[1];
        dp[1] = dp[2];
    }
    
    
    
    
    return dp[1] % 1_000_000_007;
}