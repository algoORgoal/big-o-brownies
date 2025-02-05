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
        if (this.front.length) return this.front.pop();
        while (this.back.length) {
            this.front.push(this.back.pop());
        }
        return this.front.pop();
    }
}

function solution(begin, target, words) {    
    const graph = [ begin, ...words ].reduce((accumulator, source, sourceIndex, array) => {
        
        if (!accumulator[source]) {
                accumulator[source] = [];
        }
        
        const adjacentWords = array.slice(sourceIndex + 1, array.length).filter((destination) => {
            const sameCharacterCount = [ ...source ].filter((_, i) => source[i] === destination[i]).length;
            if (sameCharacterCount === source.length - 1) return true;
            return false;
        });
        
        adjacentWords.forEach((adjacentWord) => {
            if (!accumulator[adjacentWord]) {
                accumulator[adjacentWord] = [];
            }
            accumulator[source].push(adjacentWord);
            accumulator[adjacentWord].push(source);
        });
        
        return accumulator;
    }, {});
        
    const root = [ begin , 0 ];
    const queue = new Queue();
    const visitedWords = new Set();
    
    queue.enqueue(root);
    visitedWords.add(begin);
    
    while (!queue.isEmpty) {        
        const [ node, distance ]  = queue.dequeue();
        if (node === target) return distance;
        
        graph[node].forEach((adjacentNode) => {
            if (!visitedWords.has(adjacentNode)) {
                visitedWords.add(adjacentNode);
                queue.enqueue([ adjacentNode, distance + 1 ]);
            }
        });
    }
    
    return 0;
}