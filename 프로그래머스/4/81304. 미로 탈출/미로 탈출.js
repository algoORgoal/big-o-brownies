// 함정의 활성화/비활성화 상태를 비트맵으로 관리한다.
// 함정이 엣지의 방향을 전환시키기 때문에, 노드뿐만 아니라 함정상태까지 같이 저장하여 재방문할 수 있도록 한다.
// 가능한 상태의 개수: 2 ** 10 * 1000
// 시간복잡도: O((n * 2^10 + m)log(n * 2^10))
// 공간복잡도: O(n * 2^10 + m)

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
        return Math.floor((index - 1) / 2);
    }
    
    getChildren(index) {
        return [ 2 * index + 1, 2 * index + 2 ];
    }
    
    swap(i, j) {
        [ this.heap[i], this.heap[j] ] = [ this.heap[j], this.heap[i] ];
    }
    
    bubbleUp() {
        let current = this.heap.length - 1;
        while (current > 0) {
            const parent = this.getParent(current);
            if (this.heap[current].cost > this.heap[parent].cost) break;
            this.swap(current, parent);
            current = parent;
        }
    }
    
    insert(node) {
        this.heap.push(node);
        if (this.size === 1) return;
        this.bubbleUp();
    }
    
    bubbleDown() {
        let current = 0;
        while (current < this.heap.length) {
            let smallest = current;
            const [ left, right ] = this.getChildren(current);
            if (left < this.heap.length && this.heap[smallest].cost > this.heap[left].cost) {
                smallest = left;
            }
            if (right < this.heap.length && this.heap[smallest].cost > this.heap[right].cost) {
                smallest = right;
            }
            if (smallest === current) break;
            this.swap(current, smallest);
            current = smallest;
        }
    }
    
    delete() {
        if (this.isEmpty) return null;
        if (this.size === 1) return this.heap.pop();
        this.swap(0, this.heap.length - 1);
        const node = this.heap.pop();
        this.bubbleDown();
        return node;
    }
}

const generateGraph = (roads) => roads.reduce((accumulator, [ source, destination, cost ]) => {
    if (!(source in accumulator)) accumulator[source] = [];
    if (!(destination in accumulator)) accumulator[destination] = [];
    accumulator[source].push({ adjacent: destination, cost, isOriginal: true });
    accumulator[destination].push({ adjacent: source, cost, isOriginal: false });
    return accumulator;
}, {})

function solution(n, start, end, roads, traps) {
    const graph = generateGraph(roads);
    return dijkstra(start, end, graph, traps);
}

const json = (value) => JSON.stringify(value);
const parse = (value) => JSON.parse(value);

const checkTraversable = (graph, edge, trapBitmap, trapIndices) => {
    const isSourceReversed = edge.source in trapIndices && Boolean(trapBitmap & (1 << trapIndices[edge.source]));
    const isDestinationReversed = edge.destination in trapIndices && Boolean((trapBitmap & (1 << trapIndices[edge.destination])));
    const isReversed = isSourceReversed !== isDestinationReversed;
    if (edge.isOriginal && isReversed) return false;
    if (edge.isOriginal && !isReversed) return true;
    if (!edge.isOriginal && isReversed) return true;
    if (!edge.isOrignal && !isReversed) return false;
    throw new Error("source and reserved don't match")
}

function dijkstra(source, destination, graph, traps) {
    const trapIndices = traps.reduce((accumulator, trap, index) => {
        accumulator[trap] = index;
        return accumulator;
    }, {});
    const initialState = {
        value: source,
        trapBitmap: 0,
    };
    const initialNode = {
        ...initialState,
        cost: 0,
    };
    const visited = new Map();
    const priorityQueue = new PriorityQueue();
    priorityQueue.insert(initialNode);
    
    while (!priorityQueue.isEmpty) {
        const { value, trapBitmap, cost, } = priorityQueue.delete();
        
        const key = json({ value, trapBitmap });
        if (visited.has(key)) continue;
        visited.set(key, cost);
        
        if (value === destination) {
            return cost;
        }
        
        graph[value].forEach(({ adjacent, cost: newCost, isOriginal }) => {
            const isTraversable = checkTraversable(graph, { source: value, destination: adjacent, isOriginal }, trapBitmap, trapIndices);
            if (isTraversable) {
                const isAdjacentTrap = adjacent in trapIndices;
                const newTrapBitmap = isAdjacentTrap ? trapBitmap ^ (1 << trapIndices[adjacent]) : trapBitmap;
                const newState = { value: adjacent, trapBitmap: newTrapBitmap };
                
                const newKey = json(newState);
                if (!visited.has(newKey)) {
                    priorityQueue.insert({ ...newState, cost: cost + newCost, });
                }
            }
        });
    }
    
    return -1;
}