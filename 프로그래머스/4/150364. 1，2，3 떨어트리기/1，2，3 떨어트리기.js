// construct a tree 

// O(n + m)
// 떨어뜨린 뒤에 selected leaf node가 정해진다, 이 때 주어진 방문 조합으로 target을 만들 수 있는지 확인한다.
// 만족시키는지 확인: O(n)
// O(n^2): 최대 n개의 리프노드에 n을 채워넣음 


const generateGraph = (edges) => edges.reduce((accumulator, [ source, destination ]) => {
    if (!accumulator[source]) {
        accumulator[source] = {
            children: [ destination ],
            selected: 0,
        }
        return accumulator;
    }
    accumulator[source].children.push(destination);
    return accumulator;
}, {});

const sortChildren = (graph) => Object.keys(graph).map((parent) => graph[parent].children.sort((a, b) => a - b));

const drop = (graph, node = 1) => {
    if(!graph[node]) return node;
    const leaf = drop(graph, graph[node].children[graph[node].selected]);
    graph[node].selected = (graph[node].selected + 1) % graph[node].children.length;
    return leaf;
}



function solution(edges, target) {
    const tree = generateGraph(edges);
    sortChildren(tree);
    const selectedLeaves = {};
    const indexedTarget = [ 0, ...target ];

    const sequence = [];
    while (true) {
        const leaf = drop(tree);
        sequence.push(leaf);
        if (!selectedLeaves[leaf]) selectedLeaves[leaf] = 0;
        selectedLeaves[leaf] += 1;
        if (Object.entries(selectedLeaves).some(([ node, visitCount ]) => visitCount > target[node - 1])) return [ -1 ];
        if (indexedTarget.every((sum, node) => sum === 0 || (selectedLeaves[node] && selectedLeaves[node] * 3 >= sum))) break;
    }
    
    const table = Object.entries(selectedLeaves).reduce((accumulator, [ leaf, visitCount ]) => {
        const sum = indexedTarget[leaf];
        if (visitCount === 1) {
            accumulator[leaf] = [ sum ];
            return accumulator;
        }
        const values = Array.from({ length: visitCount, }, () => 3);
        let offset = values.reduce((accumulator, value) => accumulator + value, 0) - sum;
        for (let i = values.length - 1; i >= 0 && offset > 0; i--) {
            if (offset === 1) {
                values[i] -= 1;
                offset -= 1;
                continue;
            }
            values[i] -= 2;
            offset -= 2;
        }
        accumulator[leaf] = values;
        return accumulator;
    }, {});
    
    const answer = sequence.reduce((accumulator, leaf) => {
        const value = table[leaf].pop();
        accumulator.push(value);
        return accumulator;
    }, []);
    return answer;
}