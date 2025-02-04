class MinMaxHeap {
    constructor() {
        this.heap = [];
    }
    
    isInRange(index) {
        return index < this.heap.length;
    }
    
    get isEmpty() {
        return this.heap.length === 0;
    }
    
    getLevel(index) {
        return Math.floor(Math.log2(index + 1));
    }
    
    getChildrenIndices(index) {
        return [ 2 * index + 1, 2 * index + 2 ];
    }
    
    getParentIndex(index) {
        return Math.floor((index - 1) / 2);
    }
    
    getGrandchildrenIndices(index) {
        return this.getChildrenIndices(index).flatMap((childIndex) => {
            return this.getChildrenIndices(childIndex)
        });
    }
    
    checkMinLevel(index) {
        return this.getLevel(index) % 2 === 0;
    }
    
    swap(index1, index2) {
        [ this.heap[index1], this.heap[index2] ] = [ this.heap[index2], this.heap[index1] ];
    }
    
    findExtremumIndex(indexes, isMinLevel) {
        return indexes.reduce((accumulator, index) => {
            if (!this.isInRange(index)) return accumulator;
            if (isMinLevel && (this.heap[accumulator] < this.heap[index])) return accumulator;
            if (!isMinLevel && (this.heap[accumulator] > this.heap[index])) return accumulator;
            return index;
        });
    }
    
    bubbleUp(index) {
        if (index === 0) return;
    
        const isMinLevel = this.checkMinLevel(index);
        const parentIndex = this.getParentIndex(index);
        if (index === this.heap.length - 1 && ((isMinLevel && this.heap[index] > this.heap[parentIndex]) || (!isMinLevel && this.heap[index] < this.heap[parentIndex]))) { 
            this.swap(index, parentIndex);
            index = parentIndex;
            this.bubbleUp(index);
            return;
        }

        if (index <= 2) return;

        const grandparentIndex = Math.floor(((Math.floor((index - 1) / 2)) - 1) / 2);
        if ((isMinLevel && this.heap[index] < this.heap[grandparentIndex]) || (!isMinLevel && this.heap[index] > this.heap[grandparentIndex])) {
            this.swap(index, grandparentIndex);
            this.bubbleUp(grandparentIndex);
        }
    }

    bubbleDown(index) {
        const isMinLevel = this.checkMinLevel(index);
        const childrenIndex = this.getChildrenIndices(index);
        const grandchildrenIndex = this.getGrandchildrenIndices(index);

        const extremumIndex = this.findExtremumIndex([ index, ...childrenIndex, ...grandchildrenIndex ], isMinLevel);
        if (index === extremumIndex) {
            return;
        }

        this.swap(index, extremumIndex);
        if (childrenIndex.some((childIndex) => childIndex === extremumIndex)) {
            return;
        }

        index = extremumIndex;
        const parentIndex = this.getParentIndex(index);

        if ((isMinLevel && (this.heap[index] > this.heap[parentIndex])) || (!isMinLevel && (this.heap[index] < this.heap[parentIndex]))) {
            [ this.heap[index], this.heap[parentIndex] ] = [ this.heap[parentIndex], this.heap[index] ];
            index = parentIndex;
        } 
        this.bubbleDown(index); 
    }

    
    insert(element) {
        this.heap.push(element);
        this.bubbleUp(this.heap.length - 1);
    }
    
    delete(shouldRemoveMin) {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();

        const extremumIndex = this.findExtremumIndex([ 0, 1, 2 ], shouldRemoveMin);
        this.swap(extremumIndex, this.heap.length - 1);
        const node = this.heap.pop();

        if (this.heap.length >= 2) this.bubbleDown(extremumIndex);

        return node;
    }
}

function solution(operations) {    
    const heap = new MinMaxHeap();
    
    operations.forEach((operation) => {
        const [ operationType, number] = operation.split(' ').map((element) => isNaN(element) ? element : Number(element));
        if (operationType === 'I') {
            heap.insert(number);
        }
        else if (operationType === 'D' && number === -1) {
            heap.delete(true);
        }
        else if (operationType === 'D' && number === 1) {
            heap.delete(false);
        }
    })
    
    if (heap.isEmpty) {
        return [ 0, 0 ];
    }
    return [ Math.max(...heap.heap), Math.min(...heap.heap) ]; 
    
    
}