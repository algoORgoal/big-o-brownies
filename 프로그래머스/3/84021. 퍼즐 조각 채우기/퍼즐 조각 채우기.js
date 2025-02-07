const checkReachable = (matrix, [ x, y ]) => {
    if (x < 0) return false;
    if (y < 0) return false;
    if (x >= matrix.length) return false;
    if (y >= matrix[0].length) return false;
    return true;
}

const getRelativePositions = (positions) => {
    if (positions.length === 0) return positions;
    
    const [ minX, minY ] = [ Math.min(...positions.map((position) => position[0])), Math.min(...positions.map((position) => position[1])) ];
    return positions.map(([ x, y ]) => [x - minX, y - minY]);
}

const getTargetPositions = (matrix, positions, target) => positions.filter(([ x, y ]) => matrix[x][y] === target);

const getEmptyPositions = (matrix, set, position) => {
    const [ x, y ] = position;
    const nearbyPositions = [[ x - 1, y ], [ x + 1, y ], [ x, y - 1 ], [ x, y + 1 ]].filter((position) => checkReachable(matrix, position));
    const unvisitedNearbyPositions = nearbyPositions.filter((position) => !set.has(JSON.stringify(position)));
    unvisitedNearbyPositions.forEach((position) => set.add(JSON.stringify(position)));
    const targetPositions = getTargetPositions(matrix, unvisitedNearbyPositions, 0);
    return targetPositions;
}

const getBlockPositions = (matrix, set, position, target) => {
    const [ x, y ] = position;
    const nearbyPositions = [[ x - 1, y ], [ x + 1, y ], [ x, y - 1 ], [ x, y + 1 ]].filter((position) => checkReachable(matrix, position));
    const unvisitedNearbyPositions = nearbyPositions.filter((position) => !set.has(JSON.stringify(position)));
    unvisitedNearbyPositions.forEach((position) => set.add(JSON.stringify(position)));
    const targetPositions = getTargetPositions(matrix, unvisitedNearbyPositions, target);
    return targetPositions;
}

function getBlocks(matrix, target) {
    const visited = new Set();

    const blocks = [];
    
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            const root = [ i, j ];
            const positionJson = JSON.stringify(root);
            
            if (visited.has(positionJson) || matrix[i][j] !== target) continue;
            
            
            visited.add(positionJson) 
            const stack = [ root ];
            const block = [];
            while (stack.length) {
                const [ x, y ] = stack.pop();
                block.push([ x, y ]);
                const positions = getBlockPositions(matrix, visited, [ x, y ], target);
                stack.push(...positions);
            }
            blocks.push(getRelativePositions(block));
        }
    }
    
    return blocks;
    
}



const rotatePosition = ([ x, y ]) => [ -y , x ];


function solution(gameBoard, table) {
    const emptyBlocks = getBlocks(gameBoard, 0);
    const pieces = getBlocks(table, 1);
    
    const sortedEmptyBlocks = emptyBlocks.map((emptyBlock) => emptyBlock.sort(([ x1, y1 ], [ x2, y2 ]) => x1 !== x2 ? x1 - x2 : y1 - y2));
    const sortedRotatedPieces = pieces.map((piece) => {
        const piece1 = piece.sort(([ x1, y1 ], [ x2, y2 ]) => x1 !== x2 ? x1 - x2 : y1 - y2);
        const piece2 = getRelativePositions(piece1.map(rotatePosition)).sort(([ x1, y1 ], [ x2, y2 ]) => x1 !== x2 ? x1 - x2 : y1 - y2);
        const piece3 = getRelativePositions(piece2.map(rotatePosition)).sort(([ x1, y1 ], [ x2, y2 ]) => x1 !== x2 ? x1 - x2 : y1 - y2);
        const piece4 = getRelativePositions(piece3.map(rotatePosition)).sort(([ x1, y1 ], [ x2, y2 ]) => x1 !== x2 ? x1 - x2 : y1 - y2);
        return [ piece1, piece2, piece3, piece4 ];
    });
    
    let fittableCount = 0;
    const fitBlock = new Set();
    const usedPieces = new Set();
    
    for (let i = 0; i < sortedEmptyBlocks.length; i++){
        const emptyBlock = sortedEmptyBlocks[i];
        for (let j = 0; j < sortedRotatedPieces.length; j++) {
            if (fitBlock.has(i)) break;
            if (usedPieces.has(j)) continue;
            if (emptyBlock.length !== sortedRotatedPieces[j][0].length) continue;
            for (let k = 0; k < sortedRotatedPieces[j].length; k++) {
                if (fitBlock.has(i)) break;
                if (usedPieces.has(j)) break;
                const piece = sortedRotatedPieces[j][k];
                const canFitIn = emptyBlock.every((_, index) => emptyBlock[index][0] === piece[index][0] && emptyBlock[index][1] === piece[index][1]);
                if (canFitIn) {
                    fittableCount += emptyBlock.length;
                    fitBlock.add(i);
                    usedPieces.add(j);
                }
            }
            
        }
    }
    return fittableCount;
}
        
