function solution(tickets) {
    const ticketGraph = tickets.reduce((acc, [ source, destination ]) => {
        if (!(source in acc)) {
            acc[source] = {};
        }
        
        if (!(destination in acc[source])) {
            acc[source][destination] = 0;
        }
        
        acc[source][destination] += 1;
        return acc;
    }, {});
    
    const sortedTicketGraph = Object.entries(ticketGraph).reduce((acc, [ source, edge ]) => {
        acc[source] = [];
        Object.entries(edge).sort(([ destination1 ], [ destination2 ]) => destination1.localeCompare(destination2)).forEach(([ destination, count ]) => {
            acc[source].push([ destination, count ]);
        });
        
        return acc;
    }, {});
    
    
    const route = [];
    dfs("ICN", sortedTicketGraph, route);
    
    return route.reverse();
}

function dfs(node, graph, route) {
    
    const edges = graph[node];
    if (edges == null) {
        route.push(node);
        return;
    };
    
    edges.forEach((edge, index) => {
        const [ destination, count ] = edge;
        if (count > 0) {
            graph[node][index][1] -= 1;
            dfs(destination, graph, route);
        }
    });
    
    route.push(node);
}


// A <-> B -> C -> A
// A -> B -> C -> A -> B -> D


