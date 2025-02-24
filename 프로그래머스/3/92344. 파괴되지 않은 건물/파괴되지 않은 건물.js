// 1. Create an array for marking the beginning and the end of the range
// 2. When it is addition, add value to the beggining and subtract the end with the value
// 3. Calculate the prefix sum from left to right
// 4. Calculate the prefix sum from the top to the bottom

function solution(board, skill) {
    const prefixSum = Array.from({ length: board.length }, () => Array.from({ length: board[0].length }, () => 0));
    
    for (let i = 0; i < skill.length; i++) {
        const [ type, r1, c1, r2, c2, degree, ] = skill[i];
        const adjustment = type === 1 ? degree * (-1) : degree;
        
        prefixSum[r1][c1] += adjustment;
        if (c2 + 1 < prefixSum[0].length) prefixSum[r1][c2 + 1] -= adjustment;
        if (r2 + 1 < prefixSum.length) prefixSum[r2 + 1][c1] -= adjustment;
        if (r2 + 1 < prefixSum.length && c2 + 1 < prefixSum[0].length) prefixSum[r2 + 1][c2 + 1] += adjustment;
    }
    
    for (let i = 0; i < prefixSum.length; i++) {
        for (let j = 1; j < prefixSum[0].length; j++) {
            prefixSum[i][j] += prefixSum[i][j - 1];
        }
    }
    
    for (let i = 1; i < prefixSum.length; i++) {
        for (let j = 0; j < prefixSum[0].length; j++) {
            prefixSum[i][j] += prefixSum[i - 1][j];
        }
    }
    
    let count = 0;
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            board[i][j] += prefixSum[i][j];
            if (board[i][j] > 0) {
                count += 1;
            }
        }
    }
    
    return count;
}