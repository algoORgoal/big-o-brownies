class Queue {
    constructor() {
        this.front = [];
        this.back = [];
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

const copyMatrix = (matrix) => [ ...matrix.map((row) => [ ...row ])];

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
    const initialState = {
        cursor: [ r, c ],
        serializedBoard: json(board),
        selected: null,
    }
    const root = {
        typingCount: 0,
        ...initialState,
    };
    const queue = new Queue();
    queue.enqueue(root);
    
    let minTypingCount = Infinity;
    const visited = new Set();
    visited.add(json(initialState));
    
    while(!queue.isEmpty) {
        const { typingCount, cursor, serializedBoard, selected } = queue.dequeue();
        const stateKey = json({ cursor, serializedBoard, selected });
        const board = parse(serializedBoard);
        const linearBoard = board.flatMap((cell) => cell);
        const [ x, y ] = cursor;
        
        if (linearBoard.every((cell) => cell === 0)) {
            minTypingCount = Math.min(minTypingCount, typingCount);
            continue;
        }
        
        const linearPosition = alignPosition(4, cursor);
        
        if (selected && board[selected[0]][selected[1]] === board[x][y] && (x !== selected[0] || y !== selected[1])) {
            const copiedBoard = copyMatrix(board);
            copiedBoard[selected[0]][selected[1]] = 0;
            copiedBoard[x][y] = 0;
            
            const nextState = {
                cursor,
                serializedBoard: json(copiedBoard),
                selected: null,
            }
            const nextStateKey = json(nextState);
            const nextNode = {
                typingCount: typingCount + 1,
                ...nextState,
            };
            if (!visited.has(nextStateKey)) {
                queue.enqueue(nextNode);
                visited.add(nextStateKey);
            }
        } else if (!selected && board[x][y]) {
            const nextState = {
                cursor,
                serializedBoard: json(board),
                selected: [ x, y ],
            }
            const nextStateKey = json(nextState);
            const nextNode = {
                typingCount: typingCount + 1,
                ...nextState,
            }
            if (!visited.has(nextStateKey)) {
                queue.enqueue(nextNode);
                visited.add(nextStateKey);
            }
        }
        
        const aroundPositions = move(board, [ x, y ]);
        const jumpedPositions = jump(board, [ x, y ]);
        [ ...aroundPositions, ...jumpedPositions ].forEach((nextCursor) => {
            const nextState = {
                cursor: nextCursor,
                serializedBoard,
                selected,
            }
            const nextStateKey = json(nextState);
            const nextNode = {
                typingCount: typingCount + 1,
                ...nextState
            };
            if (!visited.has(nextStateKey)) {
                queue.enqueue(nextNode);
                visited.add(nextStateKey);
            }
        });   
    }
    
    return minTypingCount;
}