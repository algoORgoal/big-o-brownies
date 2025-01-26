function solution(grid) {
    const visitedCells = new Set();
    const cycleLengths = [];
    
    
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            for (let k = 0; k < 4; k++) {
                const positionJson = JSON.stringify([ i, j, k ]);
                if (visitedCells.has(positionJson)) {
                    continue;
                }
            
                const stack = [ [ i, j, k, 1 ] ];
                visitedCells.add(positionJson);
                
                
                
                while (stack.length) {                    
                    const [ x, y, direction, cycleLength ] = stack.pop();                   
                    
                    let nextPosition = [];
                    
                    if (direction === 0) {
                        nextPosition = [ x === 0 ? grid.length - 1 : x - 1, y, direction ];
                    }
                    
                    if (direction === 1) {
                        nextPosition = [ x, y === grid[0].length - 1 ? 0 : y + 1, direction ];
                    }
                    
                    if (direction === 2) {
                        nextPosition = [ x === grid.length - 1 ? 0 : x + 1, y, direction ];
                    }
                    
                    if (direction === 3) {
                        nextPosition = [ x, y === 0 ? grid[0].length - 1 : y - 1, direction ];
                    }
                    
                    const [ nextX, nextY ] = nextPosition;
                    
                    if (grid[nextX][nextY] === 'S') {
                        nextPosition = [ nextX, nextY, direction ]
                    }
                    
                    if (grid[nextX][nextY] === 'L') {
                        nextPosition = [ nextX, nextY, (direction + 3) % 4 ];
                    }
                    
                    if (grid[nextX][nextY] === 'R') {
                        nextPosition = [ nextX, nextY, (direction + 1) % 4 ];
                    }
                    
                    
                    const nextPositionJson = JSON.stringify(nextPosition);
                    if (!visitedCells.has(nextPositionJson)) {
                        stack.push([ ...nextPosition, cycleLength + 1]);
                        visitedCells.add(nextPositionJson);
                    } else {
                        cycleLengths.push(cycleLength);
                    }
                }
            }        
        }
    }
    
    
    return cycleLengths.sort((a, b) => a - b);
}