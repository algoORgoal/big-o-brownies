// construct a graph
// run dijkstra's algorithm instead of floyd-warshall algorithm
// dijkstra's algorithm time complexity: O((n + m)log(n))
// floyd-warshall algorithm time complexity: O(n^3)
// n <= 100_000, m <= 500_000
// Therefore, it is more efficient to choose the first algorithm

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
    
    swap(i, j) {
        [ this.heap[i], this.heap[j] ] = [ this.heap[j], this.heap[i] ];
    }
    
    getParent(index) {
        return Math.floor((index - 1) / 2);
    }
    
    getChildren(index) {
        return [ 2 * index + 1, 2 * index + 2 ];
    }
    
    bubbleUp() {
        let index = this.size - 1;
        while (index > 0) {
            const parent = this.getParent(index);
            if (this.heap[index].cost > this.heap[parent].cost) break;
            this.swap(index, parent);
            index = parent;
        }
    }
    
    enqueue(element) {
        this.heap.push(element);
        if (this.size === 1) return;
        this.bubbleUp();
    }
    
    bubbleDown() {
        let index = 0;
        while (index < this.size) {
            let minimum = index;
            const [ left, right ] = this.getChildren(index);
            if (left < this.size && this.heap[left].cost < this.heap[minimum].cost) minimum = left;
            if (right < this.size && this.heap[right].cost < this.heap[minimum].cost) minimum = right;
            
            if (minimum === index) break;
            this.swap(index, minimum);
            index = minimum;
        }
    }
    
    dequeue() {
        if (this.isEmpty) return null;
        if (this.size === 1) return this.heap.pop();
        if (this.size === 2) {
            this.swap(0, this.size - 1);
            return this.heap.pop();
        }
        this.swap(0, this.size - 1);
        const node = this.heap.pop();
        this.bubbleDown();
        return node;
    }
}

const generateGraph = (edges) => edges.reduce((accumulator, [ source, destination ]) => {
    if (!(source in accumulator)) accumulator[source] = [];
    if (!(destination in accumulator)) accumulator[destination] = [];
    accumulator[source].push(destination);
    accumulator[destination].push(source);
    return accumulator;
}, {});

function dijkstra(graph, source) {
    const priorityQueue = new PriorityQueue();
    const visited = new Set();
    
    const root = {
        node: source,
        cost: 0,
    }
    priorityQueue.enqueue(root);
    
    const distances = new Map();
    
    while (!priorityQueue.isEmpty) {
        const { node, cost } = priorityQueue.dequeue();
        if (visited.has(node)) continue;
        visited.add(node);
        distances.set(node, cost);
        
        graph[node].forEach((adjacent) => {
            priorityQueue.enqueue({
                node: adjacent,
                cost: cost + 1,
            });
        });
    }
    
    return distances;
}

const getDistancesFromSources = (distances, sources) => sources.map((source) => {
        if (distances.get(source) === 0) return 0;
        if (!distances.get(source)) return -1;
        return distances.get(source);
});
    

function solution(n, roads, sources, destination) {
    
    const graph = generateGraph(roads);
    const distances = dijkstra(graph, destination);
    const distancesFromSources = getDistancesFromSources(distances, sources);
    return distancesFromSources;
}

