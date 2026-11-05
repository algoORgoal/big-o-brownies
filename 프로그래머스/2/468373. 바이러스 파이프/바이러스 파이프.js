class Deque {
    constructor() {
        this.table = {};
        this.next = 0;
        this.prev = -1;
    }
    
    pushLeft(element) {
        this.table[this.prev] = element;
        this.prev -= 1;
    }
    
    pushRight(element) {
        this.table[this.next] = element;
        this.next += 1;
    }
    
    popLeft() {
        if (this.next - this.prev === 1) {
            return;
        }
        this.prev += 1;
        const element = this.table[this.prev];
        return element;
    }
    
    popRight() {
        if (this.next - this.prev === 1) {
            return;
        }
        this.next -= 1;
        const element = this.table[this.next];
        return element;
    }
    
    head() {
        if (this.next - this.prev === 1) {
            return null;
        }
        return this.table[this.next - 1];
    }
    
    tail() {
        if (this.next - this.prev === 1) {
            return null;
        }
        return this.table[this.prev + 1];
    }
    
    size() {
        return (this.next - this.prev) - 1;
    }
}


function solution(n, infection, edges, k) {
    const permutations = [];
    permutate(permutations, [], [ 1, 2, 3 ], k);
    
    
    const nodes = Array.from({ length: n }).map((_, index) => index + 1);
    const graph = constructGraph(nodes, edges);
    
    let maxTotal = Number.MIN_VALUE;
    
    for (let permutation of permutations) {
        const infectedNodes = new Set([ infection ]);
        for (let type of permutation) {
            bfs(graph, type, infectedNodes)
        }
        
        maxTotal = Math.max(maxTotal, infectedNodes.size);
    }
    
    return maxTotal;
}

function constructGraph(nodes, edges) {
    
    const graph = nodes.reduce((acc, node) => {
        acc[node] = [];
        return acc;
    }, {})
    
    edges.forEach(([ x, y, type]) => {
        graph[x].push([ y, type ]);
        graph[y].push([ x, type ]);
    });
    
    return graph;
}

function permutate(permutations, permutation, elements, k) {
    if (permutation.length === k) {
        permutations.push([ ...permutation ]);
        return;
    }
    
    elements.forEach((element) => {
        permutation.push(element);
        permutate(permutations, permutation, elements, k);
        permutation.pop();
    });
}


function bfs(graph, type, infectedNodes){
    const deque = new Deque();
    
    infectedNodes.forEach((node) => {
        deque.pushRight(node);
    });
    
    const visited = new Set();
    
    while (deque.size() > 0) {
        const node = deque.popLeft();
        
        if (visited.has(node)) {
            continue
        }
        
        visited.add(node);
        infectedNodes.add(node);
        
        
        
        for (let [ adjacentNode, pipeType ] of graph[node]) {
            if (type === pipeType) {
                deque.pushRight(adjacentNode);
            }
        }
    }
}

// A, B, C 3개 중 선택 가능
// 파이프 여는 경우의 수 => 3 ** 10
// 한번 열었을 때 type 같은 경로 계속 선택해서 바이러스 추가 가능
// 시간 복잡도 O(3 ** 10 * 100) => 5904900
// 상태: (노드)

// 1. permutations 만들기
// 2. permutation 순회하면서, 현재 바이러스 걸린 노드들 시작점으로 모두 탐색하기
// 3. 바이러스 걸린 노드 총 개수 반환하기
