// Represent the relative magnitude as a directed graph.
// if A beats B, there is an edge from A to B.
// if A beats B and B beats C, there is a path from A to C.
// if A is ranked higher than B and B is ranked higher than C, there is a path from A to C.
// if there is not path from A to C, the relationship is not clear.
// Run floyd-warshall algorithm to check if there is a path from node i to j.
// if i has path from i to k or k to i, for 1<=k<=n(k!=i), we can clear set the order of the node. Otherwise, it's impossible.
// So check dp[i][k] || dp[k][i] for every k except j. If so, add count to 1.
// Time complexity: O(n^3) 
// Space complexity: O(n^2) 

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

