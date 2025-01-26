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
    preorderTraverse(visited, str + 'A', depth + 1);
    preorderTraverse(visited, str + 'E', depth + 1);
    preorderTraverse(visited, str + 'I', depth + 1);
    preorderTraverse(visited, str + 'O', depth + 1);
    preorderTraverse(visited, str + 'U', depth + 1);
}