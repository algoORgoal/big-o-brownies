function solution(k, num, links) {
    const graph = links.reduce((accumulator, [ leftChild, rightChild ], node) => {
        accumulator[node] = [ leftChild, rightChild ];
        return accumulator;
    }, {});
    
    const subnodes = new Set(links.flatMap((children) => children).filter((child) => child !== -1));
    const root = links.findIndex((_, node) => !subnodes.has(node));
    const minimizedMaximumSum = binarySearch([ graph, num, root ], k - 1);
    return minimizedMaximumSum;
}

function binarySearch(traverseArgs, upperbound) {
    let start = 0;
    let end = 10_000 * 10_000;
    while (start !== end) {
        const middle = Math.floor((start + end) / 2);
        const [ _, cuts ] = postOrderTraverse(...traverseArgs, middle);
        if (cuts > upperbound) {
            start = middle + 1;
        } else {
            end = middle;
        }
    }
    return start;
}

function postOrderTraverse(graph, num, root, upperbound) {
    
    const stack = [{ node: root, isVisited: false }];
    const computed = new Map();
    
    while (stack.length) {
        const { node, isVisited } = stack.pop();
        
        if (node === -1) continue;
        
        if (!isVisited) {
            stack.push({ node, isVisited: true });
            const [ left, right ] = graph[node];
            if (left !== -1) stack.push({ node: left, isVisited: false });
            if (right !== -1) stack.push({ node: right, isVisited: false });
            
        } else {
            const leftResult = graph[node][0] !== -1 ? computed.get(graph[node][0]) : null;
            const rightResult = graph[node][1] !== -1 ? computed.get(graph[node][1]) : null;
            const result = computeForNode(node, num[node], leftResult, rightResult, upperbound);
            computed.set(node, result);
        }
    }
    
    return computed.get(root);
}

function computeForNode(node, nodeValue, leftResult, rightResult, upperbound) {
    if (!leftResult && !rightResult) return nodeValue <= upperbound ? [ nodeValue, 0 ] : [ nodeValue, Infinity ];
    if (leftResult && rightResult) {
        const totalResult = [ leftResult[0] + rightResult[0], leftResult[1] + rightResult[1] ];
        if (totalResult[0] + nodeValue <= upperbound) {
            return [ totalResult[0] + nodeValue, totalResult[1] ];
        }
        
        const smallerResult = leftResult[0] < rightResult[0] ? leftResult : rightResult;
        if (smallerResult[0] + nodeValue <= upperbound) {
            return [ smallerResult[0] + nodeValue, totalResult[1] + 1 ];
        }
        if (nodeValue <= upperbound) {
            return [ nodeValue, totalResult[1] + 2 ];
        }
        return [ nodeValue, Infinity ];
    }
    if (leftResult) {
        if (leftResult[0] + nodeValue <= upperbound) {
            return [ leftResult[0] + nodeValue, leftResult[1] ];
        }
        if (nodeValue <= upperbound) {
            return [ nodeValue, leftResult[1] + 1 ];
        }
        return [ nodeValue, Infinity ];
    }
    if (rightResult) {
        if (rightResult[0] + nodeValue <= upperbound) {
            return [ rightResult[0] + nodeValue, rightResult[1] ];
        }
        if (nodeValue <= upperbound) {
            return [ nodeValue, rightResult[1] + 1 ];
        }
        return [ nodeValue, Infinity ];
    }
}