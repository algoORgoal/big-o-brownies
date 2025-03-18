// Custom Deque 구현 (head, tail 포인터를 사용하는 방식)

class Deque {
    constructor(arr) {
        const entries = arr.map((element, index) => [ index, element ]);
        this.items = new Map(entries);
        this.head = 0;
        this.tail = this.items.size;
    }
    
    get size() {
        return this.items.size;
    }
    
    get isEmpty() {
        return this.size === 0;
    }
    
    unshift(node) {
        this.head -= 1;
        this.items.set(this.head, node);
    }
    
    shift() {
        if (this.isEmpty) return null;
        const node = this.items.get(this.head);
        this.items.delete(this.head);
        this.head += 1;
        return node;
    }
    
    push(node) {
        this.items.set(this.tail, node);
        this.tail += 1;
    }
    
    pop() {
        if (this.isEmpty) return null;
        this.tail -= 1;
        const node = this.items.get(this.tail);
        this.items.delete(this.tail);
        return node;
    }
    
    get first() {
        if (this.isEmpty) return null;
        return this.items.get(this.head);
    }
    
    get last() {
        if (this.isEmpty) return null;
        return this.items.get(this.tail - 1);
    }
    
    get(index) {
        if (!this.items.has(this.head + index)) return null;
        return this.items.get(this.head + index);
    }
}



function solution(rc, operations) {
    const [ rowCount, columnCount ] = [ rc.length, rc[0].length ];
    const firstColumn = new Deque(Array.from({ length: rowCount }, (_, index) => rc[index][0]));
    const lastColumn = new Deque(Array.from({ length: rowCount }, (_, index) => rc[index][columnCount - 1]));
    const rows = new Deque(Array.from({ length: rowCount, }, (_, i) => new Deque(Array.from({ length: columnCount - 2, }, (_, j) => rc[i][j + 1]))));
    
    operations.forEach((operation) => {
        if (operation === "ShiftRow") {
            firstColumn.unshift(firstColumn.pop());
            lastColumn.unshift(lastColumn.pop());
            rows.unshift(rows.pop());
        } else {
            rows.first.unshift(firstColumn.shift());
            lastColumn.unshift(rows.first.pop());
            rows.last.push(lastColumn.pop());
            firstColumn.push(rows.last.shift());
        }
    });
    
    const result = [];
    for (let i = 0; i < rowCount; i++) {
        const first = firstColumn.get(i);
        
        const row = rows.get(i);
            
        const middle = Array.from({ length: row.size }, (_, index) => row.get(index));
        const last = lastColumn.get(i);
        const completed = [ first, ...middle, last ];
        
        result.push(completed);
    }
    
    return result;
}