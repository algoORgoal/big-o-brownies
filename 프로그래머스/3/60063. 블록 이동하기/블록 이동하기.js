// 한 자리에서 가능한 move의 개수는 8까지 (중심축 2개를 기준으로 시계 방향 / 반시계 방향 회전, 상/하/좌/우)
// 드론의 현재 좌표를 기준으로 bfs를 돌려서 최단 거리를 찾는다.

class Queue {
    constructor(){
        this.front = [];
        this.back = [];
    }
    
    get size() { 
        return this.front.length + this.back.length;
    }
    
    get isEmpty() {
        return this.size === 0;
    }
    
    insert(element) {
        this.back.push(element);
    }
    
    delete () {
        if (this.isEmpty) return null;
        if (this.front.length) return this.front.pop();
        while (this.back.length) {
            this.front.push(this.back.pop());
        }
        return this.front.pop();
    }
}

const json = (value) => JSON.stringify(value);

const up = ([[x1, y1], [x2, y2]]) => [[x1 - 1, y1], [x2 - 1, y2]];
const down = ([[x1, y1], [x2, y2]]) => [[x1 + 1, y1], [x2 + 1, y2]];
const left = ([[x1, y1], [x2, y2]]) => [[x1, y1 - 1], [x2, y2 - 1]];
const right = ([[x1, y1], [x2, y2]]) => [[x1, y1 + 1], [x2, y2 + 1]];

const move = (positions) => {
    return [ up(positions), down(positions), left(positions), right(positions) ];
}

const isValid = (board, positions) => {
    return positions.every(([ x, y ]) => x >= 0 && x < board.length && y >= 0 && y < board[0].length && board[x][y] !== 1);
}

const spin = (board, [[ x1, y1 ], [ x2, y2 ]]) => {
    // [ x2, y2 ]를 변경
    const candidates1 = [[ x1 + 1, y1 ], [ x1 - 1, y1 ], [ x1, y1 - 1 ], [ x1, y1 + 1 ]].filter(([ x, y ]) => {
        if (x === x2 && y === y2) return false;
        if (Math.abs(x - x2) === 1 && Math.abs(y - y2) === 1) {
            const [ cornerX, cornerY ] = [ x1 + (x - x1) + (x2 - x1), y1 + (y - y1) + (y2 - y1) ];
            if (isValid(board, [[ cornerX, cornerY ]])) return true;
            return false;
        }
        return true;
    }).map(([ x, y ]) => [[ x1, y1 ], [ x, y ]]);
    // [ x1, y1 ]을 변경
    const candidates2 = [[ x2 + 1, y2 ], [ x2 - 1, y2 ], [ x2, y2 - 1 ], [ x2, y2 + 1 ]].filter(([ x, y ]) => {
        if (x === x1 && y === y1) return false;
        if (Math.abs(x - x1) === 1 && Math.abs(y - y1) === 1) {
            const [ cornerX, cornerY ] = [ x2 + (x - x2) + (x1 - x2), y2 + (y - y2) + (y1 - y2) ];
            if (isValid(board, [[ cornerX, cornerY ]])) return true;
            return false;
        }
        return true;
    }).map(([ x, y ]) => [[ x, y ], [ x2, y2 ]]);
    return [ ...candidates1, ...candidates2 ]
}

function bfs(board) {
    const root = [[ 0, 0 ], [ 0, 1 ]];
    const target = [ board.length - 1, board[0].length - 1]
    const rootState = {
        node: root,
        count: 0,
    };
    const visitedStates = new Set([ json(root) ]);
    const queue = new Queue();
    queue.insert(rootState);
    while (!queue.isEmpty) {
        const { node, count } = queue.delete();
        
        if (node.some((element) => element[0] === target[0] && element[1] === target[1])) {
            return count;
        }
        
        const movedNodes = move(node).filter((node) => isValid(board, node));
        const spinnedNodes = spin(board, node).filter((node) => isValid(board, node));
        const candidates = [ ...movedNodes, ...spinnedNodes ]
        const nextNodes = candidates.map((node) => node.sort(([ x1, y1 ], [ x2, y2 ]) => x1 - x2 || y1 - y2));
                
        nextNodes.forEach((nextNode) => {
            const nextNodeKey = json(nextNode);
            if (!visitedStates.has(nextNodeKey)) {
                visitedStates.add(nextNodeKey);
                queue.insert({
                    node: nextNode,
                    count: count + 1,
                });
            }
        });
    }
    
    return -1;
}

function solution(board) {
    return bfs(board);
}

