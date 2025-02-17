const json = (value) => JSON.stringify(value);

function solution(n, results) {
    const matches = results.reduce((matches, [ source, destination ]) => {
        matches.add(json([ source, destination ]));
        return matches;
    }, new Set());
    
    const dp = Array.from({ length: n + 1 }, () => Array.from({ length: n + 1 }, () => 0));
    for (let k = 0; k <= n; k++) {
        for (let i = 1; i <= n; i++) {
            for (let j = 1; j <= n; j++) {
                if (k === 0 && matches.has(json([ i, j, ]))) {
                    dp[i][j] = 1;
                    continue;
                }
                dp[i][j] = dp[i][j] || (dp[i][k] && dp[k][j]);
            }
        }
    }
    
    let count = 0;
    for (let i = 1; i <= n; i++) {
        if (dp[i].every((element, j) => j === 0 || j === i || dp[i][j] === 1 || dp[j][i] === 1)) {
            count += 1;
        }
    }
    return count;
}

