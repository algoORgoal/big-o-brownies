
function solution(N, number) {
    const dp = Array.from({ length: 9, }, () => new Set());
    for (let i = 1; i < dp.length; i++) {
        if (dp[i] === 1) {
            dp[i].set(N);
            continue;
        }
        dp[i].add(Number((String(N)).repeat(i)));
        for (let j = 1; j < i; j++) {
            [ ...dp[j] ].forEach((element1) => {
                [ ...dp[i - j] ].forEach((element2) => {
                    const candidates = [ element1 + element2, element1 - element2, element1 * element2, Math.floor(element1 / element2) ];
                    candidates.forEach((candidate) => {
                        if (candidate >= 1) {
                            dp[i].add(candidate);
                        }
                    });
                });
            });
        }
    }
    
    for (let i = 1; i < dp.length; i++){
        if (dp[i].has(number)) {
            return i;
        }
    }
    return -1;
}