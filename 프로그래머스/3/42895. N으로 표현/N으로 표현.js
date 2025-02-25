// (5를 n번 쓰는 경우) = (5를 n번 쓰는 경우의 집합) +  (5를 1번 쓰는 경우의 집합) +-*/ (5를 n - 1번 쓰는 경우의 집합), ..., (5를 n-1번 쓰는 경우의 집합) +-*/ (5를 1번 쓰는 경우의 집합)

function solution(N, number) {
    const dp = Array.from({ length: 9 }, () => new Map());
    for (let i = 0; i < dp.length; i++) {
        if (i === 0) {
            dp[i].set(0, 0);
            continue;
        }
        if (i === 1) {
            dp[i].set(N, 1);
            continue;
        }
        for (let j = 0; j < i; j++) {
            if (j === 0) {
                dp[i].set(Number(Array.from({ length: i }, () => String(N)).join('')), i);
                continue;
            }
            [ ...dp[j] ].forEach(([ num1, count1, ]) => {
                [ ...dp[i - j] ].forEach(([ num2, count2, ]) => {
                    const nums = [ num1 + num2, num1 - num2, num1 * num2, Math.floor(num1 / num2) ];
                    nums.forEach((newNum) => {
                        if (!dp[i].get(newNum) || dp[i].get(newNum) > count1 + count2) {
                            dp[i].set(newNum, count1 + count2);
                        }
                    })
                    
                });
            });
        }
    }
    
    let minimalCount = Infinity;
    for (let i = 0; i < dp.length; i++) {
        [ ...dp[i] ].forEach(([ num, count ]) => {
            if (num === number && count <= 8) minimalCount = Math.min(minimalCount, count);
        })
    }
    return minimalCount === Infinity ? -1 : minimalCount;
}