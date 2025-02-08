function solution(n, money) {
    const memo = Array.from({ length: 2 }, () => Array.from({ length: n + 1 }, () => 0));
    const sortedMoney = money.sort((a, b) => a - b);
    for (let i = 0; i < money.length; i++) {
        const coin = sortedMoney[i];
        for (let j = 1; j <= n; j++) {
            if (i === 0 && j < coin) continue;
            if (i === 0 && j === coin) {
                memo[i & 1][j] = 1;
                continue;
            }
            if (i === 0 && j > coin) {
                memo[i & 1][j] = memo[i & 1][j - coin];
                continue;
            }
            if (j < coin) {
                memo[i & 1][j] = memo[(i & 1) ^ 1][j];
                continue;
            }
            if (j === coin) {
                memo[i & 1][j] = memo[(i & 1) ^ 1][j] + 1;
                continue;
            }
            if (j > coin) {
                memo[i & 1][j] = memo[(i & 1) ^ 1][j] + memo[i & 1][j - coin];
                continue;
            }
            throw new Error("invalid index");
        }
    }
    
    return memo[(money.length - 1) & 1][n] % 1_000_000_007
}

// [ 1, 2 ] 10
// 1 1 1 1 1 1 1 1 1 1
// 2 1 1 1 1 1 1 1 1
// 2 2 1 1 1 1 1 1
// 2 2 2 1 1 1 1
// 2 2 2 2 1 1
// 2 2 2 2 2

// 1 1 1 1 1
// 1 1
// 2
// 2 1
// 1 1 1



// only considers these cases
// 1. the number of ways to form j using only the first i - 1 coins
// 2. the number of ways to form j using the first i coins
// and it counts the number of ways to form j by
// (the number of ways to form j - coin in non decreasing order) + coin because
// 1. the order of addition while constructing j - coin is non-decreasing
// 2. coin is bigger or equals to the last element?
