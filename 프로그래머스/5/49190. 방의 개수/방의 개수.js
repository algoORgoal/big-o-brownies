// create a graph using arrows
// Couting cycles don't work since if there is a edge inside a room, it's not a room anymore.

const convertToEdges = (directions) => directions.reduce((accumulator, direction, index) => {
    const previousPoint = index === 0 ? [ 0, 0 ] : accumulator[accumulator.length - 1][1];
    const newPoint = move(previousPoint, direction);
    const extendedEdges = extend(previousPoint, newPoint);
    accumulator.push(...extendedEdges);
    
    return accumulator;
}, []);

const move = ([ x, y ], direction) => {
    if (direction === 0) return [ x - 1, y ];
    if (direction === 1) return [ x - 1, y + 1 ];
    if (direction === 2) return [ x, y + 1 ];
    if (direction === 3) return [ x + 1, y + 1 ];
    if (direction === 4) return [ x + 1, y ];
    if (direction === 5) return [ x + 1, y - 1 ];
    if (direction === 6) return [ x, y - 1 ];
    if (direction === 7) return [ x - 1, y - 1 ];
}

const extend = ([ x1, y1, ], [ x2, y2, ]) => {
    const [ xOffset, yOffset ] = [ x2 - x1, y2 - y1 ];
    return [[[ x1, y1 ], [ x2, y2 ]], [[ x2, y2 ], [ x2 + xOffset, y2 + yOffset ]]];
}

const constructGraph = (edges) => edges.reduce((accumulator, [ source, destination ]) => {
    if (!(source in accumulator)) accumulator[source] = new Set();
    if (!(destination in accumulator)) accumulator[destination] = new Set();
    accumulator[source].add(json(destination));
    accumulator[destination].add(json(source));
    return accumulator;
}, {});

const json = (value) => JSON.stringify(value);
const parse = (value) => JSON.parse(value);

function dfs(graph) {
    const root = [ 0, 0 ];
    const rootState = {
        node: root,
        parent: null,
    }
    const visitedNodes = new Set([ json(root) ]);
    const stack = [ rootState ];
    let cycleCount = 0;
    while (stack.length) {
        const { node, parent } = stack.pop();
        
        const adjacentNodes = [ ...graph[node] ].map((str) => parse(str));
        adjacentNodes.forEach((adjacent) => {
            if (json(adjacent) !== json(parent) && visitedNodes.has(json(adjacent))) {
                cycleCount += 1;
            }
            if (json(adjacent) !== json(parent) && !visitedNodes.has(json(adjacent))) {
                visitedNodes.add(json(adjacent));
                stack.push({
                    node: adjacent,
                    parent: node,
                });
            }
            
        });
    }
    return cycleCount / 2;
}

function solution(arrows) {
    const edges = convertToEdges(arrows);
    const graph = constructGraph(edges);
    const cycleCount = dfs(graph);
    return cycleCount;
}

