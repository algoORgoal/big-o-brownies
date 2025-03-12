// bfs
// the cost from one position to another comes down to not only 'distance', but also the number of corners it passed.
// state: position, lastDirection, cost, countCorners
// visited: position, countCorners

class Heap {
    constructor() {
        this.heap = [];
    }
    
    get size() {
        return this.heap.length;
    }
    
    get isEmpty() {
        return this.size === 0;
    }
    
    swap(i, j) {
        [ this.heap[i], this.heap[j] ] = [ this.heap[j], this.heap[i] ]; 
    }
    
    getParent(index) {
        return Math.floor((index - 1) / 2);
    }
    
    bubbleUp() {
        let current = this.size - 1;
        while (current > 0) {
            const parent = this.getParent(current);
            if (this.heap[parent].cost < this.heap[current].cost) break;
            this.swap(current, parent);
            current = parent;
        }
    }
    
    enqueue(element) {
        this.heap.push(element);
        if (this.size > 1) this.bubbleUp();
    }
    
    getChildren(index) {
        return [ 2 * index + 1, 2 * index + 2 ];
    }
    
    bubbleDown() {
        let current = 0;
        
        
        while (current < this.size) {
            let smallest = current;
            const [ left, right ] = this.getChildren(current);
            if (left < this.size && this.heap[left].cost < this.heap[current].cost) smallest = left;
            if (right < this.size && this.heap[right].cost < this.heap[current].cost) smallest = right;
            if (smallest === current) break;
            this.swap(smallest, current);
            current = smallest;
        }
    }
    
    dequeue() {
        if (this.isEmpty) return null;
        if (this.heap.length === 1) return this.heap.pop();
        this.swap(0, this.size - 1);
        const node = this.heap.pop();
        this.bubbleDown();
        return node;
    }
}

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
        if (this.front > 0) return this.front.pop();
        while (this.back.length) {
            this.front.push(this.back.pop());
        }
        return this.front.pop();
    }
}

const isValid = (matrix, [ x, y ]) => x >= 0 && x < matrix.length && y >= 0 && y < matrix[0].length && matrix[x][y] === 0;

const up = ([ x, y ]) => [ x - 1, y ];
const down = ([ x, y ]) => [ x + 1, y ];
const left = ([ x, y ]) => [ x, y - 1 ];
const right = ([ x, y ]) => [ x, y + 1 ];

const move = (matrix, [ x, y ]) => [[ x, y - 1, 3 ], [ x, y + 1, 1, ], [ x - 1, y, 0, ], [ x + 1, y, 2, ]].filter((newPosition) => isValid(matrix, newPosition)).map((newPosition) => newPosition);

const json = (value) => JSON.stringify(value);
const parse = (value) => JSON.parse(value);

function bfs(board) {
    
    const rootState = {
        position: [ 0, 0, null ],
    }
    const rootNode = {
        ...rootState,
        cost: 0,
    }
    
    const queue = new Heap();
    queue.enqueue(rootNode);
    
    const visited = new Map();
    
    while (!queue.isEmpty) {
        const node = queue.dequeue();
        
        // console.log(node);
        
        if (visited.has(json(node.position))) {
            const previousCost = visited.get(json(node.position));
            if (previousCost <= node.cost) continue;
        }
        
        visited.set(json(node.position), node.cost);
        
        const nextPositions = move(board, node.position);
        
        nextPositions.forEach((nextPosition) => {
            const isStraight = node.position[2] === null || node.position[2] === nextPosition[2];
            const nextCost = isStraight ? node.cost + 100 : node.cost + 500 + 100;
            const nextNode = {
                position: nextPosition,
                cost: nextCost,
            };
            
            queue.enqueue(nextNode);
            
            
            
        });
    }
    
    return [ ...visited ].reduce((acc, [ key, cost ]) => {
        const position = parse(key);
        if (position[0] === board.length - 1 && position[1] === board[0].length - 1 && cost < acc) return cost;
        return acc;
    }, Infinity);
}

function solution(board) {
    return bfs(board);
}

