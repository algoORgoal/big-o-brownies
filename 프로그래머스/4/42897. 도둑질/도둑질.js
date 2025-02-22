// dp[k] = max(dp[k - 1], dp[k - 2] + house[k])

function solution(money) {
    const dp = Array.from({ length: money.length, }, () => 0);
    
    if (money.length === 1) {
        return money[0];
    }
    
    if (money.length <= 2) {
        return Math.max(money[0], money[1]);
    }
    
    for (let i = 0; i < dp.length - 1; i++) {
        if (i === 0) {
            dp[i] = money[i];
            continue;
        }
        if (i === 1) {
            dp[i] = Math.max(dp[i], dp[i - 1]);
            continue;
        }
        dp[i] = Math.max(dp[i - 1], dp[i - 2] + money[i]);
    }

    let max = dp[dp.length - 2];
    
    for (let i = 0; i < dp.length; i++) {
        dp[i] = 0;
    }
        
    for (let i = 1; i < dp.length; i++) {
        if (i === 1) {
            dp[i] = money[i];
            continue;
        }
        dp[i] = Math.max(dp[i - 1], dp[i - 2] + money[i]);
    }
    
    max = Math.max(max, dp[dp.length - 1]);
    
    return max;
    
}