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
        
        if (this.front.length) {
            return this.front.pop();
        }
        
        while (this.back.length) {
            this.front.push(this.back.pop());
        }
        
        return this.front.pop();
    }
}

const getAllAroundPositions = ([ x, y ]) => [
    [ x - 1, y ],
    [ x + 1, y ],
    [ x, y - 1],
    [ x, y + 1 ],
    [ x - 1, y - 1],
    [ x - 1, y + 1 ],
    [ x + 1, y - 1],
    [ x + 1, y + 1]
];

const getNearbyPositions = ([ x, y ]) => [
    [ x - 1, y ],
    [ x + 1, y ],
    [ x, y - 1 ],
    [ x, y + 1 ],
]

const checkValidPosition = (board, [ x, y ]) => x >= 0 && x < board.length && y >= 0 && y < board[0].length;

const getValidAllAroundPositions = (board, position) => getAllAroundPositions(position).filter((position) => checkValidPosition(board, position));

const getValidNearbyPositions = (board, position) => getNearbyPositions(position).filter((position) => checkValidPosition(board, position));

const Json = (value) => JSON.stringify(value);

function solution(rectangles, characterX, characterY, itemX, itemY) {
    const board = Array.from({ length: 102, }, () => Array.from({ length: 102 }, () => 0));
    
    rectangles.forEach(([ x1, y1, x2, y2 ]) => {
        for (let i = 2 * Math.min(x1, x2); i <= 2 * Math.max(x1, x2); i++) {
            for (let j = 2 * Math.min(y1, y2); j <= 2 * Math.max(y1, y2); j++) {
                board[i][j] = 1;
            }
        }
    });
    
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j <= board[0].length; j++) {
            if (board[i][j] === 0) continue;
            const positions = getValidAllAroundPositions(board, [ i, j ]);
            // if (positions.every(([ x, y ]) => board[x][y] === 1)) continue;
            if (positions.some(([ x, y ]) => board[x][y] === 0)) {
                board[i][j] = 2;
            }
        }
    }
    
    const queue = new Queue();
    const root = {
        node: [ 2 * characterX, 2 * characterY ],
        distance: 0,
    }
    queue.enqueue(root);
    
    let shortestDistance = Infinity;
    const visited = new Set();
    visited.add(Json([ 2 * characterX, 2 * characterY ]));
    
    while (!queue.isEmpty) {
        const { node, distance } = queue.dequeue();
        const [ x, y ] = node;
        
        if (x === itemX * 2 && y === itemY * 2) {
            shortestDistance = Math.min(shortestDistance, distance);
            return shortestDistance / 2;
        }
        
        const positions = getValidNearbyPositions(board, node).filter(([ x, y ]) => board[x][y] === 2 && !visited.has(Json([ x, y ])));
        
        
        positions.forEach(([ neighborX, neighborY ]) => {
            queue.enqueue({
                node: [ neighborX, neighborY ],
                distance: distance + 1,
            });
            visited.add(Json([ neighborX, neighborY ]));
        });
    }
}