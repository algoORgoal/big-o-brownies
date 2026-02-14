function solution(word) {
    
    
    return preorderTraverse(word);
}

let found = false;

function preorderTraverse(target, str = "", depth = 0, count = 0) {
    console.log(str, count);
    if (str === target) {
        return count;
    }
    
    if (depth === 5) {
        return -1;
    }
    
    for (let character of [ 'A' , 'E', 'I', 'O', 'U' ]) {
        const result = preorderTraverse(target, str + character, depth + 1, count + 1);
        if (result !== -1) {
            return result;
        }
    }
    return -1;
}