function solution(rows, columns, queries) {
    
    const matrix = Array.from({ length: rows }, (_, i) => Array.from({ length: columns }, (_, j) => i * columns + j + 1));
    
    const smallestNumbers = [];
    
    queries.forEach((query) => {
        const [ x1, y1, x2, y2 ] = [ query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1 ];
        
    
        let temp = matrix[x1][y1];
        let smallestNumber = temp;
        
        for (let i = y1; i < y2; i++) {
            [ temp, matrix[x1][i + 1] ] = [ matrix[x1][i + 1], temp ];
            smallestNumber = Math.min(smallestNumber, temp);
        }
        for (let j = x1; j < x2; j++) {
            [ temp, matrix[j + 1][y2] ] = [ matrix[j + 1][y2], temp ];
            smallestNumber = Math.min(smallestNumber, temp);
        }
        for (let i = y2; i > y1; i--) {
            [ temp, matrix[x2][i - 1] ] = [ matrix[x2][i - 1], temp ];
            smallestNumber = Math.min(smallestNumber, temp);
        }
        for (let j = x2; j > x1; j--) {
            [ temp, matrix[j - 1][y1] ] = [ matrix[j - 1][y1], temp ];
            smallestNumber = Math.min(smallestNumber, temp);
        }
        smallestNumbers.push(smallestNumber);  
        
    });
    return smallestNumbers;
}