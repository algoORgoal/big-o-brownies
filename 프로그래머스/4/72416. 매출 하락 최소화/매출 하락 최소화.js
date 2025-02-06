function solution(sales, links) {
    const graph = links.reduce((accumulator, [ source, destination ]) => {
        if (!accumulator[source]) {
            accumulator[source] = [];
        }
        accumulator[source].push(destination);
        return accumulator;
    }, {});
    
    return postOrderTraverse(graph, sales);
}

const checkLeafNode = (graph, node) => !graph[node];
const getChildren = (graph, node) => graph[node];

function postOrderTraverse(graph, weights) {
    const root = {
        node: 1,
        isVisited: false,
    };
    
    const stack = [ root ];
    const computed = new Map();
    
    while (stack.length) {
        const { node, isVisited } = stack.pop();
        
        if (!isVisited) {
            stack.push({ node, isVisited: true });
            const children = getChildren(graph, node);
            if (children) children.forEach((child) => stack.push({ node: child, isVisited: false }));    
            continue;;
        } 
                
        if (checkLeafNode(graph, node)) {
            computed.set(node, [ weights[node - 1], 0 ]);
            continue;
        }
        
        
        const children = graph[node];
        
        const minimizedChildrenWeightSum = children.reduce((sum, child) => sum + Math.min(...computed.get(child)), 0);
        
        
        const included = weights[node - 1] + minimizedChildrenWeightSum;
        
        const isMinimizedChildIn = children.some((child) => {
            const [ included, excluded ] = computed.get(child);
            return included <= excluded;
        });
        
        if (isMinimizedChildIn) {
            const excluded = minimizedChildrenWeightSum;
            computed.set(node, [ included, excluded ]);
            continue;
        } 
        
        const minimizedAdditionalCost = Math.min(...children.map((child) => {
            const [ included, excluded ] = computed.get(child);
            return included - excluded;
        }));
        
        const excluded = minimizedChildrenWeightSum + minimizedAdditionalCost;
        computed.set(node, [ included, excluded ]);
        
    }
    
    return Math.min(...computed.get(1));
}


// 1. 현재 노드가 참가 안 할 때 / 참가 할 때의 비용을 각각 계산한다.
// 2. 현재 노드가 참가 안 할 때: child는 참가 안 할 때 비용 / 참가 할 때 비용 중 최소를 골라 합을 구한다.
// 3. 현재 노드가 참가 할 때: 비용 중 최소를 고를 때 child 중 한명이 참가하면, 부모-자식 관계에서 한 노드가 선택되므로 그냥
//    전에 구했던 합을 그대로 대입한다 만약 아무도 참가를 안 한다면, 추가 비용이 최소가 되는 child를 참가시킨다.
  
