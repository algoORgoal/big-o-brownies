// bfs로 탐색
// 현재 노드가 이미 방문되었던 경우 => 더 짧은 경로로 방문되었다는 뜻이므로 omit
// 시간 복잡도: O(mn)

class Queue {
    constructor() {
        this.first = [];
        this.second = [];
    }
    
    enqueue(element) {
        this.first.push(element);
    }
    
    dequeue() {
        if (this.isEmpty()) {
            return null;
        }
        if (this.second.length > 0) {
            return this.second.pop();
        }
        while (this.first.length > 0) {
            this.second.push(this.first.pop());
        }
        return this.second.pop();
    }
    
    length() {
        return this.first.length + this.second.length;
    }
    
    isEmpty() {
        return this.length() === 0;
    }
}

const isPositionSame = ([ x1, y1 ], [ x2, y2 ]) => x1 === x2 && y1 === y2;

const getNearbyPositions = (maps, [ x, y ]) => {
    const nearbyPositions = [[ x + 1, y ], [ x, y + 1 ], [ x - 1, y ], [ x, y - 1]];
    return nearbyPositions.filter(([ nextX, nextY ]) => 0 <= nextX && nextX <= maps.length - 1 && 0 <= nextY && nextY <= maps[0].length - 1 && maps[nextX][nextY] === 1);
}

function solution(maps) {
    const targetPosition = [ maps.length - 1, maps[0].length - 1 ];
    const queue = new Queue();
    const root = {
        position: [0, 0],
        distance: 1,
    };
    
    const isVisited = Array.from({ length: maps.length }, () => Array.from({ length: maps[0].length, }, (element, index) => false));
    queue.enqueue(root);
    isVisited[0][0] = true;
    
    while (!queue.isEmpty()) {
        const node = queue.dequeue();
        if (isPositionSame(node.position, targetPosition)) {
            return node.distance;
        }
        
        const nearbyPositions = getNearbyPositions(maps, node.position);
        const nextDistance = node.distance + 1;
        for (let nearbyPosition of nearbyPositions) {
            const [ nextX, nextY ] = nearbyPosition;
            if (isVisited[nextX][nextY]) continue;
            queue.enqueue({
                position: [ nextX, nextY ],
                distance: nextDistance,
            });
            isVisited[nextX][nextY] = true;
        }
    }
    
    return -1;
}