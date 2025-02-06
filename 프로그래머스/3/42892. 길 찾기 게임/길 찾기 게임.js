function solution(nodeinfo) {
    const nodeTable = nodeinfo.reduce((accumulator, [ x, y ], index) => {
        accumulator[index + 1] = [ x, y ];
        return accumulator;
    }, {});
    
    const nodes = Array.from({ length: nodeinfo.length }, (_, index) => index + 1);
    const sortedNodes = nodes.sort((node1, node2) => {
        return nodeTable[node2][1] - nodeTable[node1][1] ? nodeTable[node2][1] - nodeTable[node1][1] : nodeTable[node1][0] - nodeTable[node2][0];
    });
    
    const tree = generateTree(sortedNodes, nodeTable);
    const preorderHistory = preorderTraverse(tree, sortedNodes[0]);
    const postorderHistory = postorderTraverse(tree, sortedNodes[0]);
    
    return [ preorderHistory, postorderHistory ];
}

function generateTree(sortedNodes, nodeTable) {
    const root = sortedNodes[0];
    
    const graph = {
        [root]: [ -1, -1 ],
    };
    
    const descendants = sortedNodes.slice(1);
    
    descendants.forEach((target) => {
        let node = root;
        while (true) {
            const [ left, right ] = graph[node];
            if (left === -1 && nodeTable[target][0] < nodeTable[node][0]) {
                graph[node][0] = target;
                graph[target] = [ -1, -1 ];
                break;
            }
            if (right === -1 && nodeTable[target][0] > nodeTable[node][0]) {
                graph[node][1] = target;
                graph[target] = [ -1, -1 ];
                break;
            }
                
                
            if (nodeTable[target][0] < nodeTable[node][0]) {
                node = left;
            }
            else if (nodeTable[target][0] > nodeTable[node][0]) {
                node = right;
            }
        }        
    });
    
    return graph;
}

function preorderTraverse(tree, root) {
    
    const stack = [ root ];
    const history = [];
    
    while (stack.length) {
        const node = stack.pop();
        history.push(node);
        
        const [ left, right ] = tree[node];
        if (right !== -1) stack.push(right);
        if (left !== -1) stack.push(left);
    }
    return history;
}

function postorderTraverse(tree, root) {
    const stack = [ { node: root, isVisited: false } ];
    const history = [];
    
    while (stack.length) {
        const { node, isVisited } = stack.pop();
        
        if (!isVisited) {
            const [ left, right ] = tree[node];
            
            stack.push({ node, isVisited: true });
            if (right !== -1) stack.push({ node: right, isVisited: false });
            if (left !== -1) stack.push({ node: left, isVisited: false });
            continue;
        }
        history.push(node);
    }
    return history;
}
    