// 기둥: 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 한다.
// 보: 한쪽 끝 부분이 기둥 위에 있거나, 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 한다.
// Create a matrix and fill all the cells with -1s.
// time complexity: O(n^2 + m)
// space complexity: O(n^2 + m)


const exists = (matrix, x, y) => x >= 0 && x < matrix.length && y >= 0 && y < matrix[0].length;

const isValid = (verticalMatrix, horizontalMatrix, x, y, direction, type) => {
    if (direction === 0 && type === 0) {
        const original = verticalMatrix[x][y];
        verticalMatrix[x][y] = 0;
        const around = [[ x, y ], [ x - 1, y ], [ x + 1, y ], [ x, y - 1, ], [ x, y + 1], [ x - 1, y - 1], [ x - 1, y + 1 ], [ x + 1, y - 1], [ x + 1, y + 1 ]].flatMap(([ x, y ]) => [[ x, y, 0 ], [ x, y, 1 ]]).filter(([ x, y, direction ]) => exists(direction ? horizontalMatrix : verticalMatrix, x, y)).filter(([ x, y, direction ]) => direction ? horizontalMatrix[x][y] : verticalMatrix[x][y]);
        const isSatisfied = around.every(([ x, y, direction ]) => isValid(verticalMatrix, horizontalMatrix, x, y, direction, 1));
        verticalMatrix[x][y] = original;
        return isSatisfied;
    }
    if (direction === 0 && type === 1) {
        return x === 0 || (exists(verticalMatrix, x - 1, y) && verticalMatrix[x - 1][y]) || (exists(horizontalMatrix, x, y - 1) && horizontalMatrix[x][y - 1]) || (exists(horizontalMatrix, x, y) && horizontalMatrix[x][y]);
    }
    
    if (direction === 1 && type === 0) {
        const original = horizontalMatrix[x][y];
        horizontalMatrix[x][y] = 0;
        const around = [ [ x, y ], [ x - 1, y ], [ x + 1, y ], [ x, y - 1, ], [ x, y + 1], [ x - 1, y - 1], [ x - 1, y + 1 ], [ x + 1, y - 1], [ x + 1, y + 1 ]].flatMap(([ x, y ]) => [[ x, y, 0 ], [ x, y, 1 ]]).filter(([ x, y, direction ]) => exists(direction ? horizontalMatrix : verticalMatrix, x, y)).filter(([ x, y, direction ]) => direction ? horizontalMatrix[x][y] : verticalMatrix[x][y]);
        const isSatisfied = around.every(([ x, y, direction ]) => isValid(verticalMatrix, horizontalMatrix, x, y, direction, 1));
        horizontalMatrix[x][y] = original;
        return isSatisfied;
    }
    if (direction === 1 && type === 1) {
        return ((exists(horizontalMatrix, x, y - 1) && horizontalMatrix[x][y - 1]) && (exists(horizontalMatrix, x, y + 1) && horizontalMatrix[x][y + 1]))
        || (exists(verticalMatrix, x - 1, y) && verticalMatrix[x - 1][y]) || (exists(verticalMatrix, x - 1, y + 1) && verticalMatrix[x - 1][y + 1]);
    }
}

function solution(n, build_frame) {
    const verticalMatrix = Array.from({ length: n + 1 }, () => Array.from({ length: n + 1 }, () => 0));
    const horizontalMatrix = Array.from({ length: n + 1 }, () => Array.from({ length: n + 1 }, () => 0));
    
    for (const command of build_frame) {
        const [ y, x, direction, type ] = command;
        if (direction === 0 && isValid(verticalMatrix, horizontalMatrix, x, y, direction, type)) verticalMatrix[x][y] = type;
        if (direction === 1 && isValid(verticalMatrix, horizontalMatrix, x, y, direction, type)) horizontalMatrix[x][y] = type;
    }
    
    const validFrames = [];
    for (let i = 0; i < verticalMatrix[0].length; i++) {
        for (let j = 0; j < verticalMatrix.length; j++) {
            if (verticalMatrix[i][j]) validFrames.push([ j, i, 0 ]);
            if (horizontalMatrix[i][j]) validFrames.push([ j, i, 1 ]);
        }
    }
    
    const sortedFrames = validFrames.sort(([ x1, y1, direction1, ], [ x2, y2, direction2, ]) => x1 - x2 || y1 - y2 || direction1 - direction2);
    return sortedFrames;
}