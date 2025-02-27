// Construct a tree and virtualy set 1 as root node.
// Create a dp array and post-order traverse the array and compute the folloing:
// dp[node] = (sum of dp when choosing all the children), (sum of dp when choosing the minimum cost of each subtree)
// return min(dp[root])
// time complexity: O(n + m) = O(n) for post order traversing
// space complexity: O(m) = O(n) for maintaing tree


const constructGraph = (edges) => edges.reduce((accumulator, [ source, destination ]) => {
    if (!(source in accumulator)) accumulator[source] = [];
    if (!(destination in accumulator)) accumulator[destination] = [];
    accumulator[source].push(destination);
    accumulator[destination].push(source);
    return accumulator;
}, {});

const convertToTree = (graph, root) => {
    const stack = [ root ];
    while (stack.length) {
        const node = stack.pop();
        
        if (!graph[node]) continue;
        graph[node].forEach((adjacent) => {
            graph[adjacent] = graph[adjacent].filter((adjacentNeighbor) => adjacentNeighbor !== node);
            stack.push(adjacent);
        });
    }
    
    return graph;
}


const getChildren = (graph, node) => graph[node];

function postOrderTraverse(tree) {
    const root = 1;
    const rootState = {
        node: root,
        visited: false,
    };
    const stack = [ rootState ];
    const computed = new Map();
    
    while (stack.length) {
        const { node, visited } = stack.pop();
        if (!visited) {
            stack.push({
                node,
                visited: true,
            });
            
            const children = getChildren(tree, node);
            children.forEach((nextNode) => {
                    stack.push({
                        node: nextNode,
                        visited: false,
                    });
            });
            continue;
        }
        
        const children = getChildren(tree, node);
        if (children.length === 0) {
            computed.set(node, [ 1, 0 ]);
            continue;
        }
        
        const costWithoutNode = children.reduce((accumulator, child) => accumulator + computed.get(child)[0], 0);
        const costWithNode = children.reduce((accumulator, child) => accumulator + Math.min(...computed.get(child)), 0) + 1;
        
        computed.set(node, [ costWithNode, costWithoutNode ]);
    }
    
    return Math.min(...computed.get(root));
}

function solution(n, lighthouse) {
    const graph = constructGraph(lighthouse);
    const tree = convertToTree(graph, 1);
    return postOrderTraverse(tree);
}

