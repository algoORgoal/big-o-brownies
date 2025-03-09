const isValid = (matrix, x, y) => x >= 0 && x < matrix.length && y >= 0 && y < matrix[0].length;

function isCommandValid(matrices, position) {
    const [ verticalMatrix, horizontalMatrix ] = matrices;
    const [ x, y ] = position;
    for (let i = x - 1; i <= x + 1; i++) {
        for (let j = y - 1; j <= y + 1; j++) {
            if (isValid(verticalMatrix, i, j) && verticalMatrix[i][j]) {
                const isVerticalValid = 
                i === 0 
                || (isValid(horizontalMatrix, i, j - 1) && horizontalMatrix[i][j - 1])
                || (isValid(horizontalMatrix, i, j) && horizontalMatrix[i][j])
                || (isValid(verticalMatrix, i - 1, j) && verticalMatrix[i - 1][j]);
                if (!isVerticalValid) return false;
            }
            if (isValid(horizontalMatrix, i, j) && horizontalMatrix[i][j]) {
                const isHorizontalValid = 
                isValid(verticalMatrix, i - 1, j) && verticalMatrix[i - 1][j]
                || isValid(verticalMatrix, i - 1, j + 1) && verticalMatrix[i - 1][j + 1]
                || (isValid(horizontalMatrix, i, j - 1) && horizontalMatrix[i][j - 1]
                && isValid(horizontalMatrix, i, j + 1) && horizontalMatrix[i][j + 1]);
                if (!isHorizontalValid) return false;
            }
        }
    }
    
    return true;
}


function solution(n, commands) {
    const verticalMatrix = Array.from({ length: n + 1 }, () => Array.from({ length: n + 1 }, () =>0));
    const horizontalMatrix = Array.from({ length: n + 1 }, () => Array.from({ length: n + 1, }, () => 0));
    commands.forEach(([ y, x, direction, type ]) => {
        if (direction === 0) {
            verticalMatrix[x][y] = type;
            if (!isCommandValid([ verticalMatrix, horizontalMatrix ], [ x, y ])) verticalMatrix[x][y] ^= 1;
        } else {
            horizontalMatrix[x][y] = type;
            if (!isCommandValid([ verticalMatrix, horizontalMatrix ], [ x, y ])) horizontalMatrix[x][y] ^= 1;
        }
    });
        
    
    const frames = [];
    for (let i = 0; i < verticalMatrix.length; i++) { 
        for (let j = 0; j < verticalMatrix[0].length; j++) {
            if (verticalMatrix[i][j]) frames.push([ j, i, 0 ]);
            if (horizontalMatrix[i][j]) frames.push([ j, i, 1 ]);
        }
    }
    
    return frames.sort(([ x1, y1, direction1, ], [ x2, y2, direction2 ]) => x1 - x2 || y1 - y2 || direction1 - direction2);
}