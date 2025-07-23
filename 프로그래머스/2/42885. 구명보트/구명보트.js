class Deque {
    constructor() {
        this.deque = new Map();
        this.head = 0;
        this.tail = 0;
    }
    
    get size() {
        return this.tail - this.head;
    }
    
    isEmpty() {
        return this.size === 0;
    }
    
    push(element) {
        this.deque.set(this.tail, element);
        this.tail += 1;
    }
    
    unshift(element) {
        this.head -= 1;
        this.deque.set(this.head, element);
    }
    
    pop() {
        if (this.isEmpty()) return null;
        this.tail -= 1;
        const lastElement = this.deque.get(this.tail);
        this.deque.delete(this.tail);
        return lastElement;
    }
    
    shift() {
        if (this.isEmpty()) return null;
        const firstElement = this.deque.get(this.head);
        this.deque.delete(this.head);
        this.head += 1;
        return firstElement;
    }
    
    get first() {
        return this.deque.get(this.head);
    }
    
    get last() {
        return this.deque.get(this.tail - 1);
    }
}

function solution(people, limit) {
    const sortedPeople = people.sort((a, b) => b - a);
    const deque = new Deque();
    sortedPeople.forEach((person) => {
        deque.push(person);
    });
    
    let boatCount = 0;
    while (!deque.isEmpty()) {
        if (deque.size >= 2 && (deque.first + deque.last <= limit)) {
            deque.shift();
            deque.pop();
        } else if (deque.first <= limit) {
            deque.shift();
        } else {
            throw deque;
        }
        boatCount += 1;
    }
    return boatCount;
}

// 50_000 * 50_000 = 25 * 10^8 = 2.5 * 10^9
// 1_000_000_000

// 정렬 후 deque에 넣기
// 가장 큰 수 꺼내서 확인 -> 
//    1. 가장 작은 수와 합 <= limit -> 둘 다 빼버리기
//    2. 가장 작은 수와 합 > limit > 하나만 넣기