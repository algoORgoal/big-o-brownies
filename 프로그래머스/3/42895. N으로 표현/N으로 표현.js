// (5를 n번 쓰는 경우) = (5를 n번 쓰는 경우의 집합) +  (5를 1번 쓰는 경우의 집합) +-*/ (5를 n - 1번 쓰는 경우의 집합), ..., (5를 n-1번 쓰는 경우의 집합) +-*/ (5를 1번 쓰는 경우의 집합)
// 시간 복잡도: O(n^3) (각 항마다 n^2의 시간이 걸리고, n번 반복)
// 공간 복잡도: O(n^2) (숫자 개수 * 2)

function solution(N, number) {
    const dp = Array.from({ length: 9 }, () => new Set());
    for (let i = 0; i < dp.length; i++) {
        if (i === 0) {
            dp[i].add(0);
            if (dp[i].has(number)) return i;
            continue;
        }
        if (i === 1) {
            dp[i].add(N);
            if (dp[i].has(number)) return i;
            continue;
        }
        dp[i].add(Number(String(N).repeat(i)));
        for (let j = 1; j < i; j++) {
            [ ...dp[j] ].forEach((num1) => {
                [ ...dp[i - j] ].forEach((num2) => {
                    const nums = [ num1 + num2, num1 - num2, num1 * num2 ].concat(num2 !== 0 ? Math.floor(num1 / num2) : []).filter((newNum) => newNum !== 0)
                    nums.forEach((newNum) => {
                        dp[i].add(newNum);
                    })
                });
            });
        }
        if (dp[i].has(number)) return i;
    }
    
    return -1;
}