function bfs(source, destination, walls, rowCount, columnCount) {
    const queue = [[ source, 0 ]];
    
    let distanceToLever = Infinity;
    
    const visitedPositions = new Set();

    while(queue.length > 0) {
        const [ position, distance ] = queue.shift();
        const [ x, y ] = position;
        
        if (x === destination[0] && y === destination[1]) {
            distanceToLever = distance;
            break;
        }
        const validPositions = []
        if (x > 0) {
            validPositions.push([ x - 1, y]);
        }
        if (x < rowCount - 1) {
            validPositions.push([ x + 1, y ]);
        }
        if (y > 0) {
            validPositions.push([ x, y - 1 ]);
        }
        if (y < columnCount - 1) {
            validPositions.push([ x, y + 1 ]);
        }
        const nextPositions = validPositions.filter((position) => !walls.has(JSON.stringify(position)) && !visitedPositions.has(JSON.stringify(position)));
        queue.push(...nextPositions.map((position) => [ position, distance + 1]));
        nextPositions.forEach((nextPosition) => {
            visitedPositions.add(JSON.stringify(nextPosition));
        })
    }   
    
    return distanceToLever;
}

function solution(maps) {
    let start, exit, lever;
    const walls = new Set();
    maps.forEach((rowStr, i) => {
        const row = rowStr.split('');
        row.forEach((block, j) => {
            if (block === 'S') {
                start = [ i, j ];
            } else if (block === 'L') {
                lever = [ i, j ];
            } else if (block === 'E') {
                exit = [ i, j ];
            } else if (block === 'X') {
                walls.add(JSON.stringify([ i, j ]));
            }
        });
    });
    
    const [ rowCount, columnCount ] = [ maps.length, maps[0].length ];
    
//     const queue = [[ start, 0 ]];
    
//     let distanceToLever = Infinity;
    
//     const visitedPositions = new Set();

//     while(queue.length > 0) {
//         const [ position, distance ] = queue.shift();
//         const [ x, y ] = position;
        
//         if (x === lever[0] && y === lever[1]) {
//             distanceToLever = distance;
//             break;
//         }
//         const validPositions = []
//         if (x > 0) {
//             validPositions.push([ x - 1, y]);
//         }
//         if (x < rowCount - 1) {
//             validPositions.push([ x + 1, y ]);
//         }
//         if (y > 0) {
//             validPositions.push([ x, y - 1 ]);
//         }
//         if (y < columnCount - 1) {
//             validPositions.push([ x, y + 1 ]);
//         }
//         const nextPositions = validPositions.filter((position) => !walls.has(JSON.stringify(position)) && !visitedPositions.has(JSON.stringify(position)));
//         queue.push(...nextPositions.map((position) => [ position, distance + 1]));
//     }
    const distanceToLever = bfs(start, lever, walls, rowCount, columnCount);
    const distanceToExit = bfs(lever, exit, walls, rowCount, columnCount);
    const totalDistance = distanceToLever + distanceToExit;
    if (totalDistance === Infinity) {
        return -1;
    }
    return totalDistance;
    
}