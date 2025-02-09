function solution(matrix_sizes) {
    
    const array = matrix_sizes.reduce((accumulator, [ row, column ], index) => {
        if (index === 0) {
            accumulator.push(row, column);
            return accumulator;
        }
        accumulator.push(column);
        return accumulator;
    }, []);
    
    
    const cache = Array.from({ length: array.length }, () => Array.from({ length: array.length }, () => Infinity));
    
    for (let i = 0; i < cache.length - 1; i++) {
        cache[i][i + 1] = 0;
    }
    
    
    for (let len = 2; len < array.length; len++) {          
        for (let i = 0; i < array.length - len; i++) {
            let j = i + len;
            for (let k = i + 1; k < j; k++) {
                cache[i][j] = Math.min(
                    cache[i][j],
                    cache[i][k] + cache[k][j] + array[i] * array[k] * array[j]
                );
            }
        }
    }
    
    return cache[0][array.length - 1];
    
    
    // for (let i = 2; i < cache.length; i++) {
    //     for (let j = i; j < cache[0].length - 1; j++) {
    //         if (i === j) {
    //             cache[i][j] = array[i - 1] * array[i] * array[i + 1];
    //             continue;
    //         }
    //         for (let k = i + 1; k < j; k++) {
    //             console.log(i, j, cache[i][j], );
    //             cache[i][j] = Math.min(cache[i][j], cache[i][k] + cache[k][j] + array[i] * array[k] * array[j]);
    //         }
    //     }
    // }
    console.log(cache);
}


// 14 58
//  k k+1

// dp[i][j] = dp[i][k] + dp[k+1][j] + cost[i][k]