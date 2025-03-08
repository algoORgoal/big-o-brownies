// 1. 위에 있는 블럭을 제거했을 때 아래 블럭이 제거 가능하다.
// 2. 아래 있는 블럭을 제거했을 때 위 블럭이 제거 가능한 경우는 존재하는가? 불가능하다.
// 왼쪽에 있는 블럭을 제거해서 오른쪽이 제거 가능 === 오른쪽에 있는 블럭을 제거해서 왼쪽이 제거 가능
// 각 줄 별로 가장 위에 있는 채워진 칸을 확인.
// 블럭 중 하나라도 가장 위에 있는 채워진 칸이 있을 경우 실패.
// 블럭의 아래 row에서 채워진 칸의 개수 > 위 row에서 채워진 칸의 개수인 경우 실패.
// 실패했을 경우 가장 위에 채워진 칸을 업데이트.
// 성공하면 개수 추가.

const move = ([ x, y ]) => ([[ x + 1, y ], [ x - 1, y ], [ x,  y + 1 ], [ x, y - 1]]);
const isValid = (board, [ x, y ], type) => x >= 0 && x < board.length && y >= 0 && y < board[x].length && board[x][y] === type;

function dfs(board, state, blocks, visited) {
    const [ x, y ] = state;
    const movedStates = move(state).filter((movedState) => isValid(board, movedState, board[x][y]) && !visited.has(movedState.toString()));
    movedStates.forEach((movedState) => {
        visited.add(movedState.toString());
        blocks.push(movedState);
        dfs(board, movedState, blocks, visited);
    });
};

function solution(board) {
    let totalCount = 0;
    
    let ltrCount = 0;
    const peaks = Array.from({ length: board[0].length }, () => Infinity);
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[i].length; j++) {
            if (board[i][j] === 0) continue;
            const blocks = [[ i, j ]];
            dfs(board, [ i, j ], blocks, new Set([ [ i, j ].toString() ]));

            const { minRow, maxRow, minColumn, maxColumn } = blocks.reduce((accumulator, [ x, y ]) => {
                accumulator.minRow = Math.min(accumulator.minRow, x);
                accumulator.maxRow = Math.max(accumulator.maxRow, x);
                accumulator.minColumn = Math.min(accumulator.minColumn, y);
                accumulator.maxColumn = Math.max(accumulator.maxColumn, y);
                return accumulator;
            }, {
                minRow: Infinity,
                maxRow: -Infinity,
                minColumn: Infinity,
                maxColumn: -Infinity,
            });

            let canFill = true;

            let previousRowCount = -Infinity;
            const emptyCells = [];
            for (let k = minRow; k <= maxRow && canFill; k++) {
                let rowCount = 0;
                for (let l = minColumn; l <= maxColumn && canFill; l++) {
                    if (board[k][l] === board[i][j]) rowCount += 1; 
                    else if (board[k][l] === 0) emptyCells.push([ k, l ]);
                    else canFill = false;

                }
                if (previousRowCount > rowCount) { // the number of elements in previous cells <= the number of elements in next cells
                    canFill = false;
                } 
                previousRowCount = rowCount;
            }

            // check if all the empty cells are apporoachable
            emptyCells.forEach(([ x, y ]) => {
                if (peaks[y] < x) canFill = false;
            })

            if (canFill) {
                for (let k = minRow; k <= maxRow; k++) {
                    for (let l = minColumn; l <= maxColumn; l++) {
                        board[k][l] = 0;
                    }
                }
                
                blocks.forEach(([ x, y ]) => {
                    if (peaks[y] === x) peaks[y] = Infinity;
                });
                
                ltrCount += 1;

            } else {
                blocks.forEach(([ x, y ]) => {
                    if (peaks[y] > x) peaks[y] = x;
                });
            }
        }
    }


    totalCount += ltrCount;
    
    for (let i = 0; i < peaks.length; i++) peaks[i] = Infinity;
    let rtlCount = 0;
    for (let i = 0; i < board.length; i++) {
        for (let j = board[i].length - 1; j >= 0; j--) {
            if (board[i][j] === 0) continue;
            const blocks = [[ i, j ]];
            dfs(board, [ i, j ], blocks, new Set([ [ i, j ].toString() ]));

            const { minRow, maxRow, minColumn, maxColumn } = blocks.reduce((accumulator, [ x, y ]) => {
                accumulator.minRow = Math.min(accumulator.minRow, x);
                accumulator.maxRow = Math.max(accumulator.maxRow, x);
                accumulator.minColumn = Math.min(accumulator.minColumn, y);
                accumulator.maxColumn = Math.max(accumulator.maxColumn, y);
                return accumulator;
            }, {
                minRow: Infinity,
                maxRow: -Infinity,
                minColumn: Infinity,
                maxColumn: -Infinity,
            });

            let canFill = true;

            let previousRowCount = -Infinity;
            const emptyCells = [];
            for (let k = minRow; k <= maxRow && canFill; k++) {
                let rowCount = 0;
                for (let l = minColumn; l <= maxColumn && canFill; l++) {
                    if (board[k][l] === board[i][j]) rowCount += 1; 
                    else if (board[k][l] === 0) emptyCells.push([ k, l ]);
                    else canFill = false;

                }
                if (previousRowCount > rowCount) { // the number of elements in previous cells <= the number of elements in next cells
                    canFill = false;
                } 
                previousRowCount = rowCount;
            }

            // check if all the empty cells are apporoachable
            emptyCells.forEach(([ x, y ]) => {
                if (peaks[y] < x) canFill = false;
            })

            if (canFill) {
                for (let k = minRow; k <= maxRow; k++) {
                    for (let l = minColumn; l <= maxColumn; l++) {
                        board[k][l] = 0;
                    }
                }
                blocks.forEach(([ x, y ]) => {
                    if (peaks[y] === x) peaks[y] = Infinity;
                });
                
                rtlCount += 1;

            } else {
                blocks.forEach(([ x, y ]) => {
                    if (peaks[y] > x) peaks[y] = x;
                });
            }
        }
    }


    totalCount += rtlCount;
    
    
    
    return totalCount;
}

