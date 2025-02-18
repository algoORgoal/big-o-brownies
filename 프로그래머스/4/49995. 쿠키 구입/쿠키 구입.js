// calculate prefix sum and postfix sum
// for each [i][i + 1], check prefix[m] - prefix[l] === postfix[m + 1] - postfix[r] and check the maximal value

const getPrefixSum = (array) => array.reduce((accumulator, cookie, index) => {
        if (index === 0) {
            accumulator.push(cookie);
            return accumulator;
        }
        const prefixSum = accumulator[accumulator.length - 1];
        accumulator.push(prefixSum + cookie);
        return accumulator;
    }, []);

function solution(cookies) {
    const prefixSum = getPrefixSum(cookies);
    const postfixSum = getPrefixSum([ ...cookies ].reverse()).reverse();
    
    let maxSum = 0;
    
    for (let m = 0; m < cookies.length - 1; m++) {
        let [ l, r ] = [ m, m + 1 ];
        while (l >= 0 && r < cookies.length) {
            const leftSum = prefixSum[m] - (l - 1 >= 0 ? prefixSum[l - 1] : 0);
            const rightSum = postfixSum[m + 1] - (r + 1 < cookies.length ? postfixSum[r + 1] : 0);
            if (leftSum === rightSum) {
                maxSum = Math.max(maxSum, leftSum);
                l -= 1;
                r += 1;
            }
            if (leftSum < rightSum) {
                l -= 1;
            }
            if (leftSum > rightSum) {
                r += 1;
            }
        }
    }    
    return maxSum;
}