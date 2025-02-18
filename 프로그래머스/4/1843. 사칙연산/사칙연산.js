// (1) dp[i][i] = arr[i]
// (2) dp[i][i + 1] = op[i](arr[i], arr[i + 1]) (i < arr.length - 1)
// (3) dp[i][j] = op[i](dp[i] ,dp[i + 1][j]), op[j - 1](dp[j], dp[i][j - 1]) (j = i + len - 1)
// time complexity: O(n^2) (the number of operands)
// space complexity: O(n^2)

function solution(arr) {
    const { operands, operators } = arr.reduce((accumulator, token) => {
        if (token === '+' || token === '-') {
            accumulator.operators.push(token);
            return accumulator;
        }
        accumulator.operands.push(Number(token));
        return accumulator;
    }, {
        operands: [],
        operators: []
    });
    const dp = Array.from({ length: operands.length }, () => Array.from({ length: operands.length }, () => [ -Infinity, Infinity ]));    
    
    for (let len = 1; len <= dp.length; len++) {
       for (let i = 0; i < dp.length; i++) {
           const j = i + len - 1;
           if (j >= dp.length) continue;
           if (i === j) {
               dp[i][j] = [ operands[i], operands[i], ];
               continue;
           }
           for (let k = i; k < j; k++) {
               const candidate1 = operators[k] === '+' ? dp[i][k][0] + dp[k + 1][j][0] : dp[i][k][0] - dp[k + 1][j][1];
               const candidate2 = operators[k] === '+' ? dp[i][k][1] + dp[k + 1][j][1] : dp[i][k][1] - dp[k + 1][j][0];
               dp[i][j] = [ Math.max(candidate1, dp[i][j][0]), Math.min(candidate2, dp[i][j][1])] 
           }
//            const candidate1 = operators[i] === '+' ? dp[i][i][0] + dp[i + 1][j][0] : dp[i][i][0] - dp[i + 1][j][1];
//            const candidate2 = operators[j - 1] === '+' ? dp[i][j - 1][0] + dp[j][j][0] : dp[i][j - 1][0] - dp[j][j][1];
           
        
//            const candidate3 = operators[i] === '+' ? dp[i][i][1] + dp[i + 1][j][1] : dp[i][i][1] - dp[i + 1][j][1][0];
//            const candidate4 = operators[j - 1] === '+' ? dp[i][j - 1][1] + dp[j][j][1] : dp[i][j - 1][1] - dp[j][j][0];
//            dp[i][j] = [ Math.max(candidate1, candidate2), Math.min(candidate3, candidate4) ];
       }
    }
    
    console.log(dp)
    return dp[0][dp.length - 1][0];
}