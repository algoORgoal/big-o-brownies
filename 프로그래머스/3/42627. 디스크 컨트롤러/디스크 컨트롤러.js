// store turnaround time, createdAt, and index in priority queue
// While iterating over time:
//   Initialize the current job if now === createdAt + turnaroudtime
//   Enqueue a job in the priority queue if now === createdAt
//   Dequeue a new job and set now to it when current job !== null

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
    
    compare(node1, node2) {
        if (node1.turnaround - node2.turnaround < 0) return true;
        if (node1.turnaround - node2.turnaround === 0 && node1.createdAt - node2.createdAt < 0) return true;
        if (node1.turnaround - node2.turnaround === 0 && node1.createdAt - node2.createdAt === 0 && node1.index - node2.index < 0) return true;
        return false;
    }
    
    bubbleUp() {
        let index = this.size - 1;
        
        while (index > 0) {
            const parent = this.getParent(index);
            if (this.compare(this.heap[parent], this.heap[index])) break;
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
            if (left < this.size && this.compare(this.heap[left], this.heap[minimum])) minimum = left;
            if (right < this.size && this.compare(this.heap[right], this.heap[minimum])) minimum = right;
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

function solution(jobs) {
    const requests = jobs.map(([ createdAt, turnaround, ], index) => ({
        turnaround,
        createdAt,
        index
    }));
    
    const sortedRequests = requests.sort(({ createdAt: createdAt1 }, { createdAt: createdAt2 }) => createdAt1 - createdAt2);
    const priorityQueue = new PriorityQueue();
    
    let upcomingRequestIndex = 0;
    let currentRequest = null;
    let averageTimeLapse = 0;
    
    for (let now = 0; now < 1_000_0000; now++) {
        if (currentRequest && currentRequest.turnaround === 0) {
            averageTimeLapse += (now - currentRequest.createdAt);
            currentRequest = null;
        };
        while (upcomingRequestIndex < sortedRequests.length && sortedRequests[upcomingRequestIndex].createdAt === now) {
            priorityQueue.enqueue(sortedRequests[upcomingRequestIndex]);
            upcomingRequestIndex += 1;
        }
        if (!currentRequest && !priorityQueue.isEmpty) {
            currentRequest = priorityQueue.dequeue();
        }
        if (currentRequest) currentRequest.turnaround -= 1;
        
    }
    
    averageTimeLapse = Math.floor(averageTimeLapse / sortedRequests.length);
    return averageTimeLapse;
}