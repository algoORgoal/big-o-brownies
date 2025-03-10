class UnionFind {
    constructor(n) {
        this.parent = {};
        this.rank = {};
        this.nextAvailable = {};
    }
    
    find(x) {
        if (!(x in this.parent)) {
            return null;
        }
        if (this.parent[x] !== x) {
            this.parent[x] = this.find(this.parent[x]);
        }
        return this.parent[x];
    }
    
    union(a, b) {
        let rootA = this.find(a);
        let rootB = this.find(b);
        
        if (rootA === null || rootB === null || rootA === rootB) return;
        
        if (this.rank[rootA] > this.rank[rootB]) {
            this.parent[rootB] = rootA;
            this.nextAvailable[rootA] = Math.max(this.nextAvailable[rootA], this.nextAvailable[rootB]);
        } else {
            this.parent[rootA] = rootB;
            this.nextAvailable[rootB] = Math.max(this.nextAvailable[rootA], this.nextAvailable[rootB]);
            if (this.rank[rootA] === this.rank[rootB]) {
                this.rank[rootB] += 1;
            }
        } 
    }
    
    
    
    getNextAvailable(x) {
        const root = this.find(x);
        return root !== null ? this.nextAvailable[root] : x;
    }
    
    addAndMerge(x) {
        if (!(x in this.parent)) {
            this.parent[x] = x;
            this.rank[x] = 1;
            this.nextAvailable[x] = x + 1;
        }
        
        if (x - 1 in this.parent) {
            this.union(x, x - 1);
        }
        
        if (x + 1 in this.parent) {
            this.union(x, x + 1);
        }
    }
}

function solution(k, roomNumbers) {
    const unionFind = new UnionFind();
    const assignedRooms = roomNumbers.reduce((accumulator, roomNumber) => {
        const root = unionFind.find(roomNumber);
        
        if (root === null) {
            accumulator.push(roomNumber);
            unionFind.addAndMerge(roomNumber);
        } else {
            const newRoom = unionFind.getNextAvailable(roomNumber);
            accumulator.push(newRoom);
            unionFind.addAndMerge(newRoom);
        }
        return accumulator;
    }, []);
    
    return assignedRooms;

    
}