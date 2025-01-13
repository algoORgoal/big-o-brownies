class Deque {
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
        if (this.isEmpty) {
            return null;
        }
        
        if (this.front.length === 0) {
            while (this.back.length > 0) {
                this.front.push(this.back.pop());
            }
        }
        
        return this.front.pop();
    }
    
    peek() {
        if (this.front.length) {
            return this.front[this.front.length - 1];
        }
        if (this.back.length) {
            return this.back[0];
        }
        return null;
    }
}

function solution(order) {
    const queue = new Deque();
    order.forEach((box) => {
        queue.enqueue(box);
    });
    
    const stack = [];
    
    const conveyorBelt = [ ...Array(order.length) ].map((_, index) => index + 1);
    
    conveyorBelt.forEach((currentBox) => {
        stack.push(currentBox);
        let demandedBox = queue.peek();
        let top = stack[stack.length - 1];
        while (demandedBox === top) {
            queue.dequeue();
            stack.pop();
            if (queue.isEmpty || stack.length === 0) {
                break;
            }
            demandedBox = queue.peek();
            top = stack[stack.length - 1];
        }
    });
    return order.length - queue.size;
}