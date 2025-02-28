// 1. Contruct a tree
// 2. Post-order traverse to set weight to 0
// 3. Check if all the vertice weight has become zero
// time complexity: O(m) for contructing a graph, O(n) for contructing a tree, O(m + n) for post-order traversal
// space complexity: O(m + n) for graph and tree, O(n) for weightTable
// count <= maxWeight * (1 + 2 + ... + (n - 1)) = m * (n - 1)*n / 2 = 1_000_000 * 300_000 * 300_000 / 2 > Number.

const constructGraph = (edges) => edges.reduce((accumulator, [ source, destination ]) => {
    if (!(source in accumulator)) accumulator[source] = [];
    if (!(destination in accumulator)) accumulator[destination] = [];
    accumulator[source].push(destination);
    accumulator[destination].push(source);
    return accumulator;
}, {});

const convertToTree = (graph, root) => {
    const rootState = {
        node: root,
        parent: null,
    };
    
    const stack = [ rootState ];
    while (stack.length) {
        const { node, parent } = stack.pop();
        graph[node] = graph[node].filter((adjacent) => adjacent !== parent);
        graph[node].forEach((adjacent) => {
            stack.push({
                node: adjacent,
                parent: node,
            });
        });
    }
    return graph;
}

function postOrderTraverse(tree, weights, root) {
    const weightTable = weights.reduce((accumulator, weight, node) => {
        accumulator.set(node, weight);
        return accumulator;
    }, new Map());
    

    const rootState = {
        node: root,
        parent: null,
        visited: false,
    };
    const stack = [ rootState ];
    let count = 0n;
    while (stack.length) {
        const { node, parent, visited } = stack.pop();
        if (!visited) {
            stack.push({
                node,
                parent,
                visited: true,
            });
            
            tree[node].forEach((child) => {
                stack.push({
                    node: child,
                    parent: node,
                    visited: false,
                });
            });
            
            continue;
        }
        
        if (node === root) continue;
        const weight = weightTable.get(node);
        const parentWeight = weightTable.get(parent);
        count += BigInt(Math.abs(weight));
        weightTable.set(node, weight - weight);
        weightTable.set(parent, parentWeight + weight);
    }
    
    return weightTable.get(root) === 0 ? count : -1; 
}

function solution(a, edges) {
    // a = a.map(d => BigInt(d));
    const graph = constructGraph(edges);
    const tree = convertToTree(graph, 0);
    return postOrderTraverse(tree, a, 0);
}