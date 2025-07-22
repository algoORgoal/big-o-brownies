class MinHeap {
    constructor() {
        this.heap = [];
    }
    
    swap(i, j) {
        [ this.heap[i], this.heap[j] ] = [ this.heap[j], this.heap[i] ];
    }
    
    get size() {
        return this.heap.length;
    }
    
    getParent(index) {
        return Math.floor((index - 1) / 2);
    }
    
    bubbleUp() {
        let index = this.size - 1;
        while (index > 0) {
            const parent = this.getParent(index);
            if (this.heap[index] > this.heap[parent]) break;
            this.swap(index, parent);
            index = parent;
        }
    }
    
    insert(node) {
        this.heap.push(node);
        if (this.size > 1) {
            this.bubbleUp();
        }
    }
    
    getChildren(index) {
        return [ 2 * index + 1, 2 * index + 2];
    }
    
    bubbleDown() {
        let index = 0;
        while (index < this.size) {
            const [ left, right ] = this.getChildren(index);
            let smallest = index;
            if (left < this.size && this.heap[left] < this.heap[smallest]) smallest = left;
            if (right < this.size && this.heap[right] < this.heap[smallest]) smallest = right;
            if (smallest === index) break;
            this.swap(smallest, index);
            index = smallest;
        }
    }
    
    delete() {
        if (this.size === 1) return this.heap.pop();
        
        this.swap(0, this.size - 1);
        const root = this.heap.pop();        
        this.bubbleDown();

        return root;
    }
    
    get peak() {
        if (this.size === 0) return -1;
        return this.heap[0];
    }
}

function solution(scovilleList, K) {
    const heap = new MinHeap();
    
    scovilleList.forEach((scoville) => {
        heap.insert(scoville);
    });
    
    let mixCount = 0;
    while (heap.size >= 2) {
        if (heap.peak >= K) return mixCount;
        const [ weak1, weak2 ] = [ heap.delete(), heap.delete() ];
        const mixed = weak1 + (weak2 * 2)
        heap.insert(mixed);
        mixCount += 1;
    }
    
    if (heap.peak >= K) return mixCount;
    return -1;
    
    
}

// 한 음식을 만들어서 넣을 때 O(n)
// 최대 섞을 수 있는 음식의 개수 O(n)
// O(n) * O(n) = O(n^2)
// MinHeap을 사용하여, 가장 스코빌 지수가 낮은 두 요소를 꺼내서 다시 집어넣음
// 꺼내기 O(logn) + 집어넣기 O(logn) = O(logn)
// O(n) * O(logn) = O(nlogn)