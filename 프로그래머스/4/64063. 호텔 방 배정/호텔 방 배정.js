class DisjointSet {
    constructor() {
        this.parent = new Map();
        this.rank = new Map();
        this.nextAvailable = new Map();
    }
    
    add(n) {
        this.parent.set(n, n);
        this.rank.set(n, 1);
        this.nextAvailable.set(n, n + 1);
        if (this.parent.has(n - 1)) {
            this.union(n - 1, n);
        }
        if (this.parent.has(n + 1)) {
            this.union(n, n + 1);
        }
    }
    
    getNextAvailable(n) {
        const root = this.find(n);
        return this.nextAvailable.get(root);
    }
    
    find(n) {
        if (!this.parent.has(n)) return null;
        if (this.parent.get(n) === n) {
            return n;
        }
        const root = this.find(this.parent.get(n));
        this.parent.set(n, root);
        return root;
    }
    
    union(x, y) {
        const rootX = this.find(x);
        const rootY = this.find(y);
        if (rootX === null || rootY === null) return;
        const rankX = this.rank.get(rootX);
        const rankY = this.rank.get(rootY);
        const nextAvail = Math.max(this.nextAvailable.get(rootX), this.nextAvailable.get(rootY));
        
        if (rootX === rootY) return;
        if (rankX > rankY) {
            this.parent.set(rootY, rootX);
            this.nextAvailable.set(rootX, nextAvail);
        } else if (rankX < rankY) {
            this.parent.set(rootX, rootY);
            this.nextAvailable.set(rootY, nextAvail);
        } else {
            this.parent.set(rootX, rootY);
            this.nextAvailable.set(rootY, nextAvail);
            this.rank.set(rootY, rankY + 1);
        }
    }
}

function solution(k, roomNumbers) {
    const disjointSet = new DisjointSet();
    const answer = [];
    
    for (let num of roomNumbers) {
        const root = disjointSet.find(num);
        
        if (root === null) {
            disjointSet.add(num);
            answer.push(num);
        } else {
            const nextAvailable = disjointSet.getNextAvailable(root);
            disjointSet.add(nextAvailable);
            disjointSet.union(root, disjointSet.find(nextAvailable));
            answer.push(nextAvailable);
        }
        
    }
    
    return answer;
}