// Find the connected components. If the neighbor has a value difference less than 4 they are in the same connncted component.
// Find the minimal value differece between neighbor connected components
// Get the sum of minimal value differences

// Running dfs or bfs to mark the connected component takes O(NM) time 
// Itering over land to find the minimal value difference between neighbor connected components takes 

// Running minimum spanning tree algorithm to for any compoennt to be reachable from other connected components

const isNodeValid = (matrix, [ x, y ]) => x >= 0 && x < matrix.length && y >= 0 && y < matrix[0].length;

const getAroundNodes = ([ x, y ]) => [[ x, y - 1 ], [ x, y + 1], [ x - 1, y ], [ x + 1, y ]];

const move = (matrix, node) => getAroundNodes(node).filter((aroundNode) => isNodeValid(matrix, aroundNode));

const json = (value) => JSON.stringify(value);
const parse = (value) => JSON.parse(value);


class PriorityQueue {
    constructor() {
        this.heap = [];
    }
    
    get size() {
        return this.heap.length;
    }
    
    get isEmpty() {
        return this.size === 0;
    }
    
    getParent(index) {
        if (index === 0) return null;
        return Math.floor((index - 1) / 2);
    }
    
    getChildren(index) {
        return [ 2 * index + 1, 2 * index + 2, ];
    }
    
    swap(i, j) {
        [ this.heap[i], this.heap[j], ] = [ this.heap[j], this.heap[i] ];
    }
    
    bubbleUp() {
        let index = this.heap.length - 1;
        
        while (index > 0) { 
            const parent = this.getParent(index);
            if (this.heap[parent].cost < this.heap[index].cost) break;
            this.swap(parent, index);
            index = parent;
        }
    }
    
    bubbleDown() {
        let index = 0;
        
        while (index < this.heap.length) {
            let minimum = index;
            const [ left, right ] = this.getChildren(index);
            if (left < this.heap.length) minimum = this.heap[minimum].cost < this.heap[left].cost ? minimum : left;
            if (right < this.heap.length) minimum = this.heap[minimum].cost < this.heap[right].cost ? minimum : right;
            if (index === minimum) break;
            this.swap(index, minimum);
            index = minimum;
        }
        
    }
    
    enqueue(element) {
        this.heap.push(element);
        if (this.heap.length === 1) {
            return;
        }
        
        this.bubbleUp();
    }
    
    dequeue() {
        if (this.isEmpty) return null;
        if (this.size === 1) return this.heap.pop();
        if (this.size === 2) {
            this.swap(0, this.heap.length - 1);
            return this.heap.pop();
        }
        
        this.swap(0, this.heap.length - 1);
        const node = this.heap.pop();
        this.bubbleDown();
        return node;
    }
}

function solution(land, height) {
    const visited = visitMatrix(land, height);
    const graph = findConnectedComponents(land, visited);
    
    return prim(graph);
}


function visitMatrix(land, height) {
    const visited = Array.from({ length: land.length, }, () => Array.from({ length: land[0].length }, () => 0));
    
    for (let i = 0; i < land.length; i++) {
        for (let j = 0; j < land[i].length; j++) {
            if (visited[i][j]) continue;
            visited[i][j] = i * land[i].length + j + 1;
            dfs(land, visited, [ i, j ], height, i * land[i].length + j + 1);
        }
    }
    
    return visited;
}


function dfs(land, visited, root, upperbound, type) {
    const stack = [ root ];
    
    while (stack.length) {
        const node = stack.pop();
        const [ x, y, ] = node;
        const neighbors = move(land, node);
        const nextNodes = neighbors.filter(([ nextX, nextY ]) => !visited[nextX][nextY] && Math.abs(land[x][y] - land[nextX][nextY]) <= upperbound);
        
        nextNodes.forEach((nextNode) => {
            const [ nextX, nextY ] = nextNode;
            if (!visited[nextX][nextY]) {
                stack.push(nextNode);
                visited[nextX][nextY] = type;
            }
        });

    }
    
    return visited;
}

function prim(graph) {    
    const priorityQueue = new PriorityQueue();
    if (Object.keys(graph).length === 0) return 0;
    const root = Number(Object.keys(graph)[0]);
    [...graph[root]].forEach(([ destination, cost ]) => {
        priorityQueue.enqueue({
            source: root,
            destination,
            cost,
        });
    });
    
    const visitedComponents = new Set([ root ]);
    
    let sum = 0;
    while (!priorityQueue.isEmpty) {
        const { source, destination, cost } = priorityQueue.dequeue();
        if (visitedComponents.has(destination)) continue;
        visitedComponents.add(destination);
        sum += cost;
        
        [...graph[destination]].forEach(([ newDestination, cost ]) => {
            if (!visitedComponents.has(newDestination)) {
                priorityQueue.enqueue({
                    source: destination,
                    destination: newDestination,
                    cost,
                });
            }
        });
    }
    
    return sum;
}

function findConnectedComponents(land, visited) {
    const graph = {};
    const types = new Set();
    for (let i = 0; i < visited.length; i++) {
        for (let j = 0; j < visited[i].length; j++) {
            types.add(json(visited[i][j]));
            const neighbors = move(land, [ i, j, ]);
            neighbors.forEach(([ x, y ]) => {
                if (visited[i][j] !== visited[x][y]) {
                    if (!graph[visited[i][j]]) graph[visited[i][j]] = new Map();
                    if (!graph[visited[x][y]]) graph[visited[x][y]] = new Map();
                    const difference = Math.abs(land[i][j] - land[x][y]);
                    if (!graph[visited[x][y]].get(visited[i][j]) || difference < graph[visited[x][y]].get(visited[i][j])) graph[visited[x][y]].set(visited[i][j], difference);
                    if (!graph[visited[i][j]].get(visited[x][y]) || difference < graph[visited[i][j]].get(visited[x][y])) graph[visited[i][j]].set(visited[x][y], difference);
                }
            })
        }
    }
    
    return graph;
}