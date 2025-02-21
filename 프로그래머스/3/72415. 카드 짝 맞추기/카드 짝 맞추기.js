class Queue {
    constructor(elements) {
        this.front = [];
        this.back = [ ...elements ];
    }
    
    get size() {
        return this.front.length + this.back.length;
    }
    
    get isEmpty() {
        return this.size === 0;
    }
    
    enqueue(element) {
        this.back.push(element);
    }
    
    dequeue() {
        if (this.isEmpty) return null;
        if (this.front.length) return this.front.pop();
        
        while (this.back.length) {
            this.front.push(this.back.pop());
        }
        return this.front.pop();
    }
}

// run bfs to find the shortest path from the initial state to the clear state
// represent the current state by using bitmask board representaiton and the current cursor

const alignPosition = (columnLength, [ x, y ]) => x * columnLength + y;

const checkValidPosition = (board, [ x, y ]) => x >= 0 && x < board.length && y >= 0 && y < board.length;

const getNearbyPositions = ([ x, y ]) => [[ x + 1, y ], [ x - 1, y ], [ x, y + 1], [ x, y - 1]];

const move = (board, [ x, y ]) => getNearbyPositions([ x, y ]).filter((position) => checkValidPosition(board, position));

const copyMatrix = (matrix) => matrix.map((row) => [ ...row ]);

const checkPositionSame = ([ x1, y1, ], [ x2, y2 ]) => x1 === x2 && y1 === y2; 

const jump = (board, [ x, y ]) => {
    const positions = [];
    for (let i = x + 1; i < board.length; i++) {
        if (board[i][y] !== 0 || i === board.length - 1) {
            positions.push([ i, y ]);
            break;
        }
    }
    for (let i = x - 1; i >= 0; i--) {
        if (board[i][y] !== 0 || i === 0) {
            positions.push([ i, y ]);
            break;
        }   
    }
    for (let i = y + 1; i < board[0].length; i++) {
        if (board[x][i] !== 0 || i === board[0].length - 1) {
            positions.push([ x, i ]);
            break;
        }   
    }
    for (let i = y - 1; i >= 0; i--) {
        if (board[x][i] !== 0 || i === 0) {
            positions.push([ x, i ])
            break;
        }   
    }
    return positions;
}

const json = (value) => JSON.stringify(value);
const parse = (value) => JSON.parse(value);

function solution(board, r, c) {   
    const initialStateJson = json({
        cursor: [ r, c ],
        board,
        selected: null,
    });
    const root = {
        cost: 0,
        stateJson: initialStateJson,
    };
    const queue = new Queue([ root ]);
    const visited = new Set([ initialStateJson ]);
    
    let minCost = Infinity;

    while(!queue.isEmpty) {
        const { cost, stateJson } = queue.dequeue();
        const { cursor, board, selected, } = parse(stateJson);
        const [ x, y ] = cursor;
        
        if (board.flat().every((cell) => cell === 0)) {
            minCost = Math.min(minCost, cost);
            continue;
        }
        
        const around = move(board, cursor);
        const jumps = jump(board, cursor);
        [ ...around, ...jumps ].forEach((next) => {
            const nextStateJson = json({
                cursor: next,
                board,
                selected,
            })
            const nextNode = {
                cost: cost + 1,
                stateJson: nextStateJson,
            };
            if (!visited.has(nextStateJson)) {
                queue.enqueue(nextNode);
                visited.add(nextStateJson);
            }
        });
        
        if (selected && !checkPositionSame(cursor, selected)) {
            const [ x1, y1 ] = cursor;
            const [ x2, y2 ] = selected;
            if (board[x1][y1] === board[x2][y2]) {
                const newBoard = copyMatrix(board);
                newBoard[x1][y1] = 0;
                newBoard[x2][y2] = 0;
                const nextStateJson = json({
                    cursor,
                    board: newBoard,
                    selected: null,
                });
                const nextNode = {
                    cost: cost + 1,
                    stateJson: nextStateJson,
                };
                if (!visited.has(nextStateJson)) {
                    queue.enqueue(nextNode);
                    visited.add(nextStateJson);
                }
            }
            
        }
        
        if (!selected && board[x][y]) {
            const nextStateJson = json({
                cursor,
                board: board,
                selected: [ x, y ],
            });
            const nextNode = {
                cost: cost + 1,
                stateJson: nextStateJson,
            }
            if (!visited.has(nextStateJson)) {
                queue.enqueue(nextNode);
                visited.add(nextStateJson);
            }
        }
    }
    
    return minCost;
}