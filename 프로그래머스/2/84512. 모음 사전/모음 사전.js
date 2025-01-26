function solution(word) {
    
    const visited = []
    preorderTraverse(visited, '');
    return visited.findIndex((term) => term === word) + 1;
}
        
function preorderTraverse(visited, str, depth = 0) {
    if (str) {
        visited.push(str);
    }
    
    if (depth === 5) {
        return;
    }
    
    [ 'A', 'E', 'I', 'O', 'U' ].forEach((character) => {
        preorderTraverse(visited, str + character, depth + 1);
    });
}