class SegmentTree {
    constructor(n) {
        this.n = n;
        this.leafCount = 1;
        while (this.leafCount < n) this.leafCount *= 2;
        
        this.tree = new Array(2 * this.leafCount).fill(0);
        
        for (let i = 0; i < n; i++) {
            this.tree[this.leafCount + i] = 1;
        }
        for (let i = this.leafCount - 1; i > 0; i--) {
            this.tree[i] = this.tree[2 * i] + this.tree[2 * i + 1];
        }
        
        this.existsArray = new Array(n).fill(true);
    }
    
    exists(index) {
        return this.existsArray[index];
    }
    
    delete(index) {
        if (!this.existsArray[index]) return;
        
        this.existsArray[index] = false;
        this.update(index, 0);
    }
    
    restore(idx) {
        if (this.existsArray[idx]) return;
        
        this.existsArray[idx] = true;
        this.update(idx, 1);
    }
    
    update(index, value) {
        let i = this.leafCount + index;
        this.tree[i] = value;
        
        while (i > 1) {
            i = Math.floor(i / 2);
            this.tree[i] = this.tree[2 * i] + this.tree[2 * i + 1];
        }
    }
    
    sumPrefix(index) {
        if (index < 0) return 0;
        
        let sum = 0;
        let left = this.leafCount;
        let right = this.leafCount + index;
        
        while (left <= right) {
            if (left % 2 === 1) { 
                sum += this.tree[left];
                left++;
            }
            if (right % 2 === 0) { 
                sum += this.tree[right];
                right--;
            }
            left = Math.floor(left / 2);
            right = Math.floor(right / 2);
        }
        
        return sum;
    }
    
    findKthExistingUp(current, k) {
        let existingAboveCurrent = this.sumPrefix(current);
        let targetExisting = existingAboveCurrent - k;
        
        if (targetExisting < 0) return 0;
        
        let left = 0;
        let right = current;
        
        while (left < right) {
            let mid = Math.floor((left + right) / 2);
            let existingAboveMid = this.sumPrefix(mid);
            if (existingAboveMid >= targetExisting) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left; // smallest index satisfying it
    }
    
    findKthExistingDown(current, k) {
        let existingBelowCurrent = this.sumPrefix(current);
        let targetExisting = existingBelowCurrent + k;
        if (targetExisting > this.tree[1]) {
            return this.findLastExisting();
        }
        
        let left = current;
        let right = this.n - 1;
        
        while (left < right) {
            let mid = Math.floor((left + right) / 2);
            let existingAboveMid = this.sumPrefix(mid);
            if (existingAboveMid >= targetExisting) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left // smallest index satisfying it
    }
    
    findNextExisting(current) {
        let prefix = this.sumPrefix(current);
        if (prefix === this.tree[1]) return -1;
        return this.findKth(prefix + 1);
    }
    
    findPrevExisting(current) {
        if (current === 0) return -1;
        let prefix = this.sumPrefix(current - 1);
        if (prefix === 0) return -1;
        return this.findKth(prefix);
    }
    
    findLastExisting() {
        const total = this.tree[1];
        if (total === 0) return -1;
        return this.findKth(total);
    }
    
    findKth(k) {
        let idx = 1;
        while (idx < this.leafCount) {
            if (this.tree[2 * idx] >= k) {
                idx = 2 * idx;
            } else {
                k -= this.tree[2 * idx];
                idx = 2 * idx + 1;
            }
        }
        return idx - this.leafCount;
    }
}

function solution(n, k, commandStrings) {
    const commands = commandStrings.map((commandString) => {
        const [ type, stepCountString ] = commandString.split(' ');
        return [ type, Number(stepCountString) ];
    });
    
    const segmentTree = new SegmentTree(n);
    let current = k;
    const deletedStack = [];
    
    commands.forEach(([ type, stepCount ], index) => {
        if (type === 'U') {
            current = segmentTree.findKthExistingUp(current, stepCount);
        }
        else if (type === 'D') {
            current = segmentTree.findKthExistingDown(current, stepCount);
        } else if (type === 'C') {
            deletedStack.push(current);
            segmentTree.delete(current);
            const nextRow = segmentTree.findNextExisting(current);
            if (nextRow !== -1) {
                current = nextRow;
            } else {
                current = segmentTree.findPrevExisting(current);
            }
        } else if (type === 'Z') {
            const restore = deletedStack.pop();
            segmentTree.restore(restore);
        } else {
            throw new Error('Command type not found');
        }
        
    })
    
    return segmentTree.existsArray.map((exists) => exists ? 'O' : 'X').join('');
    
}