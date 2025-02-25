// (5를 n번 쓰는 경우) = (5를 n번 쓰는 경우의 집합) +  (5를 1번 쓰는 경우의 집합) +-*/ (5를 n - 1번 쓰는 경우의 집합), ..., (5를 n-1번 쓰는 경우의 집합) +-*/ (5를 1번 쓰는 경우의 집합)

function solution(N, number) {
    const dp = Array.from({ length: 9 }, () => new Set());
    for (let i = 0; i < dp.length; i++) {
        if (i === 0) {
            dp[i].add(0);
            continue;
        }
        if (i === 1) {
            dp[i].add(N);
            continue;
        }
        for (let j = 0; j < i; j++) {
            if (j === 0) {
                dp[i].add(Number(Array.from({ length: i }, () => String(N)).join('')), i);
                continue;
            }
            [ ...dp[j] ].forEach((num1) => {
                [ ...dp[i - j] ].forEach((num2) => {
                    const nums = [ num1 + num2, num1 - num2, num1 * num2, Math.floor(num1 / num2) ].filter((num) => num !== 0);
                    nums.forEach((newNum) => {
                        dp[i].add(newNum);
                    })
                });
            });
        }
    }
    
    let minimalCount = Infinity;
    for (let i = 0; i < dp.length; i++) {
        if (dp[i].has(number)) {
                minimalCount = Math.min(minimalCount, i);
        }
    }
    return minimalCount === Infinity ? -1 : minimalCount;
}